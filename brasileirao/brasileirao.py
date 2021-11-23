from selenium import webdriver

class Brasileirao(webdriver.Chrome):
    
    def __init__(self, driver_path, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(executable_path=driver_path, options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    def access_site(self):
        self.get("https://interativos.globoesporte.globo.com/futebol/brasileirao-serie-a/especial/simulador-do-brasileirao-2021")

    def scroll_table(self):
        scroll_to_table = self.find_element_by_class_name('rounds__namedisplay')
        scroll_to_table = scroll_to_table.location_once_scrolled_into_view
    
    def fill_table(self):
        round = self.find_element_by_css_selector('div[data-round-isvisible]')
        match = round.find_elements_by_class_name('match')
        for m in match:
            teams = m.find_elements_by_css_selector('div[class*="team team--"]')
            for t in teams:
                team_name = t.find_element_by_css_selector(
                    'abbr[class="team__name-abbr"]'
                    ).get_attribute('title')

                print('\n'+team_name+'\n')

                expected_result = input(f'Por favor, insira o valor pro time {team_name}: ')
                t.find_element_by_tag_name(
                    'input'
                    ).send_keys(expected_result)

    def next_round(self):
        while True:
            right_arrow = self.find_elements_by_css_selector('button[class="rounds__next"]')
            self.fill_table()
            if right_arrow:
                right_arrow[0].click()
            else:
                break