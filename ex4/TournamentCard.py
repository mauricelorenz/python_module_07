from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 rating: int, wins: int, losses: int):
        super().__init__(name, cost, rarity)
        self.rating = rating
        self.wins = wins
        self.losses = losses

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def attack(self, target: Card) -> dict:
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": self.cost, "combat_resolved": True}

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> dict:
        return {"name": self.name, "rating": self.rating,
                "wins": self.wins, "losses": self.losses}

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"name": self.name, "rating": self.rating,
                "wins": self.wins, "losses": self.losses}

    def defend(self, incoming_damage: int) -> dict:
        return {"defender": self.name, "damage_taken": incoming_damage,
                "damage_blocked": incoming_damage,
                "still_alive": True}

    def get_combat_stats(self) -> dict:
        return {"name": self.name, "rating": self.rating,
                "wins": self.wins, "losses": self.losses}
