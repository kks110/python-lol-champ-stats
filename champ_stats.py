
#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to export the data to a CSV
import csv


def get_data_url():
    data_url = "https://ddragon.leagueoflegends.com/realms/euw.json"
    response = requests.get(data_url)
    euw_json = response.json()
    data_version = euw_json['n']['champion']
    data_url = "http://ddragon.leagueoflegends.com/cdn/" + data_version + "/data/en_GB/champion.json"
    return data_url


def get_jsons():
    response = get_data_url()
    response = requests.get(response)
    data_json = response.json()
    champ_list = data_json['data'].keys()
    return data_json, champ_list

# Not used, but could be implemented to calculate stats at different levels
def level_math(base, per_level, level):
    level_stat = base + (per_level * level)
    return level_stat


def create_file():
    data_json, champ_list = get_jsons()
    with open('champStats.csv', 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["Name", "HP", "HP Per Level", "MP", "MP Per Level", "Move Speed", "Armor", "Armour Per Level", "Spell Block", "Spell Block Per Level", "Attack Range", "HP Regen", "HP Regen Per Level", "MP Regen", "MP Regen Per Level", "Attack Damage", "Attack Damage Per Level", "Attack Speed", "Attack Speed Per Level"])
        for champ in champ_list:
            name = data_json['data'][champ]['name']
            hp = data_json['data'][champ]['stats']['hp']
            hpperlevel = data_json['data'][champ]['stats']['hpperlevel']
            mp = data_json['data'][champ]['stats']['mp']
            mpperlevel = data_json['data'][champ]['stats']['mpperlevel']
            movespeed = data_json['data'][champ]['stats']['movespeed']
            armor = data_json['data'][champ]['stats']['armor']
            armorperlevel = data_json['data'][champ]['stats']['armorperlevel']
            spellblock = data_json['data'][champ]['stats']['spellblock']
            spellblockperlevel = data_json['data'][champ]['stats']['spellblockperlevel']
            attackrange = data_json['data'][champ]['stats']['attackrange']
            hpregen = data_json['data'][champ]['stats']['hpregen']
            hpregenperlevel = data_json['data'][champ]['stats']['hpregenperlevel']
            mpregen = data_json['data'][champ]['stats']['mpregen']
            mpregenperlevel = data_json['data'][champ]['stats']['mpregenperlevel']
            attackdamage = data_json['data'][champ]['stats']['attackdamage']
            attackdamageperlevel = data_json['data'][champ]['stats']['attackdamageperlevel']
            attackspeed = data_json['data'][champ]['stats']['attackspeed']
            attackspeedperlevel = data_json['data'][champ]['stats']['attackspeedperlevel']
            writer.writerow([name, hp, hpperlevel, mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange, hpregen, hpregenperlevel, mpregen, mpregenperlevel, attackdamage, attackdamageperlevel, attackspeed, attackspeedperlevel])


def main():
    create_file()


#This starts my program!
if __name__ == "__main__":
    main()
