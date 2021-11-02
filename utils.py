from browser import ChromeAuto
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utiuls(ChromeAuto):

    def acessar(self, url):
        self.chrome.get(url)


    def espera(self, elemento):
        wait = WebDriverWait(self.chrome, 10)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, elemento)))
        element.click()


