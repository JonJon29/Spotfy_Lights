import spotify 
import analyzer 
from time import sleep 
import ledControll
import home

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
			while(home.checkSpotify() == 0):
				sleep(1)
			song = spotify.getCurrentTrack(token)
			while(song == {}):
				song = spotify.getCurrentTrack(token)
				sleep(1)
			currentSong = str(song['item']['id'])
			sleep(1)
		print()
		oldSong = currentSong 

		coverUrl = song['item']['album']['images'][1]['url']
		palette = analyzer.extract_dominant_colors(coverUrl, 10, 60, 100)

		lights = ["light.lampe1", "light.lampe2", "light.lampe3", "light.lampe4"]
		segment = 0;
		for p in palette:
			r = int(p[0]) 
			g = int(p[1]) 
			b = int(p[2])
			#ledControll.changeColor(segment, int(r * brightness), int(g * brightness), int(b * brightness));
			home.turnon(lights[segment], r, g, b)
			segment += 1
			print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mColor!\033[0m')
			if(segment >= 4): break;

except KeyboardInterrupt: 
	print("End")
