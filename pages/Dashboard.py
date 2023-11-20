from pages.base_page import BasePage


class Dashboard(BasePage):
    pass
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    dev_team_contact_xpath = "//*[text()='Dev team contact']"
    add_new_player_xpath = "//*[text()='Add player']"
    last_created_player_xpath = "//*/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//*/div/a[2]/button/span[1]"
    last_created_match_xpath = "//*/div/a[3]/button/span[1]"
    last_updated_match_xpath = "//*/div/a[4]/button/span[1]"
    last_updated_report_xpath = "//*/div/a[5]/button/span[1]"
