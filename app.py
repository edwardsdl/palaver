import contextlib

from flask import Flask
from selenium import webdriver

from palaver.pages import WelcomePage, SurveyPage

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/survey', methods=['POST'])
def survey():
    with open_browser() as browser:
        welcome_page = WelcomePage(browser)
        welcome_page.navigate_to_page()
        welcome_page.start_survey('1099-0650-1315-11001-00330155')

        for survey_page in survey_pages(browser):
            survey_page.answer_questions()


@contextlib.contextmanager
def open_browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')

    chrome = webdriver.Chrome(options=options)
    yield chrome
    chrome.quit()


def survey_pages(browser):
    for i in range(0, 3):
        yield SurveyPage(browser)
