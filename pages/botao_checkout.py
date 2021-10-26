from browser import ChromeAuto



class PageElementsButtonCheckout(object):
    BOTAO_CHECKOUT = '#checkout'


class BotaoCheckout(ChromeAuto):
    def checar_compra(self):
        self.chrome.find_element_by_css_selector(PageElementsButtonCheckout.BOTAO_CHECKOUT).click()