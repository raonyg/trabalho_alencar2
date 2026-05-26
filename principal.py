'''DOCSTRING
O programa tem como objetivo criar um sistema de votação, onde o usuário pode cadastrar candidatos ou qualquer coisa que se possa fazer uma fotação,dar nome a votação, votar e ver o resultado. O programa é dividido em 4 opções: cadastro de candidatos, lista de candidatos, votação e resultado. O programa utiliza uma lista para armazenar os candidatos em um arquivo chamado x.txt, sendo x o nome que o usuário dar para a votação, onde cada candidato é representado por uma sublista contendo o nome, número e quantidade de votos. O programa utiliza um loop para exibir o menu e processar as opções escolhidas pelo usuário. O programa também possui uma opção para encerrar o sistema.
'''

#estrutura de repetição que irá repetir todo o programa até digitar 0 e encerrar
while True:

    print('\n{:_^40}'.format('VOTAÇÃO'))

    opcao=input(
    '{:_^40} \n''1-Cadastrar candidato \t''2-Lista de candidatos \n''3-Votar \t''4-Resultado \n''0-Fechar o Programa \n''{:=^40}\n''digite sua opção: '.format('comandos','='))
# verificando se irá pedir um comentario 