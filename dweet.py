import dweepy

def send_dweet(thing, value):
    dweepy.dweet_for(thing, {"text": value})
    return "sent text=" + value

def get_dweet(thing):
    dweet = dweepy.get_latest_dweet_for(thing)
    print(dweet)
    return dweet

def listen_dweet(thing):
    for dweet in dweepy.listen_for_dweets_from(thing):
        print(dweet['content']['text'])
        return dweet
