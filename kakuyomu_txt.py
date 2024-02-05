from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pathlib import Path
import time
import sys

# Initialize the WebDriver for Firefox
driver = webdriver.Firefox()

# Function to wait for the "Load More" button and click it
def click_load_more_button(xpath):
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        load_more_button.click()
        print("Clicked 'Load More' button.")
        # Wait for additional content to load, adjust time as necessary
        time.sleep(5)  # Adjust based on your page's loading time
    except TimeoutException:
        print("Load More button not found or no more content to load.")

# Function to scrape chapter URLs after dynamically loading content
def get_urls():
    chapter_urls = []
    elements = driver.find_elements(By.CSS_SELECTOR, "a[class*='WorkTocSection_link_']")
    for element in elements:
        chapter_urls.append(element.get_attribute('href'))
    return chapter_urls

# Function to scrape title and content for each chapter URL
def scrape_and_save_content(chapter_url, file_name_start):
    driver.get(chapter_url)
    try:
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.widget-episodeTitle"))
        ).text.strip()
        
        content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.widget-episodeBody"))
        ).text.strip()

        # Replace characters not allowed in file names
        safe_title = "".join([c if c.isalnum() else "_" for c in title])
        file_path = f"./output/{file_name_start}{safe_title}.txt"

        # Save as a text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(title + "\n\n" + content)
        print(f"Successfully wrote: {file_path}")
    except TimeoutException:
        print(f"Failed to load content for {chapter_url}")

# Main Execution Flow
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]
    driver.get(url_to_fetch)

    # XPath for the "Load More" button
    load_more_button_xpath = "//div[contains(text(), 'つづきを表示')]/ancestor::button"
    click_load_more_button(load_more_button_xpath)

    # Ensure the output directory exists
    Path("./output").mkdir(parents=True, exist_ok=True)

    # Fetch chapter URLs using Selenium
    urls = get_urls()

    # Scrape and save content for each chapter
    for idx, url in enumerate(urls, start=1):
        name_initial = str(idx).zfill(3) + "-"
        scrape_and_save_content(url, name_initial)
        # Adding a short delay can help with not overloading the server
        time.sleep(1)

    # Clean up: Close the browser window
    driver.quit()
