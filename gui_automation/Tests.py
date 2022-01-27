from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.headless = True
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--disable-dev-shm-usage")
#driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
url = 'http://localhost:5000/'


longitude_el = "/html/body/div/form/input[1]"
latitude_el = "/html/body/div/form/input[2]"
median_age_el = "/html/body/div/form/input[3]"
total_rooms_el = "/html/body/div/form/input[4]"
population_el = "/html/body/div/form/input[5]"
households_el = "/html/body/div/form/input[6]"
median_income_el = "/html/body/div/form/input[7]"
submit = "/html/body/div/form/button"
expected_url = "predict"


def open_url(driver, url):
   driver.get(url)


def add_field(driver, value, field):
   username_field = driver.find_element(By.XPATH, field)
   username_field.clear()
   username_field.send_keys(value)


def add_credentials(driver, longitude, latitude, median_age, total_rooms, population, households, median_income):
   add_field(driver, longitude, longitude_el)
   add_field(driver, latitude, latitude_el)
   add_field(driver, median_age, median_age_el)
   add_field(driver, total_rooms, total_rooms_el)
   add_field(driver, population, population_el)
   add_field(driver, households, households_el)
   add_field(driver, median_income, median_income_el)


def submit_form(driver):
   driver.find_element(By.XPATH, submit).click()


def verify_url(driver, url):
   assert (url + expected_url) == driver.current_url


    
