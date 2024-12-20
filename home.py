import requests 
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMDFjMWQwZjc4MjA0MTU2OWRlODk5OTAyOTM0ZTZlMCIsImlhdCI6MTczNDM3NTI4MCwiZXhwIjoyMDQ5NzM1MjgwfQ.86FhBRhsaeeUf6cu4-hK7Z9NZm9YxWvUGHoFEUH0Wwc"

def turnon(entity, r, g, b):
    url = "http://192.168.178.57:8123/api/services/light/turn_on"

    headers = {
		"Authorization": "Bearer " + token,
        "content-type": "application/json"
    }
    payload = {
        "entity_id": entity, 
        "brightness": 255, 
        "rgb_color": [r, g, b]
    }
    res = requests.post(url, json=payload, headers=headers)

def checkSpotify():
    url = "http://192.168.178.57:8123/api/states/switch.spotify"
    headers = {
		"Authorization": "Bearer " + token,
        "content-type": "application/json"
    }
    res = requests.get(url, headers=headers)
    state = json.loads(res.text)
    return 1 if state['state'] == "on" else 0