from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def create_chrome_driver():
    service = Service(executable_path='D:\Proyectos\Instalker\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver
