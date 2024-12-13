from colorthief import ColorThief
import requests 

url = 'https://i.scdn.co/image/ab67616d00001e021a3804c279594ebceecec4a2'
f = requests.get(url, allow_redirects=True)
open('cover.png', 'wb').write(f.content)

color_thief = ColorThief('./cover.png')

palette = color_thief.get_palette(color_count=3, quality=1)

print(palette)

r = palette[0][0] 
g = palette[0][1]
b = palette[0][2]
print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mHello!\033[0m')


r = palette[1][0] 
g = palette[1][1]
b = palette[1][2]
print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mHello!\033[0m')


r = palette[2][0] 
g = palette[2][1]
b = palette[2][2]
print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'mHello!\033[0m')
