from Tests import *
longitude = "-122.23"
latitude = "37.88"
median_age = "50"
total_rooms = "5"
population = "40000"
households = "2000"
median_income = "8.3252"

# Test step 1 - Open URL

def test_open_url(driver, url):
   open_url(driver, url)


# Test step 2 - Add credentials
def test_add_credentials(driver, longitude, latitude, median_age, total_rooms, population, households, median_income):
   add_credentials(driver, longitude, latitude, median_age, total_rooms, population, households, median_income)


# Test step 3 - Submit form
def test_submit_form(driver):
   submit_form(driver)


# Test step 4 - verify URL
def test_verify_url(driver, url):
   verify_url(driver, url)

test_open_url(driver, url)
test_add_credentials(driver, longitude, latitude, median_age, total_rooms, population, households, median_income)
test_submit_form(driver)
test_verify_url(driver, url)
