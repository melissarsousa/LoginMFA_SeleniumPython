from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import pyotp
import time

# Initialize the TOTP object
totp = pyotp.TOTP(LoginPage.auth_code)

# Generate the current TOTP code
current_code = totp.now()

# Initialize the Selenium WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    login_page = LoginPage(driver)

    # Open the TOTP challenge page
    driver.get("https://authenticationtest.com/totpChallenge/")

    # Enter the email (or username)
    login_page.preencher_email("totp@authenticationtest.com")

    # Enter the password
    login_page.preencher_senha("pa$$w0rd")

    # Enter the TOTP code
    login_page.preencher_mfa(current_code)

    # Click the login button
    login_page.clicar_login()

    # Wait for the result (optional)
    time.sleep(5)

    test_status = driver.find_element(By.XPATH,"/html/body/div[1]/h1").text

    if test_status=="Login Success":
        assert True
    else:
        assert False

finally:
    # Close the browser
    driver.quit()