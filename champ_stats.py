
#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to export the data to a CSV
import csv


def getDataURL():
    dataURL = "https://ddragon.leagueoflegends.com/realms/euw.json"
    response = requests.get(dataURL)
    euwJson = response.json()
    dataVersion = euwJson['n']['champion']
    # print("Data version is " + dataVersion)
    dataURL = "http://ddragon.leagueoflegends.com/cdn/" + dataVersion + "/data/en_GB/champion.json"
    # print("Data version is " + dataURL)
    return dataURL


def getJsons():
    response = getDataURL()
    response = requests.get(response)
    dataJSON = response.json()
    champList = dataJSON['data'].keys()
    return dataJSON, champList

def levelMath(base, perLevel, level):
    levelStat = base + (perLevel * level)
    return levelStat


def createFile():
    dataJSON, champList = getJsons()
    with open('champStats.csv', 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["Name", "HP", "HP Per Level", "MP", "MP Per Level", "Move Speed", "Armor", "Armour Per Level", "Spell Block", "Spell Block Per Level", "Attack Range", "HP Regen", "HP Regen Per Level", "MP Regen", "MP Regen Per Level", "Attack Damage", "Attack Damage Per Level", "Attack Speed", "Attack Speed Per Level"])
        for champ in champList:
            name = dataJSON['data'][champ]['name']
            hp = dataJSON['data'][champ]['stats']['hp']
            hpperlevel = dataJSON['data'][champ]['stats']['hpperlevel']
            mp = dataJSON['data'][champ]['stats']['mp']
            mpperlevel = dataJSON['data'][champ]['stats']['mpperlevel']
            movespeed = dataJSON['data'][champ]['stats']['movespeed']
            armor = dataJSON['data'][champ]['stats']['armor']
            armorperlevel = dataJSON['data'][champ]['stats']['armorperlevel']
            spellblock = dataJSON['data'][champ]['stats']['spellblock']
            spellblockperlevel = dataJSON['data'][champ]['stats']['spellblockperlevel']
            attackrange = dataJSON['data'][champ]['stats']['attackrange']
            hpregen = dataJSON['data'][champ]['stats']['hpregen']
            hpregenperlevel = dataJSON['data'][champ]['stats']['hpregenperlevel']
            mpregen = dataJSON['data'][champ]['stats']['mpregen']
            mpregenperlevel = dataJSON['data'][champ]['stats']['mpregenperlevel']
            attackdamage = dataJSON['data'][champ]['stats']['attackdamage']
            attackdamageperlevel = dataJSON['data'][champ]['stats']['attackdamageperlevel']
            attackspeedoffset = dataJSON['data'][champ]['stats']['attackspeedoffset']
            attackspeedperlevel = dataJSON['data'][champ]['stats']['attackspeedperlevel']
            writer.writerow([name, hp, hpperlevel, mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange, hpregen, hpregenperlevel, mpregen, mpregenperlevel, attackdamage, attackdamageperlevel, attackspeedoffset, attackspeedperlevel])


def main():
    createFile()


#This starts my program!
if __name__ == "__main__":
    main()
