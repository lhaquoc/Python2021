from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
# khai bao bien browser
browser = webdriver.Chrome(executable_path='./chromedriver')


def savePdf(url):
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="startholder"]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[2]/div[1]/button'))).click()
    # Open a new window
    browser.execute_script("window.open('');")
    # Switch to the new window
    browser.switch_to.window(browser.window_handles[-1])


# mo thu trang web
# browser.get('https://mega.nz/file/RqggSDrS#ip_8qAT6h4llnX8PbAblNTBybjXUGirCdMZC3KPWdyo')
urls = [
    "https://mega.nz/file/1qpAhRZa#exhz8xrQeF-aHAnGyLC1Q9grFUGqhKr4vEzR6KhgLnw",
    "https://mega.nz/file/pzgwCLjK#gHcIM7KtVLP5j4vG3qP4nbFbP5IoeIlenVhW8h8P56Y",
    "https://mega.nz/file/JnwkATJb#O89LOjv6iD80KlkkLCWDymOFyXpM2czhwqLmg4vt5sM",
    "https://mega.nz/file/03hCTJ4S#xM6NsNzhsuIutfnmeSr5WsC6IK9OftCHHOeygRanZ2U",
    "https://mega.nz/file/h2wiAR5L#dpO_UvykwxXX0P0t3ku8-fnRz71adw6n4cPi7jREMIA",
    "https://mega.nz/file/digizTrI#5sk_JdQnyXuQWxIac9Yc4tgQgxAKcViBwJejOSug39c",
    "https://mega.nz/file/cyoUzRQa#j4zgEvHQ1plz7ISXs0Wx2w8UnDktJ2zNYnOt3uv-h8g",
    "https://mega.nz/file/Izh2FbCS#GjpmEyJKDjZOm4hMF1x3C45vhtj4sv9Jb3eZvBYX9J8",
    "https://mega.nz/file/U3wEiRYb#SbtqE3TGddQSzAYKKOqK09ctHSqNHdgUuEXhCNjAdi0",
    "https://mega.nz/file/96oyFLbD#-COITJl9IBRHlxja6xcvu9KohIatpkhOTe1-svmwxGM",
    "https://mega.nz/file/kz50VRzZ#LLFa06-u_yaIx3BXtFQo-bAFOJuShECoI15DxYbfSAQ"
]
for url in urls:
    savePdf(url)
sleep(10)
browser.close()
