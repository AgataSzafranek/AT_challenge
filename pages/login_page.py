import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en/login"
    text_xpath = "//*/div[1]/h5"
    expected_text = "Scouts Panel"
    language_dropdown_button_xpath = "//*[@aria-haspopup='listbox']"
    polish_option_xpath = "//*[@data-value='pl']"
    english_option_xpath = "//*[@data-value='en']"
