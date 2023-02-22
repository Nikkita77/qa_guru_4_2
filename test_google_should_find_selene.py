from selene.support.shared import browser
from selene import be, have
import pytest
from webdriver_manager.core import driver


@pytest.fixture()
def set_up():
        driver.set_window_size(800, 600)
        print("Тест старт")
        yield
        print("Окончание теста")

def test_find_google(set_up):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_find_google(set_up):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('geghwheerherhjjjrthjfgnhfgn').press_enter()
    browser.element("//*[@id='topstuff']/div/div/ul/li[1]").should(have.text('Убедитесь, что все слова написаны без ошибок'))
