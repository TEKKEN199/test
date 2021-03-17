import requests, threading, time

def x():
    mas = "HACKER"
    url = "https://discord.com/api/v8/channels/821674874497663016/messages"
    headers = {"authorization": "ODIxNjczNjYyMTkzMDc0MjQ3.YFHJ1w.bCHXCPLG7cBXQxaDIn3xkB0Glf4"}
    data = {"content": "hacker"}
    x = requests.post(url, headers=headers, data=data)
    time.sleep(0.4)
    if ('"message": "401') in x.text:
        none = None
    else:
        print("SENT >> " + mas)
for t in range(2):
    T1 = threading.Thread(target=x).start()
