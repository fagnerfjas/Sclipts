# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:51:08 2016

@author: fjas
"""
from random import *
from math import *
from scipy.stats import expon
from scipy.stats import poisson


## VARIAVEIS E FUNCOES ------------------------------

liga = ['A', 'B', 'C', 'D', 'E']
atende = ['F', 'G', 'H', 'I', 'J']
canais = [1, 2, 3]
contador = 0
bloqueio = 0
ligacoesfeitas = 0
tempo_entre_chamadas = 0
max_chamadas = 2000
matriz_ocupacao = {1: 'livre', 2: 'livre', 3: 'livre'}


def nosLivres( matriz ):
    nosOcupados = []
    for i in matriz:
        if matriz[i]!='livre':
            nosOcupados.append(matriz[i]['nos'][0])
            nosOcupados.append(matriz[i]['nos'][1])
    shuffle(liga)
    shuffle(atende)
    for a in liga:
        if a not in nosOcupados:
            break
    for b in atende:
        if b not in nosOcupados:
            break    
    return [a, b]


def criaLigacao(nos):
    ligacao = {
    'nos': nos,
    'duracaoChacamada':expon.rvs(loc=2, scale=2),
    'tempoEntreChamadas':poisson.rvs(1)
    }
    return ligacao


def canalLivre(matriz):
    for canal in matriz:
        if matriz[canal] == 'livre':
            return canal
    return 0

def decrementaTempo(matriz):
    for canal in matriz:
        if matriz[canal]!='livre':
            if matriz[canal]['duracaoChacamada'] < 1:
                matriz[canal] = 'livre'
            else:
                matriz[canal]['duracaoChacamada'] = matriz[canal]['duracaoChacamada'] - 1
    
    
while( contador < max_chamadas ):
    
    if( tempo_entre_chamadas == 0 ):        
        decrementaTempo( matriz_ocupacao )
        contador = contador + 1
        canal = canalLivre(matriz_ocupacao)

        if canalLivre( matriz_ocupacao ) > 0:
            ligacao = criaLigacao( nosLivres(matriz_ocupacao) )
            matriz_ocupacao[canal] = ligacao
            ligacoesfeitas = ligacoesfeitas+1
        else:
            bloqueio = bloqueio + 1    
    
print 'bloqueios:', bloqueio
print 'countador:', contador
print 'ligacoes feitas', ligacoesfeitas
print 'matriz ocupacao: \n', matriz_ocupacao