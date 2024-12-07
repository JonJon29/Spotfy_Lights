import base64 

def encode(client_id, client_secret):
	client_string = str(client_id) + ":" + str(client_secret)
	client_bytes = client_string.encode('ascii')
	encoded = base64.b64encode(client_bytes) 
	return encoded
