from browser import ChromeAuto
from time import sleep


class PageElementsFormulatioPessoal(object):
    FIRST_NAME = 'first-name'
    LAST_NAME = 'last-name'
    POSTAL_CODE = 'postal-code'
    BTN_CONTINUE = 'continue'


class CheckoutInformacoes(ChromeAuto):
    def preencherinformacoes(self):
        self.chrome.find_element_by_id(PageElementsFormulatioPessoal.FIRST_NAME).send_keys('Igor')
        self.chrome.find_element_by_id(PageElementsFormulatioPessoal.LAST_NAME).send_keys('Sensinha')
        self.chrome.find_element_by_id(PageElementsFormulatioPessoal.POSTAL_CODE).send_keys('58074115')
        sleep(2)
        self.chrome.find_element_by_id(PageElementsFormulatioPessoal.BTN_CONTINUE).click()