# Used to get the URL
import requests
# Used to export the data to a CSV
import csv


def data_version():
    ddragon = "https://ddragon.leagueoflegends.com/realms/euw.json"
    euw_json = requests.get(ddragon).json()
    return euw_json['n']['champion']


def build_data_url():
    return "http://ddragon.leagueoflegends.com/cdn/" + data_version() + "/data/en_GB/champion.json"


def get_jsons():
    data_url = build_data_url()
    data_json = requests.get(data_url).json()
    champ_list = data_json['data'].keys()
    return data_json, champ_list


# Not used, but could be implemented to calculate stats at different levels
def level_math(base, per_level, level):
    level_stat = base + (per_level * level)
    return level_stat


def row_headings():
    return [
        "Name",
        "HP",
        "HP Per Level",
        "MP",
        "MP Per Level",
        "Move Speed",
        "Armor",
        "Armour Per Level",
        "Spell Block",
        "Spell Block Per Level",
        "Attack Range",
        "HP Regen",
        "HP Regen Per Level",
        "MP Regen",
        "MP Regen Per Level",
        "Attack Damage",
        "Attack Damage Per Level",
        "Attack Speed",
        "Attack Speed Per Level"
    ]


def create_file():
    data_json, champ_list = get_jsons()
    file_name = 'patch_' + data_version() + '_champStats.csv'
    with open(file_name, 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row_headings())
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


if __name__ == "__main__":
    main()
