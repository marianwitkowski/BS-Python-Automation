from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

import time, os, sys

options = ChromeOptions()
#options.add_argument("--headless")  # opcjonalnie, jeśli chcesz, aby przeglądarka była niewidoczna
options.add_experimental_option("prefs", {
  "download.default_directory": os.getcwd(),
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing_for_trusted_sources_enabled": False,
  "safebrowsing.enabled": False
})


driver = webdriver.Chrome(options=options)
driver.get("https://stooq.pl/")
time.sleep(5)

btn = driver.find_element(by=By.CLASS_NAME, value="fc-primary-button")
btn.click()
time.sleep(3)
driver.refresh()

# czekamy maks 10 sek. na pojawienie sie pola o nazwie klasy f13
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located( (By.CLASS_NAME, "f13") )
    )
except:
    sys.exit(1)

input_el = driver.find_element(by=By.CLASS_NAME, value="f13")
input_el.send_keys("PKN")
input_el.send_keys(Keys.ENTER)
time.sleep(4)

link = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Dane historyczne")
link.click()

while True:
    if driver.execute_script("return document.readyState") == "complete":
        break

# wypełnianie formularza
input_el = driver.find_element(by=By.NAME, value="d7") # dzień
input_el.clear()
input_el.send_keys("1")

input_el = driver.find_element(by=By.NAME, value="d3") # rok
input_el.clear()
input_el.send_keys("2020")

select = Select(driver.find_element(by=By.NAME, value="d5"))
select.select_by_visible_text("lut")

radio_buttons = driver.find_elements(by=By.NAME, value="i")
for radio_button in radio_buttons:
    if radio_button.get_attribute("value")=="w":
        radio_button.click()
        break
radio_button.send_keys(Keys.ENTER)

link = driver.find_element(by=By.LINK_TEXT, value="Pobierz dane w pliku csv...")
link.click()

time.sleep(5)
