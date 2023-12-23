from init_app_func import TestApp

import pytest
import logging


app = TestApp()


@pytest.mark.parametrize('driver', [(app.connect_driver)])
def test_connection(driver):
    logging.info('DRIVER START CONNECT....')
    con = driver()

    # if type is dict method is correct
    assert type(con) == dict
    logging.info(f"{con['driver']} CONNECTED")



@pytest.mark.parametrize('driver', [(app.connect_driver)])
def test_open_app(driver):
    con = driver()

    # if type is dict method is correct
    assert type(con) == dict
    
    logging.info(f"{con} opening app Ajax")

    do = app.open_app(con, 'Ajax')
    assert do == True

    logging.info(f"{con} end app Ajax")
    con['driver'].press_keycode(3)


login = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]'
login_page = '//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"]'

@pytest.mark.parametrize('driver, app_name, kwargs, succes', 
                         [(app.connect_driver, 'Ajax', 
                           {'id-login-page': login_page,
                            'id-login': login,
                            'login': "qa.ajax.app.automation@gmail.com",
                            'password': 'qa_automation_password'}, True), 

                            (app.connect_driver, 'Ajax', 
                           {'id-login-page': login_page,
                            'id-login': login,
                            'login': "example_wrong@gmail.com",
                            'password': 'wrong_password'}, False)])
def test_login_to_app(driver, app_name, kwargs, succes):
    con = driver()
    logging.info(f"{con} CONNECT...")

    # if type is dict method is correct
    assert type(con) == dict

    logging.info(f"{con} CONNECTED!")
    logging.info(f"{con} OPENING {app_name}")
    op = app.open_app(con, app_name)
    assert op == True

    logging.info(f"{con} LOGGING in {app_name}...")
    login_to = app.login_to_app(con, **kwargs)

    if succes:
        assert login_to == True
        logging.info(f"{con} LOGGING in {app_name} SUCCES!")
   
        op = app.open_app(con, app_name)
        assert op == True

        exit_ = app.exit_from_app(con)
        assert exit_ == True
    else:
        assert login_to == False
        logging.info(f"{con} LOGGING in {app_name} SUCCES FAILED!")
        con['driver'].press_keycode(3)



