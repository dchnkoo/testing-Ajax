# appium dependecies
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# waiting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

import logging



# setup loger
logging.basicConfig(filename="log_file.log", 
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger()


error = logging.FileHandler("log_file.log")
error.setLevel(logging.ERROR)
error.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(error)



class TestApp:
        
    def setup(self) -> dict:
        return {
            "platformName": "Android",
            "platformVersion": "13",
            "automationName": "UIAutomator2"
        }
            

    def connect_driver(self) -> dict[webdriver.Remote, str] | bool:
        d = None

        try:
            logger.info('Connect driver...')

            d = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(self.setup()))
            
        except Exception as e:
                logger.error((e, e.args))
                return False

        else:
            info_driver = d.capabilities['deviceName'] + ' Android ' + d.capabilities['platformVersion']
            
            logger.info('\n\n' + '#' * 30 + '\n' + info_driver + ' CONNECTED')
            return {'driver': d, 'info': info_driver}
        
    
    def quit_from_driver(self, driver: str) -> None:
        logger.info("SESSION END")
        driver.quit()



    def open_app(self, driver: dict, app: str) -> bool:
        con = driver['driver']
        info = driver['info']

        try:
            logger.info(info + f' OPENING {app}')

            wait = WebDriverWait(con, 5)
            el = wait.until(es.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, app)))
            el.click()

        except Exception as e:
            logger.error(f"{info} {(e, e.args)}")
            return False
        
        else:
            logger.info(info + f' OPEN {app}')
            return True



    def notifications_window_close(self, driver: dict, id: str) -> bool:
        con = driver['driver']
        info = driver['info']

        try:
            wait = WebDriverWait(con, 5)
            el = wait.until(es.visibility_of_any_elements_located((AppiumBy.ID, id)))
            el.click()

        except Exception as e:
            logger.error((e, e.args))
            return False
        
        else:
            logger.info(f"{info} notification window closed")
            return True
        


    def login_to_app(self, driver: dict, 
                     **kwargs: dict['id-login-page': str,
                                    'id-login': str,
                                    'login': str,
                                    'password': str]) -> bool:

        con = driver['driver']
        info = driver['info']

        try:
            logger.info(f"{info} go to login page..")

            wait = WebDriverWait(con, 10)
            el = wait.until(es.element_to_be_clickable((AppiumBy.XPATH, kwargs['id-login-page'])))
            el.click()
            

            logger.info(f"{info} start logging to app...")

            email = wait.until(es.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')))
            email.clear()
            email.send_keys(kwargs['login'])

            wait.until(es.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'))).send_keys(kwargs['password'])


            btn = wait.until(es.element_to_be_clickable((AppiumBy.XPATH, kwargs['id-login'])))
            btn.click()

            wait.until(es.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.ajaxsystems:id/noHubs"]')))
        except Exception as e:
            logger.error(f"{info} {e}")
            return False

        else:

            logger.info(f"{info} success login!")
            con.press_keycode(3)
            return True


    def exit_from_app(self, driver: dict) -> bool:
        con = driver['driver']
        info = driver['info']

        try:
            wait = WebDriverWait(con, 7)

            logger.info(f"{info} go to menu..")
            el = wait.until(es.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]')))
            el.click()
            logger.info(f"{info} in burger menu")

            logger.info(f"{info} go to settings..")
            settings = wait.until(es.element_to_be_clickable((AppiumBy.XPATH, '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]')))
            settings.click()
            logger.info(f"{info} in settings")

            logging.info(f"{info} exit from app..")
            window = wait.until(es.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/account_info"])[1]')))
            location = window.location
            x, y = location['x'], location['y']

            screen_size = con.get_window_size()
            screen_height, screen_width = screen_size['height'], screen_size['width']

            scroll_x_start = (x + screen_width) / 2
            scroll_y_start = (y + screen_height) / 2

            touch = TouchAction(con)
            touch.press(x=scroll_x_start, y=scroll_y_start).move_to(x=screen_width, y=0).release().perform()

            exit_ = wait.until(es.visibility_of_element_located((AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]')))
            exit_.click()

            wait.until(es.visibility_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/root"]')))
        except Exception as e:
            logger.error(e)
            return False

        else:
            logger.info(f"{info} exit succes!")
            con.press_keycode(3)
            return True