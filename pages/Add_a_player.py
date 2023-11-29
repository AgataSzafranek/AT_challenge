import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

#TASK 3 Subtask 4 - Add a player
class AddAPlayer(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    add_player = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*/div[7]/div/div/input"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "// *[ @ id = 'menu-leg'] / div[3] / ul / li[1]"
    left_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    club_xpath = "//*[@name='club']"
    level_xpath = "//*[@name='level']"
    main_position_xpath = "//*[@name='mainPosition']"
    second_position_xpath = "//*[@name='secondPosition']"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    achievements_xpath = "//*[@name='achievements']"
    add_language_xpath = "//*/div[2]/div/div[15]/button"
    languages_xpath = "//*/div[15]/div/div/div/input"
    laczy_nas_pilka_xpath = "//*[@name='webLaczy']"
    dziewiecdziesiat_minut_xpath = "//*[@name='web90']"
    facebook_xpath = "//*[@name='webFB']"
    add_link_to_youtube_xpath = "//*/div/div[19]/button"
    link_to_youtube_xpath = "//*/div/div[19]/div/div/div/input"
    clear_xpath = "//*[text()='Clear']"
    submit_xpath = "//*[@type='submit']"
    expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
