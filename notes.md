# Daten 
- client_id = 4e7c4e2792ef4fc0963d4418ead81671 
- client_secret = 92547db376f84c0b986ecfdc3812efd7

# Link zum Autorisieren 
https://accounts.spotify.com/authorize?response_type=code&client_id=4e7c4e2792ef4fc0963d4418ead81671&redirect_uri=https://google.com/ 

## Code 7.12 22:44 
AQAT6Fy3jCwZ3OjafNWBtqwvK__GsYdj4RPJe45WBBwX1wn08sruPN_bju3UF30FxxE8WiK6BU9-N2gxxceuEhgwD6_NmAXPuYHACsVbKKIcRrYA7D0pNPywHhzarYdgOUegu_bVp3TDcKrKGR4vdiwHlMdHmb8

curl -d "grant_type=authorization_code" -d "code=AQAT6Fy3jCwZ3OjafNWBtqwvK__GsYdj4RPJe45WBBwX1wn08sruPN_bju3UF30FxxE8WiK6BU9-N2gxxceuEhgwD6_NmAXPuYHACsVbKKIcRrYA7D0pNPywHhzarYdgOUegu_bVp3TDcKrKGR4vdiwHlMdHmb8" -d "redirect_uri=https://google.com/" -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Basic NGU3YzRlMjc5MmVmNGZjMDk2M2Q0NDE4ZWFkODE2NzE6ZjMxNjRmZmNmNzU3NGI1YzlmZWFhMTA0NWQwZjJlMDk=" -X POST https://accounts.spotify.com/api/token/ --http1.1

NGU3YzRlMjc5MmVmNGZjMDk2M2Q0NDE4ZWFkODE2NzE6OTI1NDdkYjM3NmY4NGMwYjk4NmVjZmRjMzgxMmVmZDc= 

192.168.178.166/win&SS=1&R=100&B=255

# Home Assistant Token 
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMDFjMWQwZjc4MjA0MTU2OWRlODk5OTAyOTM0ZTZlMCIsImlhdCI6MTczNDM3NTI4MCwiZXhwIjoyMDQ5NzM1MjgwfQ.86FhBRhsaeeUf6cu4-hK7Z9NZm9YxWvUGHoFEUH0Wwc

curl -X GET \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMDFjMWQwZjc4MjA0MTU2OWRlODk5OTAyOTM0ZTZlMCIsImlhdCI6MTczNDM3NTI4MCwiZXhwIjoyMDQ5NzM1MjgwfQ.86FhBRhsaeeUf6cu4-hK7Z9NZm9YxWvUGHoFEUH0Wwc" \
  -H "Content-Type: application/json" \
  http://192.168.178.57:8123/api/services


