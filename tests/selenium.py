from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("http://127.0.0.1:8000/")
    driver.find_element(By.XPATH, "/html/body/main/div/header/a/form/button").click()
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("roman_admin")
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("createsuperuser")
    driver.find_element(By.XPATH, '/html/body/main/div/form/button').click()
    driver.quit()