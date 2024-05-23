from config.tools import get_config
from utils.store import generate_df
from utils.Process import pad_dict_lists
from utils.parse import parse_game_data
import pandas as pd
from tabulate import tabulate
import psutil

if __name__ == '__main__':

    config = get_config()
    data = parse_game_data(config, ['steam', 'epic games'], config.get('search_for'))
    try:
        for process in (process for process in psutil.process_iter() if process.name() == "chrome.exe"):
            process.kill()
    except:
        pass

    steam_data = pad_dict_lists(data['steam'])
    epic_games_data = pad_dict_lists(data['epic games'])
    expanded_steam_df = generate_df(steam_data)
    expanded_epic_df = generate_df(epic_games_data)
    combined_df = pd.concat([expanded_steam_df, expanded_epic_df], axis=0)
    print(tabulate(combined_df,headers='keys'))
    combined_df.to_csv(config.get('search_for'),index=False)





