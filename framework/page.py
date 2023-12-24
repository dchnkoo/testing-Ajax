from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# waiting drivers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

class Page:

    def __init__(self, driver, wait_time: int = 5):
        self.driver_waiter = WebDriverWait(driver, wait_time)
        self.driver = driver


    def find_element(self, selector: str, by: str = AppiumBy.XPATH, clickable: bool = False):
        try:
            if clickable:
                return self.driver_waiter.until(es.element_to_be_clickable((by, selector)))

            return self.driver_waiter.until(es.visibility_of_element_located((by, selector)))
        
        
        except Exception as e:
            return False


    def click_element(self, element) -> bool | Exception:
        try:
            element.click()
        except Exception as e:
            raise e
        else:
            return True
        

    def scroll(self, element, scroll_x: int, scroll_y: int) -> bool | Exception:
        try:
            location = element.location
            x, y = location['x'], location['y']

            screen_size = self.driver.get_window_size()
            screen_height, screen_width = screen_size['height'], screen_size['width']

            scroll_x_start = (x + screen_width) / 2
            scroll_y_start = (y + screen_height) / 2

            touch = TouchAction(self.driver)
            touch.press(x=scroll_x_start, y=scroll_y_start).move_to(x=scroll_x, y=scroll_y).release().perform()
        except Exception as e:
            raise e
        
        else:
            return True