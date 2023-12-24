import pytest
import logging

from framework.login_page import LoginPage
from framework.home_page import HomePage

from tests.conftest import driver


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    web_driver, info = driver
    
    logging.info(f"{info} init LoginPage..")
    yield [LoginPage(web_driver, 10), info]


@pytest.fixture(scope='function')
def home_page_fixture(driver):
    web_driver, info = driver

    logging.info(f"{info} init HomePage..")
    yield [HomePage(web_driver, 10), info]