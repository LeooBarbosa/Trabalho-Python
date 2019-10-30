class Ufc:
    def __init__(self, edicao):
        self.edicao = edicao
        self.lutadores = []
        self.pesoMosca = []
        self.pesoGalo = []
        self.pesoLeve = []
        self.pesoMedio = []
        self.pesoMeioMedio = []
        self.pesoMeioPesado = []
        self.pesoPesado = []
        self.pesoPalha = []
        self.pesoPena = []

    def cadastrar_lutador(self, nome, idade, sexo, peso, paisOrigem, categoria):

        lutador = [nome, idade, sexo, peso, paisOrigem, categoria]

        if categoria == 1:
            self.pesoPalha.append(lutador)

        elif categoria == 2:
            self.pesoMosca.append(lutador)
        
        elif categoria == 3:
            self.pesoGalo.append(lutador)

        elif categoria == 4:
            self.pesoPena.append(lutador)

        elif categoria == 5:
            self.pesoLeve.append(lutador)

        elif categoria == 6:
            self.pesoMeioMedio.append(lutador)
        
        elif categoria == 7:
            self.pesoMedio.append(lutador)

        elif categoria == 8:
            self.pesoMeioPesado.append(lutador)

        elif categoria == 9:
            self.pesoPesado.append(lutador)
        

        self.lutadores.append(lutador)

        print('Lutador: {} cadastrado' .format(lutador))

    def listar_lutadores(self):
        print('Lutadores cadastrados: {}' .format(self.lutadores))
        print('Lutadores Peso Leve: {}' .format(self.pesoLeve))
        print('Lutadores Peso Pena: {}' .format(self.pesoPena))
        print('Lutadores Peso Galo: {}' .format(self.pesoGalo))
        print('Lutadores Peso Mosca: {}' .format(self.pesoMosca))
        print('Lutadores Peso Palha: {}' .format(self.pesoPalha))
        print('Lutadores Peso Medio: {}' .format(self.pesoMedio))
        print('Lutadores Peso Meio-Pesado: {}' .format(self.pesoMeioPesado))
        print('Lutadores Peso Pesado: {}' .format(self.pesoPesado))
