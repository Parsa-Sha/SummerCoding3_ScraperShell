from selenium import webdriver
from selenium.webdriver.chrome.service import Service

web = 'https://www.audible.ca/search'
path = 'C:/Files/Code_Actually/ScrapeAndStore/chromedriver-win64/chromedriver.exe' # Change to chromedriver's path
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)
# Change code based on HTML elements that are being scraped.
products = driver.find_elements(by='xpath', value='//li[contains(@class, "productListItem")]')

for product in products:
    print(product.find_element(by='xpath', value='.//h3[contains(@class, "bc-heading")]').text)
    print(product.find_element(by='xpath', value='.//li[contains(@class, "authorLabel")]').text)
    print(product.find_element(by='xpath', value='.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()
