from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}
    _login_form = {'by': By.ID, 'value': 'login'}

    def __init__(self, driver):
        # Instaciando Selenium
        self.driver = driver
        self._entrar('http://the-internet.herokuapp.com/login')

        assert self._aparecer(self._login_form)

    def com_(self, username, password):
        self._escrever(self._username_input, username)
        self._escrever(self._password_input, password)
        self._clicar(self._login_button)

    # 2.3 - Ações Realizaveis
    def vejo_mensagem_de_sucesso(self):
        return self._aparecer(self._success_message, 10)

    def vejo_mensagem_de_falha(self):
        return self._aparecer(self._failure_message, 10)

    def testar_login_com_sucesso(self, login):
        login.com_('tomsmith', 'SuperSecretPassword!')
        assert login.vejo_mensagem_de_sucesso()

    def testar_login_com_usuario_invalido(self, login):
        login.com_('asdfgasdfg', 'SuperSecretPassword!')
        assert login.vejo_mensagem_de_falha()

    def testar_login_com_senha_invalida(self, login):
        login.com_('tomsmith', 'xpto12345')
        assert login.vejo_mensagem_de_falha()
