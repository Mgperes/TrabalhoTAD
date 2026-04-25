from TAD_DescritorCircular import ListaComDescritorCircular

#Povoamento inicial
minha_lista = ListaComDescritorCircular(6)
minha_lista.insere("a", 1)
minha_lista.insere("b", 2)
minha_lista.insere("c", 3)
minha_lista.insere("d", 4)
minha_lista.insere("e", 5)
minha_lista.insere("f", 6)
#---------------------------

print("\nini:", minha_lista.desc.ini)
print("fim:", minha_lista.desc.fim)
print("vetor:", minha_lista.vetor)

#Geração de Espaço ----------------
minha_lista.remove(1)
minha_lista.remove(1)
#----------------------------------

print("\nini:", minha_lista.desc.ini)
print("fim:", minha_lista.desc.fim)
print("vetor:", minha_lista.vetor)

#Teste de Circularidade -----------
minha_lista.insere("a", 5)

print("\nini:", minha_lista.desc.ini)
print("fim:", minha_lista.desc.fim)
print("vetor:", minha_lista.vetor)
#----------------------------------

#Teste Crítico
minha_lista.insere("X", 3)

print("\nini:", minha_lista.desc.ini)
print("fim:", minha_lista.desc.fim)
print("vetor:", minha_lista.vetor)