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
probabilidade = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'probabilidade')


#lvl_diff["much_low"] = fuzz.trapmf(lvl_diff.universe, [-9, -9, -6, -4])
lvl_diff['much_low'] = np.array([
    1.0, # -9
    1.0, # -8
    1.0, # -7
    1.0, # -6
    0.5, # -5
    0.0, # -4
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

#lvl_diff['low'] = fuzz.trapmf(lvl_diff.universe, [-7, -5, -3, -1])
lvl_diff['low'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.5, # -6
    1.0, # -5
    1.0, # -4
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

#lvl_diff['equal'] = fuzz.trapmf(lvl_diff.universe, [-3, -1, 1, 3])
lvl_diff['equal'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.0, # -6
    0.0, # -5
    0.0, # -4
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

#lvl_diff['high'] = fuzz.trapmf(lvl_diff.universe, [0, 2, 5, 7])
lvl_diff['high'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.0, # -6
    0.0, # -5
    0.0, # -4
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

#lvl_diff['much_high'] = fuzz.trapmf(lvl_diff.universe, [4, 6, 9, 9])
lvl_diff['much_high'] = np.array([
    0.0, # -9
    0.0, # -8
    0.0, # -7
    0.0, # -6
    0.0, # -5
    0.0, # -4
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
probabilidade['very_high'] = fuzz.trapmf(probabilidade.universe, [0.7, 0.9, 1.0, 1.0])   #/---



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

rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26]



def calculate_prob(level_input, effect_input):
    #p1
    lvl_pos = np.where(lvl_diff.universe == level_input)[0][0]
    eff_pos = np.where(effect.universe == effect_input)[0][0]

    #p2
    lvls_diffs = {
        label: lvl_diff[label].mf[lvl_pos]
        for label in ['much_low', 'low', 'equal', 'high', 'much_high']
    }
    effects = {
        label: effect[label].mf[eff_pos]
        for label in ['immune', 'very_weak', 'weak', 'neutral', 'strong', 'very_strong']
    }

    #p3 e p4
    aggregated = np.zeros_like(probabilidade.universe)
    for rule in rules:
        conditions = rule.antecedent_terms
        conclusion = rule.consequent[0].term

        membership = []
        for term in conditions:
            var_label  = term.parent.label
            term_label = term.label
            if var_label == 'lvl_diff':
                membership.append(lvls_diffs[term_label])
            else:
                membership.append(effects[term_label])
        rule_strength = min(membership) if membership else 0.0
 
        if rule_strength > 0:
            contribution = np.fmin(rule_strength, conclusion.mf)
            aggregated = np.fmax(aggregated, contribution)
 
    #5
    if np.sum(aggregated) == 0:
        return 0.5
 
    result = fuzz.defuzz(probabilidade.universe, aggregated, 'centroid')
    return float(np.clip(result, 0.0, 1.0))
    
    """
    try:
        lvl_pos= np.where(lvl_diff.universe == level_input)[0][0]
        effect_pos = np.where(effect.universe == effect_input)[0][0]
    except Exception as e:
        print(f"Error calculating probability: {e}")
        return 0.5
    prob_ctrl = ctrl.ControlSystemSimulation(rules)
    prob_ctrl.input['lvl_diff'] = level_input
    prob_ctrl.input['effect'] = effect_input
    
    prob_ctrl.compute()
    print(f"Calculated probability: {prob_ctrl.output['probabilidade']:.2f}")
    return float(prob_ctrl.output['probabilidade'])
    """


