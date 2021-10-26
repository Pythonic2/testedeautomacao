from browser import ChromeAuto


class PageElementsFormularioLogin(object):
    INPUT_USER_NAME = 'user-name'
    INPUT_PASSWORD = '#password'
    BTN_LOGIN = "#login-button"


class LoginPage(ChromeAuto):

    def preencher_login(self, separafrase):
        #buscar os elementos dentro do login

        for users in self.chrome.find_elements_by_id('login_credentials'):
            usuarios = users.text
        # como todos são apenas um separar eles para virarem lista para poder trabalhar com cada um isoladamente
        #caos eu precise

        nome = usuarios
        nomedeusuario = nome.split()  # quando eu separo ele pega cada espaço e torna um item de lista

        #removendo da lista itens desnecessários
        for i in range(3):
            del nomedeusuario[0]
        

        #enviar no campo usuario o primeiro indice da lista
        self.chrome.find_element_by_id(PageElementsFormularioLogin.INPUT_USER_NAME).send_keys(nomedeusuario[0])

        # agr fazer a mesma coisa para o campo de password

        # como só há uma senha, então n precisa fazer lista ou coisas parecidas
        self.chrome.find_element_by_css_selector(PageElementsFormularioLogin.INPUT_PASSWORD).send_keys('secret_sauce')


    def clicar_login(self):
        self.chrome.find_element_by_css_selector(PageElementsFormularioLogin.BTN_LOGIN).click()
