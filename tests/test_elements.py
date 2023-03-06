from pages.checkbox_page import CheckBox

class TestElements:


    def test_checkbox_page(self, driver):
        checkbox_page = CheckBox(driver, 'https://demoqa.com')
        checkbox_page.open()
        checkbox_page.open_elements_page()
        checkbox_page.open_element_list()
        checkbox_page.open_home_list()
        checkbox_page.open_download_list()
        checkbox_page.word_file_click()
        checkbox_page.check_success_text()
