import spotify 
import analyzer 
from time import sleep 
import ledControll

client_id = '4e7c4e2792ef4fc0963d4418ead81671' 
client_secret = '92547db376f84c0b986ecfdc3812efd7' 
redirect_uri = 'https://google.com/' 

refresh_token = 'AQC0zl0IfQ4aNWzvym6OUkHGxHjhIpYG2gCjeNtcsgATegYUROREBqNcbVIViKBUBLiTSCho9F99sQzgdGBXrytVUYkS9nVcgOOj2XZkjQ0N8TENLJfddK67GR-S54BaSHg'
code = 'AQBaVBnNJE5WkWPKj06o0vbCCBmd-73z2adcYLvY0uZgvdnJJ4av6BojPq2fIa7oiQOqkvxFXiLGcp-eDBzrZlTMjUgthbBbgptCLOf8NXoV_9hESPsARdGY7VSUtowKcLKnp67hzgcidsJQKZ2Em__PpHmaAGo' 

token = spotify.getToken(client_id, client_secret, refresh_token)

brightness = 1

try: 
	currentSong = "1"
	oldSong = "1"	

	while True:
		while currentSong == oldSong:
			song = spotify.getCurrentTrack(token)
			currentSong = str(song['item']['id'])
			sleep(1)
		print()
		oldSong = currentSong 

		coverUrl = song['item']['album']['images'][1]['url']
		palette = analyzer.getColor(coverUrl)

		r = palette[0][0] 
		g = palette[0][1] 
		b = palette[0][2]
		ledControll.changeColor(0, int(r * brightness), int(g * brightness), int(b * brightness));
		print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mColor!\033[0m')

		r = palette[1][0] 
		g = palette[1][1]
		b = palette[1][2]
		ledControll.changeColor(1, int(r * brightness), int(g * brightness), int(b * brightness));

		print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mColor!\033[0m') 

		r = palette[2][0] 
		g = palette[2][1]
		b = palette[2][2]
		ledControll.changeColor(2, int(r * brightness), int(g * brightness), int(b * brightness));

		print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mColor!\033[0m')
except KeyboardInterrupt: 
	print("End")
