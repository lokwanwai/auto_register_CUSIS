# Seleium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# os
import time
import datetime
import json
import os


# get current time
def get_current_time():
    current_time = datetime.datetime.now().time()
    return current_time


# get_cusis_config_setting
def get_config():
    cwd = os.getcwd()
    config_path = os.path.join(cwd, "config.json")
    with open(config_path) as config_file:
        config = json.load(config_file)
        login_email = config["login_email"]
        login_password = config["login_password"]
        register_time = config["register_time"]
        selenium_driver_PATH = config["selenium_driver_PATH"]
    register_time = datetime.datetime.strptime(register_time, "%X.%f").time()
    return login_email, login_password, register_time, selenium_driver_PATH


# get into cusis
def login_CUSIS(login_email, login_password, selenium_driver_PATH):
    dricusis = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager(driver_version="114.0.5735.90").install()
        )
    )
    dricusis.get("https://cusis.cuhk.edu.hk/")
    dricusis.set_window_size(968, 1056)
    dricusis.set_window_position(0, 0)
    login_name = dricusis.find_element_by_name("UserName")
    login_pw = dricusis.find_element_by_name("Password")
    login_name.send_keys(login_email)
    login_pw.send_keys(login_password, Keys.RETURN)
    login_click = dricusis.find_element_by_xpath("//img[@id='PS_SCHEDULE_L_FL$2']")
    login_click.click()

    # get into time management section:
    dricusis.implicitly_wait(5)
    classmanagement = dricusis.find_element_by_xpath(
        "//span[@id='PTGP_STEP_DVW_PTGP_STEP_LABEL$5']"
    )
    classmanagement.click()
    welcome = """
    =======================================
    your login in this cusis sucessfully
    plesase enter the enroll section 

    ### input your option after selecting of your choices
    ### (v)=validate
    ### (e)=enroll
    =======================================
    """

    print(welcome)
    print(f"Your are going to register at {register_time}")
    return dricusis


def register_mode(dricusis, register_time):
    mode = input("what you want yo do next: ")
    try:
        validate = dricusis.find_element_by_xpath(
            "//a[@id='DERIVED_SSR_FL_SSR_VALIDATE_FL']"
        )
        enroll = dricusis.find_element_by_xpath(
            "//a[@id='DERIVED_SSR_FL_SSR_ENROLL_FL']"
        )
        if validate:
            print("\nfind the validate button successfuly\n")
        if enroll:
            print("\nfind the enroll button successfuly\n")

    except:
        print(
            "cannot locate the validate and enroll bottom, please restart the program"
        )
        return None

    if mode == "v":
        while True:
            current_time = get_current_time()
            print(current_time)
            if current_time >= register_time:
                validate.click()
                print("clicked")
                validate.click()
                print("clicked")
                validate.click()
                print("clicked")
                break
    if mode == "e":
        while True:
            current_time = get_current_time()
            print(current_time)
            if current_time >= register_time:
                enroll.click()
                print("clicked")
                enroll.click()
                print("clicked")
                enroll.click()
                print("clicked")
                break


if __name__ == "__main__":
    login_email, login_password, register_time, selenium_driver_PATH = get_config()
    dricusis = login_CUSIS(
        login_email=login_email,
        login_password=login_password,
        selenium_driver_PATH=selenium_driver_PATH,
    )
    register_mode(dricusis=dricusis, register_time=register_time)
