from browser import ChromeAuto


class PageElementsOrdenarProdutos(object):
    ELEMENTO_SELECT = '.product_sort_container'
    OPTION_LOW_TO_HIGH = '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]'


class OrdenarProdutos(ChromeAuto):

    def ordenar_produtos_low_to_high(self):
        self.chrome.find_element_by_css_selector(PageElementsOrdenarProdutos.ELEMENTO_SELECT).click()
        self.chrome.find_element_by_xpath(PageElementsOrdenarProdutos.OPTION_LOW_TO_HIGH).click()

