# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:38:06 2013

Jogo da Vida

@author: ---
"""

class V(object):
  pass

class M(object):
  pass

def passo_vida(tabuleiro):
  return [[M]]

class TestPassoVida(object): # unittes.TestCase
  
  def test_uma_celula(self):
    assert passo_vida([[V]]) ==  [[M]]
