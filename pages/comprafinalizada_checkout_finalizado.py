from browser import ChromeAuto


class PageCompraFinalizadaElements(object):

    titulo_h2 = 'h2'


class CompraFinalizada(ChromeAuto):

    def comprafinalizadacomsucesso(self):
        try:
            verificar = self.chrome.find_element_by_tag_name(PageCompraFinalizadaElements.titulo_h2).text
            self.chrome.quit()
        except:
            print('Compra Não Finalizada')

        return verificar


