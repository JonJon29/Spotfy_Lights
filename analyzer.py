from colorthief import ColorThief
import requests 

def getColor(url):
	f = requests.get(url, allow_redirects=True)
	open('cover.png', 'wb').write(f.content)
	color_thief = ColorThief('./cover.png')
	palette = color_thief.get_palette(color_count=3, quality=1) 
	return palette
