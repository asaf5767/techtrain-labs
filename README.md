# Store Locator API

A simple Flask API to find the nearest store to a given address.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Server runs on `http://localhost:5000`

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/stores` | GET | List all stores |
| `/nearest?address=...` | GET | Find nearest store to address |

## Environment Variables

- `GOOGLE_MAPS_API_KEY` - Required for geocoding (set before running)

## Example

```bash
curl "http://localhost:5000/nearest?address=123+Main+St+New+York"
```
