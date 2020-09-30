import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    browser.maximize_window()
    button = browser.find_element_by_css_selector('[id="add_to_basket_form"]>button[type="submit"]')
    assert button, "Button not found"

