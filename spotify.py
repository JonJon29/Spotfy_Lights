import requests 
import base
import json

def authorize(client_id, client_secret, redirect_uri, code):
	url ='https://accounts.spotify.com/api/token'
	form = {
		'code': code, 
		'redirect_uri': redirect_uri, 
		'grant_type': 'authorization_code'
		}
	headers = {
		'content-type': 'application/x-www-form-urlencoded', 
		'Authorization': "Basic " + base.encode(client_id, client_secret).decode('utf-8') 
		}
	print(headers)	
	x = requests.post(url, data = form, headers = headers)

	dict = json.loads(x.txt)

	return dict['refresh_token']

def getToken(client_id, client_secret, refresh_token):
	url = 'https://accounts.spotify.com/api/token'
	body = {
		'grant_type' : 'refresh_token',
		'refresh_token' : refresh_token,
	}
	headers = {
		'Authorization': "Basic " + base.encode(client_id, client_secret).decode('utf-8') ,
		'Content-Type': 'application/x-www-form-urlencoded'}
	res = requests.post(url, data=body, headers=headers)
	dict = json.loads(res.text)
	return dict['access_token']

def getCurrentTrack(token):
	url = 'https://api.spotify.com/v1/me/player/currently-playing'
	headers = {
		'Authorization' : 'Bearer ' + str(token)
		}
	res = requests.get(url, headers=headers)
	if(res.text):
		song = json.loads(res.text)
	else: 
		song = {}
	return song
