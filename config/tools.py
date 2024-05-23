import json
from selenium.webdriver.common.by import By

_config = {
    'headless' : False,
    'search_for' : 'dying light',
    'steam_url': "https://store.steampowered.com/",
    'epic games_url': "https://store.epicgames.com/en-US/",
    'container': [{
        'store': 'steam',
        'name': 'game_editions',
        'selector': "//div[@id='game_area_purchase']/div[contains(@class,'purchase')]",
        'match': 'all',
        'type': 'raw',
        'method': By.XPATH
    },
    {
        'store': 'epic games',
        'name': 'game_cards',
        'selector': '//div[@class="css-4xp4iq egs-related-offer-card"]',
        'match': 'all',
        'type': 'raw',
        'method': By.XPATH
    }
],
    'item': [
        {
            'store': 'steam',
            'name': 'title',
            'selector': "appHubAppName",
            'match': 'first',
            'type': 'text',
            'method': By.ID,
            'container': None
        },
        {
            'store': 'steam',
            'name': 'popular_tags',
            'selector': "//div[contains(@class,'popular_tags')]/a",
            'match': 'all',
            'type': 'text',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'steam',
            'name': 'game_img',
            'selector': "//div[@id='gameHeaderImageCtn']/img",
            'match': 'first',
            'type': 'raw',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'steam',
            'name': 'release_date',
            'selector': "date",
            'match': 'first',
            'type': 'text',
            'method': By.CLASS_NAME,
            'container': None
        },
        {
            'store': 'steam',
            'name': 'game_title',
            'selector': "h1",
            'match': 'first',
            'type': 'text',
            'method': By.TAG_NAME,
            'container': 'game_editions'
        },
        {
            'store': 'steam',
            'name': 'game_price',
            'selector': ".//div[contains(@class,'price')]",
            'match': 'first',
            'type': 'text',
            'method': By.XPATH,
            'container': 'game_editions'
        },
        {
            'store': 'steam',
            'name': 'd_game_price',
            'selector': ".//div[contains(@class,'price')]",
            'match': 'first',
            'type': 'text',
            'method': By.XPATH,
            'container': 'game_editions'
        },
        {
            'store': 'epic games',
            'name': 'title',
            'selector': "//h1/span",
            'match': 'first',
            'type': 'text',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'epic games',
            'name': 'popular_tags',
            'selector': '//div[@data-testid="about-metadata-layout-column"][1]//li',
            'match': 'all',
            'type': 'text',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'epic games',
            'name': 'game_img',
            'selector': "//div[contains(data-testid,picture)]/img",
            'match': 'first',
            'type': 'raw',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'epic games',
            'name': 'release_date',
            'selector': "//time[1]",
            'match': 'first',
            'type': 'text',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'epic games',
            'name': 'game_title',
            'selector': '//div[@data-testid="related-offer-tag-title"]//h3',
            'match': 'all',
            'type': 'text',
            'method': By.XPATH,
            'container': None
        },
        {
            'store': 'epic games',
            'name': 'game_price',
            'selector': ".//span[@class='css-1vkmhw5']",
            'match': 'first',
            'type': 'text',
            'method': By.XPATH,
            'container': 'game_cards'
        },
        {
            'store': 'epic games',
            'name': 'd_game_price',
            'selector': ".//div[@class='css-4jky3p']",
            'match': 'first',
            'type': 'text',
            'method': By.XPATH,
            'container': 'game_cards'
        }
    ]
}


def get_config(load_from_file=False):
    if load_from_file:
        with open('config.json', 'r') as f:
            return json.load(f)
    return _config


def generate_config():
    with open('config', 'w') as f:
        json.dump(_config, f, indent=4)


if __name__ == '__main__':
    generate_config()
