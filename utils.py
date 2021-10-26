from browser import ChromeAuto

class Utiuls(ChromeAuto):
    def acessar(self, url):
        self.chrome.get(url)

