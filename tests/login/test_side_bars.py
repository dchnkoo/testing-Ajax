from tests.login.conftest import home_page_fixture, user_login_fixture

import logging
import pytest


@pytest.mark.parametrize('login, password', [('qa.ajax.app.automation@gmail.com',
                         'qa_automation_password')])
def test_go_to_home_page(user_login_fixture, login, password):
    web_driver, info = user_login_fixture

    logging.info(f"{info} GO TO HOME PAGE..")
    assert web_driver.click_login_btn() == True
    assert web_driver.login_to_ajax(login, password) == True


@pytest.mark.parametrize('button', [
    '//*[@resource-id="com.ajaxsystems:id/settings"]',
    '//*[@resource-id="com.ajaxsystems:id/help"]',
    '//*[@resource-id="com.ajaxsystems:id/logs"]',
    '//android.widget.Button'
])
def test_side_bar_options(home_page_fixture, button: str):
    web_driver, info = home_page_fixture

    logging.info(f"{info} TESTING {button} button")
    assert web_driver.check_menu_elements(button) == True

