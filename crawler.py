from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import action_builder
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from time import sleep
# khai bao bien browser
browser = webdriver.Chrome(executable_path='./chromedriver')

# mo thu trang web
browser.get('https://sachgiaokhoavn.com/')

# input to login
# email = browser.find_element(By.ID, 'email')
# email.send_keys('abcxyz')

# password = browser.find_element(By.ID, 'pass')
# password.send_keys('password')
# dung 5s

menu = browser.find_element(By.ID, 'main-menu')
menu_item_1 = browser.find_element(By.ID, 'menu-item-150968')
menu_item_2 = browser.find_element(By.ID, 'menu-item-161442')
menu_item_3 = browser.find_element(By.ID, 'menu-item-125811')
menu_item_4 = browser.find_element(By.ID, 'menu-item-125812')
menu_item_5 = browser.find_element(By.ID, 'menu-item-125813')
menu_item_6 = browser.find_element(By.ID, 'menu-item-161444')
menu_item_7 = browser.find_element(By.ID, 'menu-item-125815')
menu_item_8 = browser.find_element(By.ID, 'menu-item-125816')
menu_item_9 = browser.find_element(By.ID, 'menu-item-125817')
menu_item_10 = browser.find_element(By.ID, 'menu-item-125818')
menu_item_11 = browser.find_element(By.ID, 'menu-item-125819')
menu_item_12 = browser.find_element(By.ID, 'menu-item-125820')

# tao list menu items
menu_items = [menu_item_1,
              menu_item_2,
              menu_item_3,
              menu_item_4,
              menu_item_5,
              menu_item_6,
              menu_item_7,
              menu_item_8,
              menu_item_9,
              menu_item_10,
              menu_item_11,
              menu_item_12]
for item in menu_items:
    print(f'item: {item}')
# sub_menu_1 = browser.find_element(By.CLASS_NAME, 'sub-menu')
# hidden_submenu_1 = browser.find_element(By.ID, 'menu-item-161445')

actions = ActionChains(browser)


actions.move_to_element(menu)
sleep(1)
actions.move_to_element(menu_item_1)
sleep(1)
actions.move_to_element(menu_item_2)

# actions.move_to_element_with_offset(menu, -400, 0)
# print(menu_item_1)
# sleep(1)
# actions.move_to_element(menu)
# sleep(1)
# actions.move_to_element(menu_item_2)
# print(menu_item_2)
sleep(1)
actions.perform()

# for menu_item in menu_items:
#     sleep(2)
#     actions.move_to_element(menu_item)
#     print(menu_item)
#     actions.perform()
# actions.move_to_element(menu).perform()
# actions.move_to_element_with_offset(menu_item_1, 5, 25)
# actions.move_to_element(sub_menu_1)
# actions.move_to_element(hidden_submenu_1)
# actions.click(hidden_submenu_1)


sleep(5)

# dong trinh duyet
browser.close()
