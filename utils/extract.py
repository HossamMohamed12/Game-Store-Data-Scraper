from config.tools import get_config
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


def search_for_game(game_title,store):
    config = get_config()
    if store == 'steam':
        web = config.get('steam_url')
        driver = uc.Chrome(headless=config.get('headless'),use_subprocess=False, no_sandbox=False)
        driver.get(web)
        driver.maximize_window()
        # searching for a game
        search_box = driver.find_element(By.ID, 'store_nav_search_term')
        search_box.send_keys(game_title)
        time.sleep(2)
        search_btn = driver.find_element(By.XPATH, '//div[@id="search_suggestion_contents"]/a[1]')
        search_btn.click()
        time.sleep(1)
        if 'agecheck' in driver.current_url:
            dropdown = Select(driver.find_element(By.ID, 'ageYear'))
            dropdown.select_by_visible_text('2000')
            view_page = driver.find_element(By.ID, 'view_product_page_btn')
            view_page.click()
            time.sleep(2)
            return driver
        else:
            return driver
    elif store == 'epic games':
        web = config.get('epic games_url')
        driver = uc.Chrome(headless=False, use_subprocess=False)
        driver.get(web)
        driver.maximize_window()
        # searching for a game
        search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search store"]')
        search_box.send_keys(game_title)
        time.sleep(2)
        game_url = driver.find_element(By.XPATH, "//div[contains(id,tippy)]//a[1]").get_attribute('href')
        driver.get(game_url)
        time.sleep(1)
        try:
            age_check = driver.find_element(By.ID, 'btn_age_continue')
        except:
            pass

        if age_check:
            month_list = driver.find_element(By.ID, 'month_toggle')
            month_list.click()
            month_btn = driver.find_element(By.XPATH, '//ul[@id="month_menu"]/li[10]')
            month_btn.click()
            day_list = driver.find_element(By.ID, 'day_toggle')
            day_list.click()
            day_btn = driver.find_element(By.XPATH, '//ul[@id="day_menu"]/li[10]')
            day_btn.click()
            year_list = driver.find_element(By.ID, 'year_toggle')
            year_list.click()
            year_btn = driver.find_element(By.XPATH, '//ul[@id="year_menu"]/li[45]')
            year_btn.click()
            view_page = driver.find_element(By.ID, 'btn_age_continue')
            view_page.click()
            time.sleep(4)
            return driver
        else:
            time.sleep(4)
            return driver

