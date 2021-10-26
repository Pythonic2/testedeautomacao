from browser import ChromeAuto



class PageProdutosElements(object):
    ITENS = '.inventory_item_name'
    TITULO_ITEM1 = 'Sauce Labs Onesie'
    BOTAO_ADD_AO_CARRINHO = "#add-to-cart-sauce-labs-onesie"

    TITULO_ITEM2 = 'Test.allTheThings() T-Shirt (Red)'
    BOTAO_ADD_AO_CARRINHO2 = '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'


class EscolherProdutos(ChromeAuto):

    def adicionar_produtos_ao_carrinho(self):
        for itens in self.chrome.find_elements_by_css_selector(PageProdutosElements.ITENS):
            if itens.text == PageProdutosElements.TITULO_ITEM1:
                self.chrome.find_element_by_css_selector(PageProdutosElements.BOTAO_ADD_AO_CARRINHO).click()
            elif itens.text ==PageProdutosElements.TITULO_ITEM2:
                self.chrome.find_element_by_xpath(PageProdutosElements.BOTAO_ADD_AO_CARRINHO2).click()

