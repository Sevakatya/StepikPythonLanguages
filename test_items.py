import time
class TestLanguages():
    def test_find_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        assert browser.find_element_by_css_selector("#add_to_basket_form"), \
        'The button "add to basket" is not displayed'
