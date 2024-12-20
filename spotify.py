import requests 
import json
from datetime import datetime, timezone
import base64 

def encode(client_id, client_secret):
	client_string = str(client_id) + ":" + str(client_secret)
	client_bytes = client_string.encode('ascii')
	encoded = base64.b64encode(client_bytes) 
	return encoded

class Spotify:
	def __init__(self, refreshToken, clientId, clientSecret):
		self.refreshToken = refreshToken 
		self.clientId = clientId 
		self.clientSecret = clientSecret
		self.expireTime = 0 
		self.token = 0

	def getTime(self): 
		return int(datetime.now(timezone.utc).timestamp())
	
	def getToken(self):
		url = 'https://accounts.spotify.com/api/token'
		body = {
			'grant_type' : 'refresh_token',
			'refresh_token' : self.refreshToken,
		}
		headers = {
			'Authorization': "Basic " + encode(self.clientId, self.clientSecret).decode('utf-8') ,
			'Content-Type': 'application/x-www-form-urlencoded'}
		res = requests.post(url, data=body, headers=headers)
		dict = json.loads(res.text)

		return dict['access_token']
	
	def checkToken(self):
		now = self.getTime()
		if(now >= self.expireTime):
			self.token = self.getToken() 
			self.expireTime = now 

	def authorize(self, redirect_uri, code):
		url ='https://accounts.spotify.com/api/token'
		form = {
			'code': code, 
			'redirect_uri': redirect_uri, 
			'grant_type': 'authorization_code'
			}
		headers = {
			'content-type': 'application/x-www-form-urlencoded', 
			'Authorization': "Basic " + encode(self.clientId, self.clientSecret).decode('utf-8') 
			}
		x = requests.post(url, data = form, headers = headers)

		dict = json.loads(x.txt)

		return dict['refresh_token']

	def getCurrentTrack(self):
		self.checkToken()
		url = 'https://api.spotify.com/v1/me/player/currently-playing'
		headers = {
			'Authorization' : 'Bearer ' + str(self.token)
			}
		res = requests.get(url, headers=headers)
		if(res.text):
			song = json.loads(res.text)
		else: 
			song = -1
		return song