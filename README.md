# testedeautomacao
desenvolver teste de automação em um 'ecommerce'
Acessar um site específico, ordenar seus itens do mais barato ao mais caro, adicionar dois itens específicos ao carrinho;
e fazer os passos para finalizar a compra.




# detalhes e técnicas

Automação desenvolvida com Selenium e Python, usando o BDD(Behavior Driven Development ou Desenvolvimento Orientado ao Comportamento)

CONTENDO PAGE OBJECTS E COMO ADICIONAL, GERAÇÃO DE RELATORIO COM O ALLURE RESULTS

O Driver utilizado para automação foi o do google chrome: chromedriver na versão - 94.0.4606.81 (Versão oficial) 64 bits

foi desenvolvido com ambiente virtual venv com as bibliotecas ja instaladas e segue arquivo com requiriments.txt




#observação

'''''''''Caso não veja os itens adicionados, pela velocidade que será adicionado, será gerado um print automaticamente dos produtos para ser visualizado com mais calma posteriormente e ficará na pasta do projeto'''''''''




# como utilizar:
Crie um novo projeto no pycharm para ter um ambiente virtual, venv.
Depois, copie todos os arquivos deste teste de automação para seu novo projeto e execute o seguinte comando:

pip install -r requirements.txt    para instalar os requisitos do sistema

Após o Ambiente configurado corretamente execute este comando:

behave --tags=@compra

(caso as dependencias n sejam instaladas, segue arquivo requiriments.txt com todas que foram utilizadas)



#GERAR RELATÓRIO:

Para gerar o relatório com o Allure Result basta executar os seguintes códigos:

para instalar o allure com behave: pip install allure-behave


executar relatorio do allure:  behave --tags=@compra -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

para ver o relatório: allure serve %allure_result_folder%



