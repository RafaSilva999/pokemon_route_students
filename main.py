from game import pokemon_fuzzy
from game.pokemon_game import PokemonGame
from gui.pokemon_gui import PokemonGUI
from gui.starter_gui import StarterGUI

def main():

    starter_gui = StarterGUI()
    starter = starter_gui.run()

    if starter is None:
        return
    prolog_file="prolog/pokemon_game.pl"
        
    gui = PokemonGUI(
        prolog_file=prolog_file,
        starter_id=starter
    )

    #teste do fuzzy
    prob_pior=pokemon_fuzzy.calculate_prob(level_input=-8, effect_input=0.0)
    print(f"Probabilidade de derrota total: {prob_pior:.2f}")

    prob_neutral=pokemon_fuzzy.calculate_prob(level_input=0, effect_input=1.0)
    print(f"Probabilidade de resultado neutro: {prob_neutral:.2f}")

    prob_melhor=pokemon_fuzzy.calculate_prob(level_input=8, effect_input=4.0)
    print(f"Probabilidade de vitória total: {prob_melhor:.2f}")

    print("-----------""")

    game = PokemonGame(
        prolog_file=prolog_file,
        starter_id=starter
    )

    # Start stepwise game + GUI updates
    gui.start_game(game, delay=800)

    gui.run()


if __name__ == "__main__":
    main()