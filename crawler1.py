from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

DRIVER_PATH = '/Users/siddhanttiwari/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def crawl_page(src):
    driver.get(src)
    list_ref = '//*[@aria-label="Search results"]/li'
    projectsPerPage = len(driver.find_elements(By.XPATH, list_ref))

    for projectCount in range(1,projectsPerPage):
        xp_projectName = list_ref+'['+ str(projectCount)  +']//*[@class="package-snippet__name"]'
        xp_projectVersion = list_ref + '[' + str(projectCount) + ']//*[@class="package-snippet__version"]'
        xp_projectCreated = list_ref + '[' + str(projectCount) + ']//*[@class="package-snippet__created"]/time'
        xp_projectDescription = list_ref + '[' + str(projectCount) + ']//*[@class="package-snippet__description"]'

        projectName = driver.find_element(By.XPATH, xp_projectName).text
        projectVersion = driver.find_element(By.XPATH, xp_projectVersion).text
        projectCreated = driver.find_element(By.XPATH, xp_projectCreated).text
        # projctDescription = driver.find_element(By.XPATH,xp_projectDescription).text
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
tp2 = 'https://pypi.org/search/?c=Framework+%3A%3A+Django&o=&page=495'
print(crawl_page(tp2))


