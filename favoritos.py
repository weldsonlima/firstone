#!/Library/Frameworks/Python.framework/Versions/3.6/bin/env python3.6
# _*_ coding: utf-8 _*_
'''
Created on 14 de out de 2018
Pense em Python - Cap 09
@author: weldson lima
'''
class ativfav():
    def __init__(self, categoria, atividades):
        """Inicializa os atributos"""
        self.categoria = categoria
        self.atividades = atividades
    
    def busca_ativfav(self, lista):
        lazeres = [lazer.title() for lazer in lista if lazer.title() in self.atividades]
        return lazeres
    
    def mostra_ativfav(self):
        if len(self.atividades) != 0:
            for item in self.atividades:
                if self.atividades.index(item) == 0:
                    print("Na categoria %s, suas atividades favoritas são: %s" % (self.categoria, item), end="")
                elif self.atividades.index(item) == (len(self.atividades)-1):
                    print(" e %s" %item, end="")
                else:
                    print(", %s" %item, end="")
            print(".")
        else:
            print("Você não gosta de nada da categoria %s." %(self.categoria))        
 