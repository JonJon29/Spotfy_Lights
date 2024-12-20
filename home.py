import requests 
import json

class Home: 
    def __init__(self, token: str, ip: str):
        self.token = token 
        self.ip = ip 

    def changeColor(self, entity, r, g, b):
        url = self.ip + "/api/services/light/turn_on"

        headers = {
            "Authorization": "Bearer " + self.token,
            "content-type": "application/json"
        }
        payload = {
            "entity_id": entity, 
            "brightness": 255, 
            "rgb_color": [r, g, b]
        }
        res = requests.post(url, json=payload, headers=headers)
    
    def checkSwitch(self, entity): 
        url = self.ip + "/api/states/" + entity
        headers = {
            "Authorization": "Bearer " + self.token,
            "content-type": "application/json"
        }
        res = requests.get(url, headers=headers)
        state = json.loads(res.text)
        return 1 if state['state'] == "on" else 0       