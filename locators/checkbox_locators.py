from selenium.webdriver.common.by import By


class CheckBoxLocators:

    ELEMENTS = (By.XPATH, "//div[@class='card mt-4 top-card'][1]")
    CHECK_BOX = (By.ID, "item-1")
    HOME_BUTTON = (By.XPATH, "//button[@class= 'rct-collapse rct-collapse-btn']")
    DOWNLOAD_BUTTON = (By.XPATH, "//ol/li/ol/li[3]/span/button")
    WORD_FILE_DOC = (By.XPATH, "//*[text() = 'Word File.doc']")
    SUCCESS_TEXT = (By.XPATH, "//span[@class='text-success']")