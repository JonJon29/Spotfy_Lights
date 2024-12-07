import spotify 

client_id = '4e7c4e2792ef4fc0963d4418ead81671' 
client_secret = '92547db376f84c0b986ecfdc3812efd7' 
redirect_uri = 'https://google.com/' 

refresh_token = 'AQC0zl0IfQ4aNWzvym6OUkHGxHjhIpYG2gCjeNtcsgATegYUROREBqNcbVIViKBUBLiTSCho9F99sQzgdGBXrytVUYkS9nVcgOOj2XZkjQ0N8TENLJfddK67GR-S54BaSHg'
code = 'AQBaVBnNJE5WkWPKj06o0vbCCBmd-73z2adcYLvY0uZgvdnJJ4av6BojPq2fIa7oiQOqkvxFXiLGcp-eDBzrZlTMjUgthbBbgptCLOf8NXoV_9hESPsARdGY7VSUtowKcLKnp67hzgcidsJQKZ2Em__PpHmaAGo' 

token = spotify.getToken(client_id, client_secret, refresh_token)

song = spotify.getCurrentTrack(token)

print(song)
