from .page import Page



class HomePage(Page):

    def __init__(self, driver, wait_time: int = 5):
        super().__init__(driver, wait_time)

    
    def click_burger(self, quit = False) -> bool | Exception:
        try:
            get_burger = self.find_element('//*[@resource-id="com.ajaxsystems:id/menuDrawer"]', clickable=True)
            self.click_element(get_burger)
            if quit:
                self.driver.press_keycode(4)
                self.driver.press_keycode(4)
        
        except Exception as e:
            raise e
        
        else:
            return True


    def check_menu_elements(self, xpath) -> bool | Exception:
        try: 
            self.click_burger()
            elem = self.find_element(xpath, clickable=True)
            self.click_element(elem)
            self.driver.press_keycode(4)

        except Exception as e:
            raise e
        
        else:
            return True