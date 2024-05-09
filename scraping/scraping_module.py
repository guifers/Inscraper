import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from drivers.chrome_driver import create_chrome_driver
from filewriter.file_writer import write_to_file,verify_folder
def get_time():
    return datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_until_no_more(driver):
    match = False
    while not match:
        last_count = driver.execute_script(
            "return document.body.scrollHeight")
        time.sleep(3)
        scrolldown = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        if last_count == scrolldown:
            match = True


def scrape_instagram(user_to_scrape, user, pw):
    print(verify_folder('a', user_to_scrape))
    driver = create_chrome_driver()
    driver.get('https://www.instagram.com/')
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    footer_element = soup.find(string={'Productos de Meta'})
    footer_element2 = soup.find_all("button")
    divTag = soup.find_all("div", {"role": "dialog"})
    botonqueno = driver.find_element(
        "xpath", "//button[contains(text(), 'Permitir todas las cookies')]").click()
    time.sleep(4)
    username = driver.find_element("css selector", "input[name='username']")
    password = driver.find_element("css selector", "input[name='password']")
    username.clear()
    password.clear()
    username.send_keys(user)
    password.send_keys(pw)
    login = driver.find_element("css selector", "button[type='submit']").click();
    time.sleep(10)
    ahorano = driver.find_element(
        "xpath", "//div[contains(text(), 'Ahora no')]").click()
    time.sleep(10)
    ahorano2 = driver.find_element(
        "xpath", "//button[contains(text(), 'Ahora no')]").click()
    time.sleep(4)
    searchbox1 = driver.find_element(
        "css selector", "svg[aria-label='Búsqueda']").click()
    time.sleep(4)
    searchbox = driver.find_element("css selector", "input[placeholder='Busca']")
    searchbox.send_keys(user_to_scrape)
    driver.get('https://www.instagram.com/' + user_to_scrape)
    print(user_to_scrape)
    path = 'D:\Proyectos\Instalker\\'
    filename = path + user_to_scrape + '\\' + user_to_scrape + '_' + get_time() + ".txt"  # Adjust file extension as needed
    print(filename)
    with open(filename, "w") as f:
        pass
    scroll_until_no_more(driver)
    time.sleep(4)
    posts = []
    links = driver.find_elements("tag name", "a")
    for link in links:
        post = link.get_attribute('href')
        if '/p/' in post:
            posts.append(post)
    likes_por_publicacion = {}
    for post in posts:
        driver.get(post + 'liked_by/')
        time.sleep(4)
        scroll_down(driver)
        userlinks = driver.find_elements(By.CSS_SELECTOR, "a[role='link']")
        likes = set()
        for userlink in userlinks:
            href_value = userlink.get_attribute("href")[26:-1]
            if href_value and "liked_by" not in href_value and "inbox" not in href_value and "explore" not in href_value and "reels" not in href_value:
                likes.add(href_value)
        likes_por_publicacion[post] = len(likes)
        write_to_file(filename, f"Publicación: {post}, Likes: {len(likes)}\n")
        for like in likes:
            write_to_file(filename, f"- {like}\n")
    for post, likes in likes_por_publicacion.items():
        print(f"Publicación: {post}, Likes: {likes}")