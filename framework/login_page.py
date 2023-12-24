from .page import Page


class LoginPage(Page):
    
    def __init__(self, driver, wait_time: int = 5):
        super().__init__(driver, wait_time)


    def click_login_btn(self) -> bool | Exception:
        try:
            elem = self.find_element('(//*[@resource-id="com.ajaxsystems:id/compose_view"])[1]')
            self.click_element(elem)

            self.find_element('//*[@resource-id="com.ajaxsystems:id/content"]')
        except Exception as e:
            raise e

        else:
            return True
        

    def login_to_ajax(self, email_: str, password_: str) -> bool | Exception:
        try:
            email = self.find_element('(//*[@resource-id="defaultAutomationId"])[1]')
            password = self.find_element('(//*[@resource-id="defaultAutomationId"])[2]')

            email.clear()
            email.send_keys(email_)

            password.clear()
            password.send_keys(password_)

            # submit login
            self.find_element('(//*[@resource-id="com.ajaxsystems:id/compose_view"])[4]', clickable=True).click()
            
            # check for loading home page
            home_page = self.find_element('//*[@resource-id="com.ajaxsystems:id/noHubs"]')
        except Exception as e:
            return e
        
        else:
            if home_page: 
                return True
            else:
                return False

    def exit_(self):
        try:
            # burger button
            self.click_element(self.find_element('//*[@resource-id="com.ajaxsystems:id/menuDrawer"]', clickable=True))
            
            # setting section
            self.click_element(self.find_element('//*[@resource-id="com.ajaxsystems:id/settings"]', clickable=True))
            
            # scroll to end page
            self.scroll(self.find_element('//*[@resource-id="com.ajaxsystems:id/items"]'), 0, 0)

            # exit button
            self.click_element(self.find_element('(//*[@resource-id="com.ajaxsystems:id/compose_view"])[6]', clickable=True))

            # wait for login/sign page 
            self.find_element('//*[@resource-id="com.ajaxsystems:id/root"]')
        except Exception as e:
            raise e
        
        else: 
            return True