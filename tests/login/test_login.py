from tests.login.conftest import user_login_fixture

import pytest
import logging


@pytest.mark.parametrize('param_login, password', 
                         [('qa.ajax.app.automation@gmail.com',
                           'qa_automation_password'), (
                            'wrong_email@gmail.com',
                            'wrong_password'
                           )])
def test_login_to_ajax(user_login_fixture, param_login, password):
    driver, info = user_login_fixture

    logging.info(f"{info} GO TO LOGIN PAGE..")
    assert driver.click_login_btn() == True

    logging.info(f"{info} START LOGIN TO APP")
    login_to = driver.login_to_ajax(param_login, password)

    if login_to:
        logging.info(f"{info} LOGIN TO APP SUCCESS")
        assert login_to == True
        driver.exit_()
    else:
        logging.info(f"{info} {login_to}")
        logging.info(f"{info} LOGIN TO APP IS NOT SUCCESS")
        assert login_to == False
