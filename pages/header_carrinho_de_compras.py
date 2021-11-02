from browser import ChromeAuto
from utils import Utiuls

utils = Utiuls()


class HeaderPageElements(object):
    CARRINHO_COMPRAS = '.shopping_cart_link'


class CarrinhoCompas(ChromeAuto):
    def clicar_carrinho_compras(self):
        utils.espera(HeaderPageElements.CARRINHO_COMPRAS)
        self.chrome.find_element_by_css_selector(HeaderPageElements.CARRINHO_COMPRAS).click()
