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

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_visible(self.login_field_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_header_text(self):
        self.assert_element_text(self.driver, self.text_xpath, self.expected_text)

    def select_language(self, language):
        self.click_on_the_element(self.language_dropdown_button_xpath)
        time.sleep(1)
        if language == "english":
            self.click_on_the_element(self.english_option_xpath)
        else:
            self.click_on_the_element(self.polish_option_xpath)