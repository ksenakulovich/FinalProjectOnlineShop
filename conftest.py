import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose one of the languages available for testing')

@pytest.fixture(scope="function")
def browser(request):
    try:
        language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        yield browser
    except:
        raise pytest.UsageError("--Please choose an appropriate language available for testing")
    browser.quit()
