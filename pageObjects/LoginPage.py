from selenium.webdriver.common.by import By


class LoginPage:

    email_id = "email"
    password_id = "password"
    mfa_id = "totpmfa"
    botaoLogin_xpath = "/html/body/div[1]/div/div[2]/form/input"

    auth_code = "I65VU7K5ZQL7WB4E"

    def __init__(self,driver):
        self.driver=driver

    def preencher_email(self,email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def preencher_senha(self,senha):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(senha)

    def preencher_mfa(self,mfa):
        self.driver.find_element(By.ID, self.mfa_id).clear()
        self.driver.find_element(By.ID, self.mfa_id).send_keys(mfa)

    def clicar_login(self):
        self.driver.find_element(By.XPATH, self.botaoLogin_xpath).click()