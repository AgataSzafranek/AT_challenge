import time

from pages.base_page import BasePage



class AddaPlayer(BasePage):
    add_player = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    expected_text_xpath = "//*[text()='Add player']"
    email_field_add_player_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    age_field_xpath = "//*/div[7]/div/div/input"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[1]"
    left_leg_xpath = "//li[2]"
    club_xpath = "//*[@name='club']"
    level_xpath = "//*[@name='level']"
    main_position_xpath = "//*[@name='mainPosition']"
    second_position_xpath = "//*[@name='secondPosition']"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    lower_silesia_xpath = "//*[@id='menu-district']/div[3]/ul/li[1]"
    achievements_xpath = "//*[@name='achievements']"
    laczy_nas_pilka_xpath = "//*[@name='webLaczy']"
    dziewiecdziesiat_minut_xpath = "//*[@name='web90']"
    facebook_xpath = "//*[@name='webFB']"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    player_form_xpath = "//*[contains(@class,'MuiGrid-root')]"
    player_form_url = "https://scouts.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"


    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def type_in_email(self, email):
        time.sleep(5)
        self.field_send_keys(self.email_field_add_player_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def click_on_the_leg(self):
        self.click_on_the_element(self.leg_dropdown_xpath)

    def click_on_the_right_leg(self):
        time.sleep(5)
        self.click_on_the_element(self.right_leg_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.club_xpath, club)



    def type_in_level(self, level):
        self.field_send_keys(self.level_xpath, level)

    def type_in_main_position(self, main):
        self.field_send_keys(self.main_position_xpath, main)

    def type_in_second_position(self, second):
        self.field_send_keys(self.second_position_xpath, second)

    def click_on_the_district(self):
        self.click_on_the_element(self.district_dropdown_xpath)

    def click_on_the_lower_silesia(self):
        time.sleep(5)
        self.click_on_the_element(self.lower_silesia_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_xpath, achievements)

    def type_in_laczy_nas_pilka(self, pilka):
        self.field_send_keys(self.laczy_nas_pilka_xpath, pilka)

    def type_in_minut(self, minut):
        self.field_send_keys(self.dziewiecdziesiat_minut_xpath, minut)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_xpath, facebook)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_xpath)

    def click_on_the_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_xpath)

    def check_page_title(self):
        time.sleep(5)
        assert self.get_page_title() == self.expected_title