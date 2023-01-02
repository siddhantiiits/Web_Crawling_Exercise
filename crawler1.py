from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

DRIVER_PATH = '/Users/siddhanttiwari/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def crawl_page(src):
    driver.get(src)
    list_ref = '//*[@aria-label="Search results"]/li'
    for project_element in driver.find_elements(By.XPATH,list_ref):
        projectName = project_element.find_element(By.XPATH,'.//*[@class="package-snippet__name"]').text
        projectVersion = project_element.find_element(By.XPATH,'.//*[@class="package-snippet__version"]').text
        projectCreated = project_element.find_element(By.XPATH,'.//*[@class="package-snippet__created"]/time').text



        print(projectName,projectVersion,projectCreated)
        projct_info = [projectName,projectVersion,projectCreated]
        filename = "Django Projects.csv"
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(projct_info)

    xp_nextPage = '//*[@class="button-group button-group--pagination"]/a[last()]'
    nextPageLink = driver.find_element(By.XPATH,xp_nextPage).get_attribute("href")
    if not nextPageLink:
        return 'Sucessfully Crawled'

    return crawl_page(nextPageLink)


target_page = 'https://pypi.org/search/?&o=&c=Framework+%3A%3A+Django'

print(crawl_page(target_page))


