import time
class TestLanguages():
    def test_different_languages(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        checkbasket = browser.find_element_by_css_selector("#add_to_basket_form")
        assert checkbasket.is_displayed()