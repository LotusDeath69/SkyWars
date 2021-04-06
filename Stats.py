import requests
api = 'INSERT_KEY_HERE'
username = 'ThatBananaKing'


def uuid(ign):
    data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
    return data['id']


def formatPercentage(x):
    return "{:.0%}".format(x)


def stats(ign, key):
    data = requests.get(f'https://api.hypixel.net/player?key={key}&uuid={uuid(ign)}').json()
    wins = data['player']['stats']['SkyWars']['wins']
    losses = data['player']['stats']['SkyWars']['losses']
    win_rate = round(wins / losses, 2)

    kills = data['player']['stats']['SkyWars']['kills']
    deaths = data['player']['stats']['SkyWars']['deaths']
    kill_death_ratio = round(kills / deaths, 2)

    current_winstreak = data['player']['stats']['SkyWars']['win_streak']
    games_played = data['player']['stats']['SkyWars']['games']

    '#Experiences: converting to skywar level using muchnameless wrapper'
    # experience = data['player']['stats']['SkyWars']['skywars_experience']

    return f"Levels: {'insert wrapper here'}\nWins: {wins}\nLosses: {losses}\nWin Rate: {formatPercentage(win_rate)}" \
           f"\n\nKills: {kills}\nDeaths: {deaths}\nK/D Ratio: {kill_death_ratio}\nGames Played: " \
           f"{games_played}\nCurrent Winstreak: {current_winstreak}" \



print(stats(username, api))
