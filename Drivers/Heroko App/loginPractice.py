from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

login = "tomsmith"
password = "SuperSecretPassword1"

def herokuAppLogin (login, password):
    chrome_options = Options()

    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID,
        'username').send_keys(login)

    driver.find_element(By.ID,
        'password').send_keys(password)

    driver.find_element(By.CLASS_NAME,
        'radius').click()

    title = "The Internet"
    actualTitle = driver.title

    print("The title of the web page is", actualTitle)
    assert(actualTitle == title)
    print("User logged in succesfully")

herokuAppLogin(login, password)
