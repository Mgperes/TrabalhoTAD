class Descritor:
    def _init_(self, capacidade):
        self.ini = 0
        self.fim = -1
        self.n = 0
        self.max = capacidade

class ListaComDescritorCircular:
    def _init_(self, capacidade):
        self.vetor = [None] * capacidade
        self.desc = Descritor(capacidade)

    def vazia(self):
        return self.desc.n == 0

    def cheia(self):
        return self.desc.n == self.desc.max
    
    def insere(self, dado, posicao):
        if self.cheia() or posicao < 1 or posicao > self.desc.n + 1:
            return False
        
        if posicao == self.desc.n + 1:
            self.desc.fim = (self.desc.fim + 1) % self.desc.max
            self.vetor[self.desc.fim] = dado

        # Inserção no início
        elif posicao == 1:
            self.desc.ini = (self.desc.ini - 1) % self.desc.max
            self.vetor[self.desc.ini] = dado

        # Inserção no meio
        else:
            i = self.desc.fim
            novo_fim = (self.desc.fim + 1) % self.desc.max

            while i != (self.desc.ini + posicao - 2) % self.desc.max:
                prox = (i + 1) % self.desc.max
                self.vetor[prox] = self.vetor[i]
                i = (i - 1) % self.desc.max

            indice = (self.desc.ini + posicao - 1) % self.desc.max
            self.vetor[indice] = dado
            self.desc.fim = novo_fim

        self.desc.n += 1
        return True

    def remove(self, posicao):
        if self.vazia() or posicao < 1 or posicao > self.desc.n:
            return False
        
        if posicao == 1:
            self.vetor[self.desc.ini] = None
            self.desc.ini = (self.desc.ini + 1) % self.desc.max

        # remover fim
        elif posicao == self.desc.n:
            self.vetor[self.desc.fim] = None
            self.desc.fim = (self.desc.fim - 1) % self.desc.max

        # remover meio
        else:
            i = (self.desc.ini + posicao - 1) % self.desc.max

            while i != self.desc.fim:
                prox = (i + 1) % self.desc.max
                self.vetor[i] = self.vetor[prox]
                i = prox

            self.vetor[self.desc.fim] = None
            self.desc.fim = (self.desc.fim - 1) % self.desc.max

        self.desc.n -= 1

        if self.desc.n == 0:
            self.desc.ini = 0
            self.desc.fim = -1

        return True

    def consulta(self, valor):
        i = self.desc.ini
        for pos in range(1, self.desc.n + 1):
            if self.vetor[i] == valor:
                return pos
            i = (i + 1) % self.desc.max
        return -1

    def acessa(self, posicao):
        if posicao < 1 or posicao > self.desc.n:
            return None
        return self.vetor[self.indice_fisico(posicao)]
    
    def exibir(self):
        if self.vazia():
            print("Lista vazia!")
            return
        
        i = self.desc.ini
        print("Lista: ")

        for _ in range(self.desc.n):
            print(self.vetor[i], end= " ")
            i = (i + 1) % self.desc.max

        print()