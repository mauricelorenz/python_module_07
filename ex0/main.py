#!/usr/bin/env python3

from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    fire_dragon_args = {"name": "Fire Dragon", "cost": 5,
                        "rarity": "Legendary", "attack": 7, "health": 5}
    fire_dragon = CreatureCard(**fire_dragon_args)
    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")
    print(f"Play result: {fire_dragon.play({})}")
    print("\nFire Dragon attacks Goblin Warrior:")
    goblin_warrior_args = {"name": "Goblin Warrior", "cost": 5,
                           "rarity": "Legendary", "attack": 7, "health": 5}
    goblin_warrior = CreatureCard(**goblin_warrior_args)
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
