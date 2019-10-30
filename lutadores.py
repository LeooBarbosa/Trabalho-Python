from ufc import Ufc

ufc = Ufc("Ufc 654")
print(' --- UFC  ---')
print(' --- MENU ---')
print('1 - Cadastrar Lutadores')
print('2 - Listar usuários')


opcao = int(input('Digite uma opcao: '))

if opcao == 2:
    print('Impossivel listar lutadores inexistentes')
    exit()

if opcao == 1:
    contador = 1
    quantidade = int(input('Deseja cadastrar quantos lutadores?: '))
    while contador <= quantidade:
        sexo = int(input('Digite o sexo do lutador(a):\n [1]Feminino\n [2]Masculino\n '))

        if sexo == 1:
            print('Categorias de peso femininos:\n [1] - Peso Palha\n [2] - Peso Mosca\n [3] - Peso Galo\n [4] - Peso Pena')
            categoria = int(input('Informe qual sua categoria: '))
            nome = input('Digite o nome do lutador(a): ')
            idade = int(input('Digite a idade do lutador(a): '))
            peso = input('Digite o peso do lutador(a): ')
            pais = input('Digite o pais de nacionalidade do lutador(a): ')
            ufc.cadastrar_lutador(nome, idade, sexo, peso, pais, categoria)

        elif sexo == 2:
            print('Categorias de peso masculinos:\n [5] - Peso Leve\n [6] - Peso Meio-Médio\n [7] - Peso Médio\n [8] - Peso Meio-Pesado\n [9] - Peso Pesado ')
            categoria = int(input('Informe qual sua categoria: '))
            nome = input('Digite o nome do lutador(a): ')
            idade = int(input('Digite a idade do lutador(a): '))
            peso = input('Digite o peso do lutador(a): ')
            pais = input('Digite o pais de nacionalidade do lutador(a): ')
            ufc.cadastrar_lutador(nome, idade, sexo, peso, pais, categoria)

        contador = contador + 1

print(' --- UFC  ---')
print(' --- MENU ---')
print('2 - Listar usuários')

opcao = int(input('Digite uma opcao: '))

if opcao == 2:
    ufc.listar_lutadores()

