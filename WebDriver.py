# Seleium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    def __init__(self, login_email, login_password):
        self.login_email = login_email
        self.login_password = login_password
        self.driver = self.set_driver()

    def set_driver(self):
        ## 設定Chrome的瀏覽器彈出時遵照的規則
        ## 這串設定是防止瀏覽器上頭顯示「Chrome正受自動控制」
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        ## 關閉自動記住密碼的提示彈窗
        options.add_experimental_option(
            "prefs",
            {
                "profile.password_manager_enabled": False,
                "credentials_enable_service": False,
            },
        )

        return webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager(driver_version="114.0.5735.90").install()
            )
        )

    # get into cusis
    def login_CUSIS(self):
        self.driver.get("https://cusis.cuhk.edu.hk/")
        self.driver.set_window_size(968, 1056)
        self.driver.set_window_position(0, 0)

        box_login_name = self.driver.find_element(By.NAME, "UserName")
        box_login_name.send_keys(self.login_email)
        box_login_pw = self.driver.find_element(By.NAME, "Password")
        box_login_pw.send_keys(self.login_password, Keys.RETURN)

        # login_click = self.driver.find_element(By.ID, "submitButton")
        # login_click.click()

        # get into time management section:
        self.driver.implicitly_wait(5)
        try:
            page_classManagement = self.driver.find_element(By.ID, "PS_SCHEDULE_L_FL$2")
            page_classManagement.click()
        except:
            print("cannot locate the class management section")
        print("your login in this CUSIS successfully, please enter the enroll section")

        self.driver.implicitly_wait(5)
        page_shoppingCart = self.driver.find_element(
            By.XPATH, "//span[@id='PTGP_STEP_DVW_PTGP_STEP_LABEL$5']"
        )
        page_shoppingCart.click()
        self.driver.implicitly_wait(15)
        button_OK = self.driver.find_element(
            By.XPATH, "//a[@id='DERIVED_REGFRM1_DETAILS_LINK']"
        )
        button_OK.click()
        self.driver.implicitly_wait(5)

        self.button_enroll = self.driver.find_element(
            By.XPATH, "//a[@id='DERIVED_SSR_FL_SSR_ENROLL_FL']"
        )
        self.button_validate = self.driver.find_element(
            By.XPATH, "//a[@id='DERIVED_SSR_FL_SSR_VALIDATE_FL']"
        )
        if self.button_validate:
            print("find the validate button successfully")
        if self.button_enroll:
            print("find the enroll button successfully")

    def register(self, register_mode):
        if register_mode == "e":
            self.button_enroll.click()
        if register_mode == "v":
            self.button_validate.click()


if __name__ == "__main__":
    webdriver = WebDriver(
        login_email="1155xxx@link.cuhk.edu.hk", login_password="xxxxxxxx"
    )
    webdriver.login_CUSIS()
    register_mode = input("please input your mode: ")
    webdriver.register(register_mode=register_mode)
    input("The programme is finished, enter any key to quit the browser")
