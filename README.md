# Lista com Descritor Circular

## 📋 Descrição

Implementação de uma **Lista Dinâmica com Descritor Circular** em Python. Este TAD (Tipo Abstrato de Dados) utiliza um vetor estático com apontadores circulares para gerenciar inserções e remoções eficientemente em qualquer posição da lista, minimizando movimentações desnecessárias de elementos.

## 🎯 Objetivo

Fornecer uma estrutura de dados que:
- Permite inserção e remoção em qualquer posição (início, meio, fim)
- Utiliza um vetor de tamanho fixo com apontadores (`ini` e `fim`) que circulam
- Otimiza operações ao usar aritimética modular para evitar reorganizações frequentes

## 📁 Estrutura do Projeto

### Arquivos

- **`TAD_DescritorCircular.py`**: Implementação das classes `Descritor` e `ListaComDescritorCircular`
- **`maintrabalho.py`**: Script de teste e demonstração do funcionamento da lista

## 🏗️ Estrutura das Classes

### Classe `Descritor`
Armazena os metadados da lista:
- `ini`: índice do primeiro elemento
- `fim`: índice do último elemento
- `n`: quantidade de elementos na lista
- `max`: capacidade máxima do vetor

### Classe `ListaComDescritorCircular`
Implementa a lista circular com os seguintes métodos:

| Método | Descrição | Parâmetros | Retorno |
|--------|-----------|-----------|---------|
| `vazia()` | Verifica se a lista está vazia | — | bool |
| `cheia()` | Verifica se a lista está cheia | — | bool |
| `insere(dado, posicao)` | Insere elemento na posição especificada | `dado`, `posicao` (1-indexado) | bool |
| `remove(posicao)` | Remove elemento da posição | `posicao` (1-indexado) | bool |
| `consulta(valor)` | Busca posição do valor | `valor` | int (posição ou -1) |
| `acessa(posicao)` | Acessa elemento em posição | `posicao` (1-indexado) | elemento ou None |
| `exibir()` | Imprime todos os elementos | — | — |

## 🚀 Como Usar

### Instalação
Não há dependências externas. Apenas certifique-se de ter Python 3+ instalado.

### Exemplo Básico

```python
from TAD_DescritorCircular import ListaComDescritorCircular

# Criar lista com capacidade para 6 elementos
minha_lista = ListaComDescritorCircular(6)

# Inserir elementos
minha_lista.insere("a", 1)
minha_lista.insere("b", 2)
minha_lista.insere("c", 3)

# Exibir
minha_lista.exibir()  # Lista: a b c

# Remover
minha_lista.remove(1)

# Buscar
posicao = minha_lista.consulta("b")
print(f"Elemento 'b' está na posição: {posicao}")
```

### Executar Testes

```bash
python maintrabalho.py
```

O script demonstra:
1. **Povoamento inicial** com 6 elementos
2. **Geração de espaço** através de remoções
3. **Teste de circularidade** com reinserções
4. **Teste crítico** com múltiplas operações

## 🔄 Funcionamento Circular

A lista utiliza **aritmética modular** (`%`) para criar um comportamento circular:

```
Exemplo com capacidade 6:
ini = 2, fim = 5
Índices lógicos:    1    2    3    4    5    6
Índices físicos:    2    3    4    5    6    0  (wrapping)
```

Isso permite que após remover do início, o espaço seja reutilizado no final sem necessidade de copiar elementos.

## 📊 Complexidade de Tempo

| Operação | Complexidade | Notas |
|----------|-------------|-------|
| Inserção no início | O(1) | Apenas ajusta `ini` |
| Inserção no fim | O(1) | Apenas ajusta `fim` |
| Inserção no meio | O(n) | Requer deslocamento |
| Remoção no início | O(1) | Apenas ajusta `ini` |
| Remoção no fim | O(1) | Apenas ajusta `fim` |
| Remoção no meio | O(n) | Requer deslocamento |
| Busca | O(n) | Busca linear |

## ⚠️ Limitações

- O tamanho do vetor é fixo (definido na criação)
- A lista não pode crescer dinamicamente
- Uma lista cheia não aceita mais inserções

## 🔧 Desenvolvimento

Para adicionar novos métodos, estenda a classe `ListaComDescritorCircular`:

```python
def inverte(self):
    """Inverte a ordem dos elementos da lista"""
    # Implementação aqui
    pass
```

## 📝 Observações Importantes

- As posições são **1-indexadas** (começam em 1)
- Use `_init_` conforme demonstrado na classe (construtor Python)
- O método `acessa()` referencia `self.indice_fisico()` que não está implementado nesta versão

## 👨‍🎓 Contexto Acadêmico

Este projeto é um trabalho acadêmico para a disciplina de **Estruturas de Dados II**, implementando um TAD (Tipo Abstrato de Dados) com foco em otimização de operações em listas sequenciais.

---

**Autor:** Mariana Peres, Isis castro e Maria Lucia Machado  
**Linguagem:** Python 3+  
**Data:** 2026
