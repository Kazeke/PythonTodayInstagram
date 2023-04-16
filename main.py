from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from auth_data import username, password, hashtag
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium import webdriver

# replace 'user:pass@ip:port' with your information
options = {
    'proxy': {
        'http': 'http://YkFP84:jEMbsq@103.74.76.49:8000',
        'https': 'https://YkFP84:jEMbsq@103.74.76.49:8000',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\PROXY\\chromedriver\\chromedriver.exe',
                          seleniumwire_options=options)
# driver.get('https://instagram.com')

# service = Service(executable_path="C:\\Users\\user\\Desktop\\InstaBot\\chromedriver\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

try:
    driver.get("https://instagram.com")
    time.sleep(20)
    text_box = driver.find_element(by=By.NAME, value="username")
    text_box.clear()
    text_box.send_keys(username)
    time.sleep(2)

    text_box = driver.find_element(by=By.NAME, value="password")
    text_box.clear()
    text_box.send_keys(password + Keys.ENTER)
    time.sleep(15)

    driver.execute_script('document.getElementsByClassName("_acan _acao _acas")[0].click()')
    time.sleep(10)
    driver.execute_script('document.getElementsByClassName("_a9-- _a9_1")[0].click()')
    time.sleep(10)

    try:
        # извлекаем ссылки на посты
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}')
        time.sleep(10)
        links = driver.find_elements(by=By.TAG_NAME, value="a")

        posts_urls = []
        for item in links:
            link = item.get_attribute("href")

            # фильтруем ссылки
            if "/p/" in link:
                posts_urls.append(link)
                print(link)

        # ставим лайки
        for url in posts_urls:
            try:
                driver.get(url)
                time.sleep(3)
                like_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//button//span//*[name()='svg' and @aria-label='Нравится']")))
                like_button.click()
                time.sleep(random.randrange(20, 30))
            except Exception as ex:
                print(ex)


    except Exception as ex:
        print(ex)


except Exception as ex:
    print(ex)

# https://www.youtube.com/watch?v=QIFIT0szu-o


# replace 'your_absolute_path' with your chrome binary's aboslute path
# driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\PROXY\\chromedriver\\chromedriver.exe', seleniumwire_options=options)
# driver.get('https://instagram.com')
# time.sleep(60)
# driver.quit()
