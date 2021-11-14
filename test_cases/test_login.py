import pytest
from selenium import webdriver
from page.longin_page import login
from utilities.readConfig import read_config


class Test_001_login:

    config = read_config()
    baseURL = config.getApplicationURL()
    username = config.getApplication_username()
    password = config.getApplication_password()




    def test_homepageTitle(self,setup,logger):

        logger.info ("****************** Test_001 login Test **************************")
        logger.info ("****************** Verifying Home Page Title **************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title=="Your store. Login":
            self.logger.error("****************** Home Page Title Verified: Passed **************************")
            assert True
            self.driver.close()

        else:
            self.logger.info("****************** Home Page Title Verified: Failed **************************")
            self.driver.save_screenshot("./screenshots/homepage-failed.jpg")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info("****************** Home Page login: Passed **************************")
            assert True
            self.driver.close()
        else:
            self.logger.error("****************** Home Page Login: Failed **************************")
            self.driver.save_screenshot("./screenshots/login-failed.jpg")
            self.driver.close()
            assert False

