import os
import unittest
import time

from selenium import webdriver
from pages.add_a_player import AddaPlayer
from pages.Dashboard import Dashboard
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddaPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_Add_a_Player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)
        dashboard_page.click_add_a_player_button()
        player = AddaPlayer(self.driver)
        player.type_in_email('john@test.com')
        player.type_in_name('John')
        player.type_in_surname('Smith')
        player.type_in_phone('99')
        player.type_in_weight('65')
        player.type_in_height('168')
        player.type_in_age('01.01.1999')
        player.click_on_the_leg()
        player.click_on_the_right_leg()
        player.type_in_club('FC Barca')
        player.type_in_level('5')
        player.type_in_main_position('goalkeeper')
        player.type_in_second_position('striker')
        player.click_on_the_district()
        player.click_on_the_lower_silesia()
        player.type_in_achievements('5')
        player.type_in_laczy_nas_pilka('www.laczynaspilka.pl')
        player.type_in_minut('90minut')
        player.type_in_facebook('John/facebook')
        player.click_on_the_submit_button()
        player.click_on_the_main_page_button()
        time.sleep(5)