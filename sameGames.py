import requests

EleGanTor = "76561198070755550"
Destiny = "76561198036465436"
Schnipsgie = "76561198097976977"
Infuson = "76561198121409124"
ZeBi = "76561198078633456"
Gemmling = "76561198097679779"
Tim = "76561198236423500"
HunterStorm = "76561198032384256"
McBerti = "76561198029291865"
OtherMCBerti = "76561197981604128"
tired_ = "76561198164281879"
genesis = "76561198350433664"
Kim = "76561198191283141"
ValleyofFeed = "76561198069573710"
Apo = "76561198208715317"

key = "318D204969260A9465D28DDD06A29D40"

ids = [EleGanTor, Destiny]

allGames = {}
gameNames = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/").json()["applist"]["apps"]
giveName = {}

for i in range(len(gameNames)):
    giveName[gameNames[i]["appid"]]=gameNames[i]["name"]

for i in range(len(ids)):
    response = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + key + "&steamid=" + ids[i])
    if response.status_code == 200:
        json_response = response.json()["response"]["games"]
        for j in range(len(response.json()["response"]["games"])):
            if i == 0:
                allGames[json_response[j]["appid"]] = 1
            else:
                try:
                    allGames[json_response[j]["appid"]]+=1
                except:
                    allGames[json_response[j]["appid"]] = 1

for i, j in allGames.items():
    if j == len(ids):
        try:
            print(giveName[i])
        except:
            pass

