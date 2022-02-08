import pytest
import time

links = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
]


@pytest.mark.parametrize('link', links)
def test_find_add_to_basket_button(browser, link):
    browser.get(link)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    time.sleep(30)
    find_buttons = browser.find_elements_by_css_selector('#add_to_basket_form .btn-add-to-basket')
    assert len(find_buttons) > 0, 'Отсуствует кнопка добавления в корзину'

