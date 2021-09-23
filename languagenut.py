import requests

print("  _                                              _   _       _   ")
print(" | |                                            | \ | |     | |  ")
print(" | |     __ _ _ __   __ _ _   _  __ _  __ _  ___|  \| |_   _| |_ ")
print(" | |    / _` | '_ \ / _` | | | |/ _` |/ _` |/ _ \ . ` | | | | __|")
print(" | |___| (_| | | | | (_| | |_| | (_| | (_| |  __/ |\  | |_| | |_ ")
print(" |______\__,_|_| |_|\__, |\__,_|\__,_|\__, |\___|_| \_|\__,_|\__|")
print("                     __/ |             __/ |                     ")
print("                    |___/             |___/                      ")
print("      /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$")
print("     | $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/")
print("     | $$  | $$| $$  \ $$| $$  \__/| $$ /$$/ ")
print("     | $$$$$$$$| $$$$$$$$| $$      | $$$$$/  ")
print("     | $$__  $$| $$__  $$| $$      | $$  $$  ")
print("     | $$  | $$| $$  | $$| $$    $$| $$\  $$ ")
print("     | $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$")
print("     |__/  |__/|__/  |__/ \______/ |__/  \__/")
print(" ")
print(" ")
instructions = input("Would you like instructions on how to use the hack? y/n: ")
print(" ")
print(" ")
if instructions == "y":
    print("1. Enter your username and password to languagenut.")
    print(" ")
    print("2. Next enter a number between 1000 and 40000, (this determines what lesson you will get points from. If you have already completed the lesson too many times you will no longer gain points from it, so pick a number different to one you have used before. In some cases the number will not correspond to a lesson, in which case just try another number. If it is your first time I recommend the number 12000.")
    print(" ")
    print("3. Enter how many points you would like to earn.")
    print(" ")
    print("4. Wait for hack to complete.")
    print(" ")
    print(" ")


username = input("Enter languagenut username: ")
password = input("Enter languagenut password: ")
score=0


url = 'https://api.languagenut.com/loginController/attemptlogin?cacheBreaker=1621610672902'

body = 'username='+ str(username) +'&pass='+ str(password) +'&languagenutTimeMarker=1621610672902&lastLanguagenutTimeMarker=1621610672902&apiVersion=8'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 
        'Accept': 'text/plain, */*; q=0.01', 
        'Accept-Language': 'en-GB,en;q=0.5', 
        'Accept-Encoding': 'gzip, deflate', 
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
        'Content-Length': '122', 
        'Origin': 'https://www.languagenut.com', 
        'Referer': 'https://www.languagenut.com/', 
        'Te': 'trailers', 
        'Connection': 'close'    
}   

x = requests.post(url, data = body, headers = headers)
jsonResponse = x.json()

token = jsonResponse['newToken']

number = input("Enter what number to start at: ")
number = int(number)
points = input("How many points would you like? ")
print(" ")
print(" ")

url = 'https://api.languagenut.com:443/gameDataController/addGameScore?cacheBreaker=1621543527060'

body = 'moduleUid=' + str(number) + '&gameUid=10&gameType=reading&isTest=true&toietf=es&fromietf=en-GB&score=3800&correctVocabs=26097%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096&incorrectVocabs=&isSentence=false&isVerb=false&grammarCatalogUid=12116&isGrammar=false&isExam=false&timeStamp=39250&vocabNumber=19&languagenutTimeMarker=1621543527060&lastLanguagenutTimeMarker=1621543527060&apiVersion=8&token=' + str(token)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', 
        'Accept': 'text/plain, */*; q=0.01', 
        'Accept-Language': 'en-GB,en;q=0.5', 
        'Accept-Encoding': 'gzip, deflate', 
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
        'Content-Length': '794', 
        'Origin': 'https://www.languagenut.com', 
        'Referer': 'https://www.languagenut.com/', 
        'Te': 'trailers', 
        'Connection': 'close'    
}

run = True

while True:
    for i in range(7):
        if int(score) > int(points):
            run = False
            break
        x = requests.post(url, data = body, headers = headers)
        if 'Fatal' in x.text:
            print("Invalid Number: " + str(number) + ", try entering another number between 1000 and 40000")
            run = False
            break
        if 'Error' in x.text:
            print("Invalid Token or login details")
            run = False
            break
        score+=3800
        percentage = int(score)/int(points)*100
        if percentage > 100:
            percentage = 100
        percentage = round(percentage, 2)
        print(str(score) + "/" + str(points) + " points  - " + str(percentage) + "%", end="\r")
    if run == False:
        break    
    number+=1
    body = 'moduleUid=' + str(number) + '&gameUid=10&gameType=reading&isTest=true&toietf=es&fromietf=en-GB&score=3800&correctVocabs=26097%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096&incorrectVocabs=&isSentence=false&isVerb=false&grammarCatalogUid=12116&isGrammar=false&isExam=false&timeStamp=39250&vocabNumber=19&languagenutTimeMarker=1621543527060&lastLanguagenutTimeMarker=1621543527060&apiVersion=8&token=' + str(token)

print("")
print("")
print("Finished hack")
print("You have earned " + str(score) + " points!")
