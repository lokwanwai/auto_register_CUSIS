import json
import os
from Timer import Timer
from WebDriver import WebDriver


class Controller:
    def __init__(self):
        self.get_config()
        self.timer = Timer(self.register_time)
        self.driver = WebDriver(self.login_email, self.login_password)

    def get_config(self):
        cwd = os.getcwd()
        config_path = os.path.join(cwd, "config.json")
        with open(config_path) as config_file:
            config = json.load(config_file)
            self.login_email = config["login_email"]
            self.login_password = config["login_password"]
            self.register_time = config["register_time"]

    def set_register_mode(self):
        welcome = """
        =======================================
        your login in this CUSIS successfully
        please enter the enroll section 

        ### input your option after selecting of your choices
        ### (v)=validate
        ### (e)=enroll
        =======================================
        """
        print(welcome)
        self.register_mode = input("input: ")
        while self.register_mode is not "v" or "e":
            print("please input the correct option")
            self.register_mode = input("input: ")


if __name__ == "__main__":
    controller = Controller()
    controller.driver.login_CUSIS()
    controller.set_register_mode()
    controller.timer.run()
    controller.driver.register(controller.register_mode)
