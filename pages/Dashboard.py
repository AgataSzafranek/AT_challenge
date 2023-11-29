import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class Dashboard(BasePage):
    pass
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    dev_team_contact_xpath = "//*[text()='Dev team contact']"
    add_player_xpath = "//*[text()='Add player']"
    last_created_player_xpath = "//*/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//*/div/a[2]/button/span[1]"
    last_created_match_xpath = "//*/div/a[3]/button/span[1]"
    last_updated_match_xpath = "//*/div/a[4]/button/span[1]"
    last_updated_report_xpath = "//*/div/a[5]/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"

    def title_of_page(self):
        self.wait_for_element_to_be_visible(self.main_page_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_a_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_player_xpath)
        self.click_on_the_element(self.add_player_xpath)

    def click_sign_out_button(self):
        self.wait_for_element_to_be_clickable(self.sign_out_xpath)
        self.click_on_the_element(self.sign_out_xpath)

    def click_polski_button(self):
        self.wait_for_element_to_be_clickable(self.polski_xpath)
        self.click_on_the_element(self.polski_xpath)

    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_xpath)
        self.click_on_the_element(self.players_xpath)

    def click_last_created_player(self):
        self.wait_for_element_to_be_clickable(self.last_created_player_xpath)
        self.click_on_the_element(self.last_created_player_xpath)