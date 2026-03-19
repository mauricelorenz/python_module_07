#!/usr/bin/env python3

from ex0.Card import Card
from .EliteCard import EliteCard
from .Combatable import Combatable
from .Magical import Magical


def main() -> None:
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    card = [method for method in Card.__dict__.keys()
            if not method.startswith("_")]
    print(f"- Card: {card}")
    combatable = [method for method in Combatable.__dict__.keys()
                  if not method.startswith("_")]
    print(f"- Combatable: {combatable}")
    magical = [method for method in Magical.__dict__.keys()
               if not method.startswith("_")]
    print(f"- Magical: {magical}")
    arcane_warrior = EliteCard("Arcane Warrior", 5, "Rare", 5, 3, 4)
    enemy = EliteCard("Enemy", 5, "Rare", 5, 3, 4)
    enemies = [EliteCard("Enemy1", 5, "Rare", 5, 3, 4),
               EliteCard("Enemy2", 5, "Rare", 5, 3, 4)]
    print(f"\nPlaying {arcane_warrior.name} (Elite Card):")
    print("\nCombat phase:")
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defense result: {arcane_warrior.defend(2)}")
    print("\nMagic phase:")
    print(f"Spell cast: {arcane_warrior.cast_spell('Fireball', enemies)}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
