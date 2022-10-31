from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import action_builder
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
# khai bao bien browser
browser = webdriver.Chrome(executable_path='./chromedriver')


def savePdf():
    iframe = browser.find_element(By.XPATH, "//iframe")
    if iframe is not None:
        browser.switch_to.frame(iframe)
        # w = WebDriverWait(browser, 7)
        # w.until(EC.presence_of_element_located(By.XPATH, "//button[contains(@id,'download')]"))
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@id,'download')]"))).click()
        button = browser.find_element(By.XPATH, "//button[contains(@id,'download')]")
        if button is not None:
            print('----->')
            # actions = ActionChains(browser)

            # actions.move_to_element(button)
            # sleep(5)
            # actions.click(button)
            # actions.perform()
            # sleep(5)
            # # dong trinh duyet
            # browser.close()
        browser.switch_to.default_content()


# mo thu trang web
# browser.get('https://mega.nz/file/RqggSDrS#ip_8qAT6h4llnX8PbAblNTBybjXUGirCdMZC3KPWdyo')
browser.get('https://sachgiaokhoavn.com/lop-9/lop-9-nxb-giao-duc/511-lich-su-9-lop-9-nxb-giao-duc.html')
savePdf()
