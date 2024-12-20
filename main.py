from spotify import Spotify 
import analyzer 
from time import sleep 
import wled
from home import Home
from dotenv import load_dotenv
import os 

load_dotenv() 

clientId = os.getenv('CLIENT_ID')
clientSecret = os.getenv('CLIENT_SECRET')
redirectUri = os.getenv('REDIRECT_URI') 
refreshToken = os.getenv('REFRESH_TOKEN') 
code = os.getenv('SPOTIFY_CODE') 
homeToken = os.getenv('HOME_TOKEN') 


s = Spotify(refreshToken, clientId, clientSecret)

home = Home(homeToken, "http://192.168.178.57:8123")

brightness = 1

try: 
	currentSong = "1"
	oldSong = "1"	

	while True:
		while currentSong == oldSong:
			while(home.checkSwitch("switch.spotify") == 0):
				sleep(1)
			song = s.getCurrentTrack()
			while(song == -1):
				song = s.getCurrentTrack()
				sleep(1)
			currentSong = str(song['id'])
			sleep(1)
		print()
		oldSong = currentSong 

		coverUrl = song['album']['images'][1]['url']
		palette = analyzer.extract_dominant_colors(coverUrl, 10, 60, 100)

		lights = ["light.lampe1", "light.lampe2", "light.lampe3", "light.lampe4"]
		segment = 0;
		for p in palette:
			r = int(p[0]) 
			g = int(p[1]) 
			b = int(p[2])
			#ledControll.changeColor(segment, int(r * brightness), int(g * brightness), int(b * brightness));
			home.changeColor(lights[segment], r, g, b)
			segment += 1
			print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mColor!\033[0m')
			if(segment >= 4): break;

except KeyboardInterrupt: 
	print("End")
