

f=[]

#estrutura de repetição que irá repetir todo o programa até digitar 0 e encerrar
while True:

    print('\n{:_^40}'.format('VOTAÇÃO'))

    opcao=input(
    '{:_^40} \n''1-Cadastrar candidato \t''2-Lista de candidatos \n''3-Votar \t''4-Resultado \n''0-Fechar o Programa \n''=============\n''digite sua opção: '.format('comandos').title())


#caso digite 0 o programa será encerrado
    if opcao=='0':
        print('encerrando..'.title())
        break

#cadastro de candidatos
    elif opcao=='1':

        print('===cadastro de candidato==='.title())

        nome=input('digite o nome do candidato: '.title())
        numero=int(input('digite o número do candidato: '.title()))


#cada candidato tem:
#nome,número,votos
        f.append([nome,numero,0])

        print('candidato cadastrado com sucesso!!!'.title())

#lista de candidatos
    elif opcao== '2':

        print('===lista de candidatos==='.title())

        print(f'{"Nome":<15}{"Número"}')

#mostra todos os candidatos
        for candidato in f:

            print(f'{candidato[0]:<15}{candidato[1]}')

#votação
    elif opcao=='3':

        print('===votação==='.title())

        voto=int(input('digite o número do candidato: '.title()))
        for candidato in f:

#se encontrar o número digitado ele soma +1 voto
            if candidato[1]==voto:

                candidato[2]+=1

                print('voto computado!'.title())
                break
#resultado
    elif opcao=='4':

        print('===resultado==='.title())

        print(f'{"Nome":<15}{"Votos"}')


#nome e a quantidade de votos
        for candidato in f:

            print(f'{candidato[0]:<15}{candidato[2]}')

#opção inválida
    else :
        print('opção inválida!!!'.title())