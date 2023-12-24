import subprocess
import logging
import time
import os

import pytest

from appium import webdriver
from appium.options.common import AppiumOptions

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    logging.info('START SERVER...')
    appium = subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.PIPE,
        env=os.environ,
        shell=True
    )    
    time.sleep(10)

    logging.info("SERVER STARTED")
    
    yield 

    appium.terminate()
    appium.wait()


@pytest.fixture(scope='session')
def driver(run_appium_server):
    logging.info("CONNECT TO DEVICE..")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=AppiumOptions().load_capabilities(android_get_desired_capabilities()))
    info = driver.capabilities['deviceName'] + ' Android ' + driver.capabilities['platformVersion']

    logging.info(f"DEVICE {info} CONNECTED")
    yield [driver, info]
    
    driver.quit()

    logging.info(f"{info} END SESSION")