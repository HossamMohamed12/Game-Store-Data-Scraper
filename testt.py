import pandas as pd
from tabulate import tabulate
#
steam = {'url': 'https://store.steampowered.com/', 'title': 'Dying Light', 'popular_tags': "['Zombies', 'Survival Horror', 'Horror', 'Online Co-Op']", 'game_img': 'https://cdn.akamai.steamstatic.com/steam/apps/239140/header.jpg?t=1715341001', 'release_date': '2015-01-26', 'game_title': [' Dying Light Standard Edition', ' Dying Light Enhanced Edition', ' Dying Light Definitive Edition', ' Dying Light Enhanced Edition + Dying Light 2 Reloaded Edition BUNDLE '], 'game_price': ['from 12.99$ to 1.95$', 'from 19.49$ to 5.84$', 'from 32.49$ to 6.49$', 'from 59.48$ to 22.91$']}
epic = {'url': 'https://store.epicgames.com/en-US/', 'title': 'Dying Light Enhanced Edition', 'popular_tags': "['Action', 'Open World', 'RPG']", 'game_img': 'https://cdn2.epicgames.com/static/fonts/joypixel/1f3a8.svg', 'release_date': '2022-02-28', 'game_title': ['Dying Light: Standard Edition', 'Dying Light Enhanced Edition', 'Dying Light Definitive Edition', 'Dying Light 2 + Brecken + Rais Bundles'], 'game_price': ['$13.39', '$5.99', '$9.99', '$39.99']}

def process_data(data):
    df = pd.DataFrame(data)
    expanded_df = df.explode('game_title').explode('game_price')
    expanded_df['price_from'] = expanded_df['game_price'].str.extract(r'from\s+(\d+\.\d+)').astype(float)
    expanded_df['price_to'] = expanded_df['game_price'].str.extract(r'to\s+(\d+\.\d+)').astype(float)
    expanded_df.drop(columns='game_price', inplace=True)
    return expanded_df
# Process the Steam and Epic data separately
expanded_steam_df = process_data(steam)
expanded_epic_df = process_data(epic)

combined_df = pd.concat([expanded_steam_df, expanded_epic_df], axis=0)


print(tabulate(combined_df))



