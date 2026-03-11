#!/usr/bin/env python3

from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 7, "Legendary", 1200, 0, 0)
    wizard = TournamentCard("Ice Wizard", 5, "Rare", 1150, 0, 0)
    tournament_platform = TournamentPlatform()
    dragon_card = tournament_platform.register_card(dragon)
    print(f"\nFire Dragon (ID: {dragon_card}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    wizard_card = tournament_platform.register_card(wizard)
    print(f"\nIce Wizard (ID: {wizard_card}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")
    print("\nCreating tournament match...")
    print("Match result: "
          f"{tournament_platform.create_match(dragon_card, wizard_card)}")
    print("\nTournament Leaderboard:")
    leaderboard = tournament_platform.get_leaderboard()
    for item in leaderboard:
        print(item)
    print("\nPlatform Report:")
    print(f"{tournament_platform.generate_tournament_report()}")
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
