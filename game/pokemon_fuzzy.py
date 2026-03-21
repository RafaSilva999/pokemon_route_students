import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Cria um sistema Fuzzy que recebe como input a diferença dos niveis
e o efeito do ataque e devolve como input a probabilidade de ganhar
'''
#Antecedentes
lvl_diff = ctrl.Antecedent(np.arange(-9, 10, 1), 'lvl_diff')
effect = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'effect')

#Consequent
probabilidade = ctrl.Consequent(np.arange(0, 1.0, 0.01), 'probabilidade')



def calculate_prob(level_input, effect_input):
    return 1
    


