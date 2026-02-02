import os
import math
import hashlib

MOCK_MODE = os.getenv("MOCK_GEOCODING", "true").lower() == "true"


def get_coordinates(address):
    """Convert address to latitude/longitude coordinates."""
    if MOCK_MODE:
        return _mock_geocode(address)
    
    import requests
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params={"address": address, "key": api_key}
    )
    data = response.json()
    location = data["results"][0]["geometry"]["location"]
    return location["lat"], location["lng"]


def _mock_geocode(address):
    """Generate consistent fake coordinates for testing."""
    h = int(hashlib.md5(address.encode()).hexdigest()[:8], 16)
    lat = 40.0 + (h % 1000) / 1000
    lng = -74.0 + ((h >> 10) % 1000) / 1000
    return lat, lng


def calculate_distance(coord1, coord2):
    """Calculate distance between two coordinates in kilometers."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    r = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return r * c


def find_nearest_store(user_address, stores):
    """Find the store closest to the user's address."""
    user_coords = get_coordinates(user_address)
    
    closest = None
    min_distance = float("inf")
    
    for store in stores:
        store_coords = get_coordinates(store["address"])
        distance = calculate_distance(user_coords, store_coords)
        if distance < min_distance:
            min_distance = distance
            closest = store
            closest["distance_km"] = round(distance, 2)
    
    return closest
