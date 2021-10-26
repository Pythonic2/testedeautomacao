# language: pt

  Funcionalidade: Fluxo de compra no ecommerce

    @compra
    Cenário: Realizar compra no ecomerce
      Dado que acesso o site do saucedemo / swaglabs
      E preencho informações de Login
      E clico no botão Login
      E ordeno os itens de low to high (menor preço para maior preço)
      E escolho os itens a serem comprados
      E clico no icon do carrinho
      E clico click no botão checkout
      E preencho as informações pessoas necessárias para finalização da compra
      Quando clico no botão FINISH
      Então devo visualizar a pagina CHECKOUT: COMPLETE! dizendo que o pedido foi enviado

