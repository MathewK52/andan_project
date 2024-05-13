#сбор данных о пикрейте и винрейте героев в патче 7.33
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

browser = webdriver.Chrome()
URL_TEMPLATE = "https://www.dotabuff.com/heroes/winning?date=patch_7.33"
browser.get(URL_TEMPLATE)
tabel = browser.find_element(By.CSS_SELECTOR, 'table.sortable')
rows = tabel.find_elements(By.TAG_NAME, 'tr')

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

wait = WebDriverWait(browser, 5)

heroes = []
win_rates = []
pick_rates = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    if cells:
        hero_cell = cells[1]
        heroes.append(hero_cell.text)
        win_rates.append(cells[2].text)
        pick_rates.append(cells[3].text)

df = pd.DataFrame({
    'Hero': heroes,
    'Win Rate': win_rates,
    'Pick Rate': pick_rates
})
print(df)
browser.quit()