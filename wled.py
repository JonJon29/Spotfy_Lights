import requests 

ip = "192.168.178.66"

def switch(state):
    url = "http://" + ip + "/win&T=" + str(state)
    x = requests.get(url=url)

def changeColor(segment, r, g, b):
    url = "http://" + ip + "/win&SS=" + str(segment) + "&R=" + str(r) + "&G=" + str(g) + "&B=" + str(b)
    try:
        r = requests.get(url, timeout=10) # 10 seconds
    except requests.exceptions.Timeout:
        print("Timed out")