from locators.checkbox_locators import CheckBoxLocators
from pages.basepage import BasePage


class CheckBox(BasePage):

    locators = CheckBoxLocators()

    def open_elements_page(self):
        self.driver.execute_script('window.scrollBy(0, 200);')
        self.is_element_visible(self.locators.ELEMENTS).click()

    def open_element_list(self):
        self.is_element_visible(self.locators.CHECK_BOX).click()

    def open_home_list(self):
        self.is_element_visible(self.locators.HOME_BUTTON).click()

    def open_download_list(self):
        self.is_element_visible(self.locators.DOWNLOAD_BUTTON).click()

    def word_file_click(self):
        self.is_element_visible(self.locators.WORD_FILE_DOC).click()

    def check_success_text(self):
        success_text = 'wordFile'
        assert self.is_element_visible(self.locators.SUCCESS_TEXT).text == success_text, "Values not equal"


