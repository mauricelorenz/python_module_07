#!/usr/bin/env python3

from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")
    game_engine = GameEngine()
    card_factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine.configure_engine(card_factory, strategy)
    print(f"Factory: {type(game_engine.factory).__name__}")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Available types: {game_engine.factory.get_supported_types()}")
    print("\nSimulating aggressive turn...")
    action_result = game_engine.simulate_turn()
    print(f"Hand: {[f"{card.name} ({card.cost})"
                    for card in game_engine.hand]}")
    print("\nTurn execution:")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    print(f"Actions: {action_result}")
    print("\nGame Report:")
    print(f"{game_engine.get_engine_status()}")
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
