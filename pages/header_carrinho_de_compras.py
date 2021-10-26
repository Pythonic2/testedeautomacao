from browser import ChromeAuto
from time import sleep


class HeaderPageElements(object):
    CARRINHO_COMPRAS = '.shopping_cart_link'


class CarrinhoCompas(ChromeAuto):
    def clicar_carrinho_compras(self):
        sleep(2)
        self.chrome.find_element_by_css_selector(HeaderPageElements.CARRINHO_COMPRAS).click()

