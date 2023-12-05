from pages.base_page import BasePage

# TASK 2 SUBTASK 5
class AddAMatchForm(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    matches_xpath = "//*[text()='Matches']"
    reports_xpath = "//*[text()='Reports']"
    polski_xpath = "//*[text()='Polski']"
    my_team_xpath = "//*[@name='myTeam']"
    enemy_team_xpath = "//*[@name='enemyTeam']"
    my_team_score_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_xpath = "//*[@name='enemyTeamScore']"
    date_xpath = "//*[@name='date']"
    match_at_home_xpath = "//*/label[1]/span[1]/span[1]/input"
    match_out_home_xpath = "//*/label[2]/span[1]/span[1]/input"
    tshirt_color_xpath = "//*[@name='tshirt']"
    league_xpath = "//*[@name='league']"
    time_played_xpath = "//*[@name='timePlayed']"
    number_xpath = "//*[@name='number']"
    web_match_xpath = "//*[@name='webMatch']"
    general_xpath = "//*[@name='general']"
    rating_xpath = "//*[@name='rating']"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"

