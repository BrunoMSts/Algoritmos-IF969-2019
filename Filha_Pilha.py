class No:
    def __init__(self, dado):
        self.dado = dado
        self.abaixo = None
        self.prox = None

class fila:
    def __init__(self):
        pass

    class Pilha:
        def __init__(self, elem=None):
            self.topo = elem
            self.tamanho = 0

        def empilha(self, elem):
            ponteiro = No(elem)
            ponteiro.abaixo = self.topo
            self.topo = ponteiro
            self.tamanho += 1

        def desempilha(self):
            if self.tamanho > 0:
                ponteiro = self.topo
                self.topo = ponteiro.abaixo
                self.tamanho -= 1
            else:
                raise IndexError('Pilha Vazia')

        def top(self):
            if self.tamanho > 0:
                return self.topo.dado
            raise IndexError('Pilha Vazia')

        def __repr__(self):
            ponteiro = self.topo
            string = ''
            while ponteiro:
                string += str(ponteiro.dado) + '\n'
                ponteiro = ponteiro.abaixo
            return string

        def __str__(self):
            return self.__repr__()

    class Fila:
        def __init__(self):
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0

        def inserir(self, elem):
            ponteiro = No(elem)
            if self.ultimo == None:
                self.ultimo = ponteiro
            else:
                self.ultimo.prox = ponteiro
                self.ultimo = ponteiro
            if self.primeiro == None:
                self.primeiro = ponteiro
            self.tamanho += 1
        def exluir(self):
            if self.tamanho > 0:
                self.primeiro = self.primeiro.prox
                self.tamanho -= 1 
            else:
                raise IndexError('Fila Vazia')

        def tam(self):
            return self.tamanho
        def peek(self):
            if self.tamanho > 0:
                return self.primeiro.dado

        def __repr__(self):
            string = ''
            ponteiro = self.primeiro
            while ponteiro:
                string += str(ponteiro.dado) + '<-' 
                ponteiro = ponteiro.prox
            return string
        def __str__(self):
            return self.__repr__()