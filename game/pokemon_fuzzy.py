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

lvl_diff['much_low'] = np.array([
    1.0, # -9
    1.0, # -8
    1.0, # -7
    1.0, # -6
    0.5, # -5
    0.0, # -4
    0.0, # -3
    0.0, # -3
    0.0, #  -2
    0.0,#-1
    0.0,#0
    0.0,#1
    0.0,#2
    0.0,#3
    0.0,#4
    0.0,#5
    0.0,#6
    0.0,#7
    0.0,#8
    0.0#9
    ])

lvl_diff['low'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.5, # -6
    1.0, # -5
    1.0, # -4
    1.0, # -3
    1.0, # -3
    0.5, #  -2
    0.0,#-1
    0.0,#0
    0.0,#1
    0.0,#2
    0.0,#3
    0.0,#4
    0.0,#5
    0.0,#6
    0.0,#7
    0.0,#8
    0.0#9
])

lvl_diff['equal'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.0, # -6
    0.0, # -5
    0.0, # -4
    0.0, # -3
    0.0, # -3
    0.5,#  -2
    1.0,# -1
    1.0,#0
    1.0,#1
    0.5,#2
    0.0,#3
    0.0,#4
    0.0,#5
    0.0,#6
    0.0,#7
    0.0,#8
    0.0#9
])

lvl_diff['high'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.0, # -6
    0.0, # -5
    0.0, # -4
    0.0, # -3
    0.0, # -3
    0.0, #  -2
    0.0,#-1
    0.0,#0
    0.5,#1
    1.0,#2
    1.0,#3
    1.0,#4
    1.0,#5
    0.5,#6
    0.0,#7
    0.0,#8
    0.0#9
])

lvl_diff['much_high'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.0, # -6
    0.0, # -5
    0.0, # -4
    0.0, # -3
    0.0, # -3
    0.0, #  -2
    0.0,#-1
    0.0,#0
    0.0,#1
    0.0,#2
    0.0,#3
    0.0,#4
    0.5,#5
    1.0,#6
    1.0,#7
    1.0,#8
    1.0#9
])

#0=imune, 0.25= very_weak, 0.5=fraco, 1.0=neutral, 2.0=strong, 4.0=very_strong
effect['immune'] = fuzz.trapmf(effect.universe, [0, 0, 0, 0.15])
effect['very_weak'] = fuzz.trimf(effect.universe, [0.1, 0.25, 0.45])
effect['weak'] = fuzz.trimf(effect.universe, [0.3, 0.5, 0.8])
effect['neutral'] = fuzz.trimf(effect.universe, [0.7, 1.0, 1.4])
effect['strong'] = fuzz.trimf(effect.universe, [1.2, 2.0, 2.8])
effect['very_strong'] = fuzz.trapmf(effect.universe, [2.5, 3.5, 4.0, 4.0])

probabilidade['very_low'] = fuzz.trapmf(probabilidade.universe, [0, 0, 0.1, 0.25])
probabilidade['low'] = fuzz.trimf(probabilidade.universe, [0.15, 0.3, 0.45])
probabilidade['medium'] = fuzz.trimf(probabilidade.universe, [0.35, 0.5, 0.65])
probabilidade['high'] = fuzz.trimf(probabilidade.universe, [0.55, 0.70, 0.85])
probabilidade['very_high'] = fuzz.trapmf(probabilidade.universe, [0.7, 0.9, 1.0, 1.0])



#immune
rule1 = ctrl.Rule(effect['immune'], probabilidade['very_low'])
#buedafraco 👎
rule2 = ctrl.Rule(effect['very_weak'] & (lvl_diff['much_low']), (probabilidade['very_low']))
rule3 = ctrl.Rule(effect['very_weak'] & lvl_diff['low'], probabilidade['very_low'])
rule4 = ctrl.Rule(effect['very_weak'] & lvl_diff['equal'], probabilidade['very_low'])
rule5 = ctrl.Rule(effect['very_weak'] & lvl_diff['high'], probabilidade['low'])
rule6 = ctrl.Rule(effect['very_weak'] & lvl_diff['much_high'], probabilidade['medium'])

#fraco
rule7 = ctrl.Rule(effect['weak'] & (lvl_diff['much_low']), (probabilidade['very_low']))
rule8 = ctrl.Rule(effect['weak'] & lvl_diff['low'], probabilidade['low'])
rule9 = ctrl.Rule(effect['weak'] & lvl_diff['equal'], probabilidade['low'])
rule10 = ctrl.Rule(effect['weak'] & lvl_diff['high'], probabilidade['medium'])
rule11 = ctrl.Rule(effect['weak'] & lvl_diff['much_high'], probabilidade['medium'])

#neutro
rule12 = ctrl.Rule(effect['neutral'] & (lvl_diff['much_low']), (probabilidade['very_low']))
rule13= ctrl.Rule(effect['neutral'] & lvl_diff['low'], probabilidade['low'])
rule14 = ctrl.Rule(effect['neutral'] & lvl_diff['equal'], probabilidade['medium'])
rule15 = ctrl.Rule(effect['neutral'] & lvl_diff['high'], probabilidade['high'])
rule16 = ctrl.Rule(effect['neutral'] & lvl_diff['much_high'], probabilidade['very_high'])

#LuvaDiNike (strong)
rule17 = ctrl.Rule(effect['strong'] & (lvl_diff['much_low']), (probabilidade['low']))
rule18 = ctrl.Rule(effect['strong'] & lvl_diff['low'], probabilidade['medium'])
rule19 = ctrl.Rule(effect['strong'] & lvl_diff['equal'], probabilidade['high'])
rule20 = ctrl.Rule(effect['strong'] & lvl_diff['high'], probabilidade['very_high'])
rule21 = ctrl.Rule(effect['strong'] & lvl_diff['much_high'], probabilidade['very_high'])

#Mike Tyson (bueda strong)
rule22 = ctrl.Rule(effect['very_strong'] & (lvl_diff['much_low']), (probabilidade['medium']))
rule23 = ctrl.Rule(effect['very_strong'] & lvl_diff['low'], probabilidade['high'])
rule24 = ctrl.Rule(effect['very_strong'] & lvl_diff['equal'], probabilidade['very_high'])
rule25 = ctrl.Rule(effect['very_strong'] & lvl_diff['high'], probabilidade['very_high'])
rule26 = ctrl.Rule(effect['very_strong'] & lvl_diff['much_high'], probabilidade['very_high'])



def calculate_prob(level_input, effect_input):
    lvl_pos = np.where(lvl_diff.universe == level_input)[0][0]
    eff_pos = np.where(effect.universe == effect_input)[0][0]
    
    
    return 1


