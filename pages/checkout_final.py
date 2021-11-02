from browser import ChromeAuto


class PageCheckoutsElements(object):
    BOTAO_FINISH = 'finish'


class CheckoutFinal(ChromeAuto):

    def finalizar_compras(self):
        # gerar tabelas com os dados? será que vao achar que foi além da conta?

        self.chrome.save_screenshot('produtos.png')

        self.chrome.find_element_by_id(PageCheckoutsElements.BOTAO_FINISH).click()