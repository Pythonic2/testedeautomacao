from browser import ChromeAuto

from time import sleep


class PageCompraFinalizadaElements(object):
    titulo_h2 = 'h2'


class CompraFinalizada(ChromeAuto):
    def comprafinalizadacomsucesso(self):
        sleep(3)
        verificar = self.chrome.find_element_by_tag_name(PageCompraFinalizadaElements.titulo_h2).text
        self.chrome.quit()
        return verificar
