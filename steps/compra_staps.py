from behave import given, when, then

from utils import Utiuls
from pages.login_page import LoginPage
from pages.ordenar_produtos import OrdenarProdutos
from pages.escolher_produtos import EscolherProdutos
from pages.header_carrinho_de_compras import CarrinhoCompas
from pages.botao_checkout import BotaoCheckout
from pages.suas_informacoes_checkout import CheckoutInformacoes
from pages.checkout_final import CheckoutFinal
from pages.comprafinalizada_checkout_finalizado import CompraFinalizada
from nose.tools import assert_equal
utils = Utiuls()
login_page = LoginPage()
ordenar_produtos = OrdenarProdutos()
escolher_produtos = EscolherProdutos()
header_carrinho_de_compras = CarrinhoCompas()
botao_checkout = BotaoCheckout()
suas_informacoes_checkout = CheckoutInformacoes()
checkout_final = CheckoutFinal()
comprafinalizada_checkout_finalizado = CompraFinalizada()


@given(u'que acesso o site do saucedemo / swaglabs')
def step_impl(context):
    utils.acessar('https://www.saucedemo.com/')

@given(u'preencho informações de Login')
def step_impl(context):
    login_page.preencher_login('')


@given(u'clico no botão Login')
def step_impl(context):
    login_page.clicar_login()


@given(u'ordeno os itens de low to high (menor preço para maior preço)')
def step_impl(context):
    ordenar_produtos.ordenar_produtos_low_to_high()

@given(u'escolho os itens a serem comprados')
def step_impl(context):
    escolher_produtos.adicionar_produtos_ao_carrinho()


@given(u'clico no icon do carrinho')
def step_impl(context):
    header_carrinho_de_compras.clicar_carrinho_compras()



@given(u'clico click no botão checkout')
def step_impl(context):
    botao_checkout.checar_compra()


@given(u'preencho as informações pessoas necessárias para finalização da compra')
def step_impl(context):
    suas_informacoes_checkout.preencherinformacoes()


@when(u'clico no botão FINISH')
def step_impl(context):
    checkout_final.finalizar_compras()


@then(u'devo visualizar a pagina CHECKOUT: COMPLETE! dizendo que o pedido foi enviado')
def step_impl(context):
    assert_equal(comprafinalizada_checkout_finalizado.comprafinalizadacomsucesso(),'THANK YOU FOR YOUR ORDER')