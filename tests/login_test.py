import os
import time

import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def login(request):
    _chromedriver = 'F:/TesteAutomacao/Iterays/TestesWEB/FTS-132_heroku_login/vendor/chromedriver.exe'

    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        driver_ = webdriver.Chrome()

    loginPage = LoginPage(driver_)

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return loginPage


def testar_login_com_sucesso(login):
    login.com_('tomsmith', 'SuperSecretPassword!')
    assert login.vejo_mensagem_de_sucesso()


def testar_login_com_usuario_invalido(login):
    login.com_('asdfgasdfg', 'SuperSecretPassword!')
    assert login.vejo_mensagem_de_falha()


def testar_login_com_senha_invalida(login):
    login.com_('tomsmith', 'xpto12345')
    assert login.vejo_mensagem_de_falha()
