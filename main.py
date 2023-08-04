import json
import os
from Timer import Timer
from WebDriver import WebDriver
import time


class Controller:
    def __init__(self):
        self.get_config()
        self.timer = Timer(self.REGISTER_TIME)
        self.driver = WebDriver(self.LOGIN_EMAIL, self.LOGIN_PASSWORD)

    def get_config(self):
        cwd = os.getcwd()
        config_path = os.path.join(cwd, "config.json")
        with open(config_path) as config_file:
            config = json.load(config_file)
            self.LOGIN_EMAIL = config["login_email"]
            self.LOGIN_PASSWORD = config["login_password"]
            self.REGISTER_TIME = config["register_time"]

    def set_register_mode(self):
        welcome = """
        =======================================
        ### input your option after selecting of your choices
        ### (v)=validate
        ### (e)=enroll
        =======================================
        """
        print(welcome)
        self.register_mode = input("input: ")
        while (self.register_mode != "v") and (self.register_mode != "e"):
            print("please input the correct option")
            self.register_mode = input("input: ")


if __name__ == "__main__":
    controller = Controller()
    controller.driver.login_CUSIS()
    controller.set_register_mode()
    controller.timer.run()
    controller.driver.register(controller.register_mode)
    input("The programme is finished, enter any key to close the browser ")
