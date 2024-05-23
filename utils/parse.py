import time

from utils.extract import search_for_game
from utils.Process import format_and_transform_steam, format_and_transform_epic
from config.tools import get_config
from selenium.webdriver.common.by import By


def parse_raw_attributes(driver, config, store):
    parsed = {}
    parsed['url'] = config.get(f'{store}_url')
    for i in config.get('item'):
        store_name = i.get('store')
        if store_name == store:
            name = i.get('name')
            selector = i.get('selector')
            match = i.get('match')
            type_ = i.get('type')
            method = i.get('method')
            container = i.get('container')

            if container:
                my_container = next((item for item in config.get('container') if item['name'] == container), None)
                my_container = driver.find_elements(my_container['method'], my_container['selector'])
                l = []
                for c in my_container:
                    if match == 'all':
                        try:
                            matched = c.find_elements(method, selector)
                            if not matched:
                                l.append('_')
                            elif type_ == 'text':
                                l.append([match.text for match in matched if match.text])
                            elif type_ == 'raw':
                                l.append(matched)
                        except:
                            l.append('_')

                    elif match == 'first':
                        try:
                            matched = c.find_element(method, selector)
                            if not matched:
                                l.append('_')
                            elif type_ == 'text':
                                l.append(matched.text)
                            elif type_ == 'raw':
                                l.append(matched)
                        except:
                            l.append('_')
                parsed[name] = l
            else:
                if match == 'all':
                    try:
                        matched = driver.find_elements(method, selector)
                        if type_ == 'text':
                            parsed[name] = [match.text for match in matched if match.text]
                        elif type_ == 'raw':
                            parsed[name] = matched

                    except:
                        parsed[name] = 'error'

                elif match == 'first':
                    try:
                        matched = driver.find_element(method, selector)
                        if type_ == 'text':
                            parsed[name] = matched.text
                        elif type_ == 'raw':
                            parsed[name] = matched
                    except:
                        parsed[name] = 'error'
    return parsed

def epic_one_edition_game(driver, data:dict):
    if not data['game_title'] and all(p=='_' for p in data['game_price']):
        try:
            prices = driver.find_elements(By.XPATH,"(//span[@class='css-d3i3lr'])[3]")
            d_prices = driver.find_elements(By.XPATH,"(//span[@class='css-119zqif'])[13]")
            data['game_price'] = [price.text for price in prices if price.text]
            data['d_game_price']=[d_price.text for d_price in d_prices if d_price.text]
            data['game_title'] = data['title']
            return data
        except:
            return data
    else :
        return  data
def epic_d_prices(data:dict):
    for p in data['d_game_price']:
        if p != '_':
            i = data['d_game_price'].index(p)
            data['d_game_price'][i], data['game_price'][i] = data['game_price'][i], data['d_game_price'][i]
        elif not p:
            del data['d_game_price']
    return data
def parse_game_data(config, store, game_title):
    data = {}
    for s in store:
        if s == 'steam':
            driver = search_for_game(game_title, s)
            steam_data = parse_raw_attributes(driver, config, s)
            data[s] = format_and_transform_steam(steam_data)
        elif s == 'epic games':
            driver = search_for_game(game_title, s)
            epic_data = parse_raw_attributes(driver, config, s)
            epic_data = epic_d_prices(epic_data)
            epic_data = epic_one_edition_game(driver,epic_data)
            data[s] = format_and_transform_epic(epic_data)
            driver.quit()
    return data

