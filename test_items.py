import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector(".btn-add-to-basket")