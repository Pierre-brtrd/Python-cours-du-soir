from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from math import *

# Définition de l'url
search_query = 'https://fr.indeed.com'

# Création et configuration des chrome options
chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

driver = webdriver.Chrome(options=chrome_options)
driver.get(search_query)

search_bar = driver.find_element(By.NAME, "q")
keyword = input("Entrez la recherche que vous voulez faire :\n")

print("-----------------------")
print("Recherche pour", keyword)
search_bar.send_keys(keyword)
search_bar.send_keys(Keys.RETURN)

# Préparation des données de sorties
columns = ["Poste", "Société", "Ville", "Description", "Salaire"]
datas = []

wait = WebDriverWait(driver, 5)

links = []

# Récupération des liens de chaque offre d'emploi
while True:
    new_links = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".result")))
    links.extend([l.get_attribute("href") for l in new_links])

    try:  # EC needed as otherwise the element was not clickable
        next_page = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[contains(@class, 'pagination-list')]/li[last()]/a")))
        ActionChains(driver).move_to_element(next_page).click().perform()

    except TimeoutException:
        print("Liens collectés")
        break

# Récupération des données pour chaque liens
for link in links:

    data = []
    driver.get(link)

    # Poste
    try:
        title = driver.find_element(
            By.CSS_SELECTOR, ".jobsearch-JobInfoHeader-title-container").text
        data = [title]

    except NoSuchElementException:
        data = ["Offre sans titre"]

    # Société
    try:
        company = driver.find_element(
            By.XPATH, "//div[contains(@class, 'jobsearch-InlineCompanyRating')]").text
        data.append(company)

    except NoSuchElementException:
        data.append("NON IDENTIFIÉ")

    # Ville
    try:
        location = driver.find_element(
            By.XPATH, "//div[contains(@class, 'jobsearch-JobInfoHeader-subtitle')]/div[2]").text
        data.append(location)

    except NoSuchElementException:
        data.append("NON IDENTIFIÉE")

    # Résumé
    try:
        description = driver.find_element(
            By.CSS_SELECTOR, "#jobDescriptionText").text
        data.append(description)

    except NoSuchElementException:
        data.append("NON IDENTIFIÉ")

    # Salaire
    try:
        salary = driver.find_element(
            By.XPATH, "//div[contains(@class, 'jobsearch-JobMetadataHeader-item')]").text
        data.append(salary)

    except NoSuchElementException:
        data.append("NON IDENTIFIÉ")

    datas.append(data)

# Mise en place du dataframe et export vers csv
datas_df = pd.DataFrame(datas)
datas_df.columns = columns
datas_df.to_csv("".join([keyword.replace(" ", "-"), ".csv"]), encoding='utf-8')

print("Le fichier", "".join(
    [keyword.replace(" ", "-"), ".csv est disponible."]))
