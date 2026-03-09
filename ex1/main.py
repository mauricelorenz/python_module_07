#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    cards = [CreatureCard(**{"name": "Fire Dragon", "cost": 5,
                             "rarity": "Legendary", "attack": 7, "health": 5}),
             ArtifactCard(**{"name": "Mana Crystal", "cost": 2,
                             "rarity": "Common", "durability": 5,
                             "effect": "Permanent: +1 mana per turn"}),
             SpellCard(**{"name": "Lightning Bolt", "cost": 3,
                          "rarity": "Common", "effect_type": "damage"})]
    deck = Deck()
    for card in cards:
        deck.add_card(card)
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")
    try:
        while deck.get_deck_stats()["total_cards"] > 0:
            first_card = deck.draw_card()
            print(f"\nDrew: {first_card.name} "
                  f"({type(first_card).__name__.replace("Card", "")})")
            print(f"Play result: {first_card.play({})}")

    except IndexError as e:
        print(f"Error: {e}")

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
