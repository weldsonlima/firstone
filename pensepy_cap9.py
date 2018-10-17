#!/Library/Frameworks/Python.framework/Versions/3.6/bin/env python3.6
# _*_ coding: utf-8 _*_
'''
Created on 14 de outubro de 2018
Pense em Python - Cap 09
@author: weldson lima
'''
import favoritos

def remove_pontuacao(lista):
    pontuacao = (".", ",", "!", "?", ":")
    lista_limpa = []
    for i in range(len(lista)):
        if lista[i][-1:] in pontuacao:
            lista_limpa.append(lista[i][:-1])
        else:
            lista_limpa.append(lista[i])
    return lista_limpa

def imprime_lista(lista):
    if len(lista) != 0:
        for item in lista:
            if lista.index(item) == 0:
                print("Sim, você ama %s" %(item), end="")
            elif lista.index(item) == (len(lista)-1):
                print(" e %s" %item, end="")
            else:
                print(", %s" %item, end="")
        print(".")
    else:
        print("Você não gosta muito disso.")
    
meus_esportes = favoritos.ativfav("Esportes", ("Natação", "Musculação", "Crossfit"))
meus_series = favoritos.ativfav("Séries", ("WalkingDead", "TheDeuce"))
meus_lugares = favoritos.ativfav("Lugares", ("Brasília", "PortoAlegre", "Natal"))

meus_esportes.mostra_ativfav()
meus_series.mostra_ativfav()
meus_lugares.mostra_ativfav()

#lista = input("O que você vai fazer?\n").split()
#lista_usr = remove_pontuacao(lista)
#imprime_lista(lista_usr)

 
#palavras = [palavra.title() for palavra in lista if isinstance(palavra, str)] # List Comprehension
#Depois do Crossfit vou correr em Brasília ouvindo um podcast sobre Python
#Vou comer torta no café da manhã
#Depois do Crossfit vou: correr, Brasília, podcast e Python.