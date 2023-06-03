from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import json
import os

def init_driver():
    # Creates a new instance of the Chrome web driver
    options = webdriver.ChromeOptions()
    # set log level to SEVERE
    options.add_argument('--log-level=3') 
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def go_to_category(driver, category):
    anchor_element = driver.find_element(By.XPATH, f"//nav//a[span[text()='{category}']]")
    anchor_element.click()


def get_news_links(driver):

    div_element_1 = driver.find_element(By.ID, "topos-component")
    div_element_2 = div_element_1.find_element(By.XPATH, "following-sibling::div[@role='region']")

    # get anchors and extract the href URLs
    anchor_elements_1 = div_element_1.find_elements(By.TAG_NAME, "a")
    anchor_elements_2 = div_element_2.find_elements(By.TAG_NAME, "a")
    anchor_elements = anchor_elements_1 + anchor_elements_2

    # we get the links that end with a hyphen and a sequence of numbers: '-\d+$'
    links = [anchor_element.get_attribute("href") for anchor_element in anchor_elements if re.search(r'-\d+$', anchor_element.get_attribute("href"))]

    return links

def get_category_links(driver, category):
    go_to_category(driver, category)
    links = get_news_links(driver)
    return links

def process_articles(driver, links):
    visited_links = set()

    for link in links:
        # Extract the sequence of digits at the end of the link
        match = re.search(r'\d+$', link)
        if match:
            article_id = match.group(0)
            file_path = os.path.join("articles", f"{article_id}.json")

            # Check if the article file already exists
            if os.path.exists(file_path):
                print(f"Skipping link: {link}. Article already processed.")
                continue

            # Visit the link
            driver.get(link)
            time.sleep(1)

            # Get the title from the H1 element
            title_element = driver.find_element(By.TAG_NAME, "h1")
            title = title_element.text

            # Get the body content from div elements with attribute data-component="text-block"
            body_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-component='text-block']")
            body = "\n".join(element.text for element in body_elements)

            # Create a dictionary with title and body content
            article_data = {"title": title, "body": body}

            # Write the article data to the JSON file
            with open(file_path, "w") as json_file:
                json.dump(article_data, json_file, indent=4)

            print(f"Processed link: {link}. Article saved as: {file_path}")

            # Add the visited link to the set
            visited_links.add(link)

    # Return the set of visited links
    return visited_links

if __name__ == "__main__":


    driver = init_driver()
    driver.get('https://www.bbc.com/news')

    business_links = get_category_links(driver, 'Business')
    tech_links = get_category_links(driver, 'Tech')

    links = business_links + tech_links
    # conserve only unique links
    links = list(set(links))

    visited_links = process_articles(driver, links)
    print('Visited Links:', visited_links)

    time.sleep(5)
