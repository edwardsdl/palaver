class BasePage:
    def __init__(self, browser):
        self._browser = browser


class WelcomePage(BasePage):
    def navigate_to_page(self):
        self._browser.get('https://www.talktoregal.com')

    def start_survey(self, access_code):
        access_code = access_code.split('-')

        self._browser.find_element_by_id('CN1').send_keys(access_code[0])
        self._browser.find_element_by_id('CN2').send_keys(access_code[1])
        self._browser.find_element_by_id('CN3').send_keys(access_code[2])
        self._browser.find_element_by_id('CN4').send_keys(access_code[3])
        self._browser.find_element_by_id('CN5').send_keys(access_code[4])

        self._browser.find_element_by_id('NextButton').click()


class SurveyPage(BasePage):
    def answer_questions(self):
        ...
