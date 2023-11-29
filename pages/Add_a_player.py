import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AddAPlayer(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*/div[7]/div/div/input"
    club_xpath = "//*[@name='club']"
    level_xpath = "//*[@name='level']"
    main_position_xpath = "//*[@name='mainPosition']"
    second_position_xpath = "//*[@name='secondPosition']"
    achievements_xpath = "//*[@name='achievements']"
    add_language_xpath = "//*/div[2]/div/div[15]/button"
    languages_xpath = "//*/div[15]/div/div/div/input"
    laczy_nas_pilka_xpath = "//*[@name='webLaczy']"
    dziewiecdziesiat_minut_xpath = "//*[@name='web90']"
    facebook_xpath = "//*[@name='webFB']"
    add_link_to_youtube_xpath = "//*/div/div[19]/button"
    link_to_youtube_xpath = "//*/div/div[19]/div/div/div/input"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[1]"
    left_leg_xpath = "//li[2]"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    lublin_xpath = "//*[@data-value='lubelskie']"

    expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    expected_assert_title = "Edit player John Smith"

    def title_of_page(self):
        self.wait_for_element_to_be_visible(self.main_page_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

    def type_in_email(self, email):
        self.wait_for_element_to_be_visible(self.email_xpath)
        self.field_send_keys(self.email_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_club(self, club):
        self.field_send_keys(self.club_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_xpath, second_position)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_xpath, achievements)

    def click_add_language_button(self):
        self.click_on_the_element(self.add_language_xpath)
    def type_in_languages(self, languages):
        self.field_send_keys(self.languages_xpath, languages)
    def type_in_laczy_nas_pilka(self, laczy_nas_pilka):
        self.field_send_keys(self.laczy_nas_pilka_xpath, laczy_nas_pilka)

    def type_in_dziewiecdziesiat_minut(self, dziewiecdziesiat_minut):
        self.field_send_keys(self.dziewiecdziesiat_minut_xpath, dziewiecdziesiat_minut)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_xpath, facebook)

    def click_add_link_to_youtube_button(self):
        self.click_on_the_element(self.add_link_to_youtube_xpath)

    def type_in_link_to_youtube(self, link_to_youtube):
        self.field_send_keys(self.link_to_youtube_xpath, link_to_youtube)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_xpath)

    def click_clear_button(self):
        self.click_on_the_element(self.clear_xpath)

    def select_leg(self, leg):
        self.wait_for_element_to_be_clickable(self.leg_dropdown_xpath)
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == "right":
            self.wait_for_element_to_be_clickable(self.right_leg_xpath)
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.left_leg_xpath)
            self.click_on_the_element(self.left_leg_xpath)

    def select_district(self, district):
        self.wait_for_element_to_be_clickable(self.district_dropdown_xpath)
        self.click_on_the_element(self.district_dropdown_xpath)
        if district == "Lublin":
            self.click_on_the_element(self.lublin_xpath)
        elif district == "Lublin":
            self.click_on_the_element(self.lublin_xpath)
        else:
            self.click_on_the_element(self.lublin_xpath)

    def title_of_edit_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_xpath)
        time.sleep(3)
        edit_page_url = self.driver.current_url
        assert self.get_page_title(edit_page_url) == self.expected_assert_title