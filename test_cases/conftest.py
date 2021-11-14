from selenium import webdriver
import pytest
import logging

@pytest.fixture
def setup():
    driver=webdriver.Chrome('/Users/kelly/Downloads/chromedriver')
    return driver

@pytest.fixture
def logger():

    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename = "/Users/kelly/PycharmProjects/framework_template/logs/result.log" ,
                        level = logging.DEBUG,
                        format = log_format,
                        filemode = 'w')

    logger= logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.debug('*************** LOGGING STARTS *********************')
    return logger



