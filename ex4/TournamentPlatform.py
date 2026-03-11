from random import random
from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches = 0
        self.is_active = True

    def register_card(self, card: TournamentCard) -> str:
        name = card.name.split()[-1].lower()
        n = 1
        while f"{name}_{n:03d}" in self.cards:
            n += 1
        new_card = f"{name}_{n:03d}"
        self.cards[new_card] = card
        return new_card

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        total_rating = self.cards[card1_id].rating
        + self.cards[card2_id].rating
        if random() < self.cards[card1_id].rating / total_rating:
            winner, loser = card1_id, card2_id
        else:
            winner, loser = card2_id, card1_id
        self.cards[winner].rating += 16
        self.cards[winner].wins += 1
        self.cards[loser].rating -= 16
        self.cards[loser].losses += 1
        self.matches += 1
        return {"winner": winner,
                "loser": loser,
                "winner_rating": self.cards[winner].rating,
                "loser_rating": self.cards[loser].rating}

    def get_leaderboard(self) -> list:
        cards_list = [self.cards[card] for card in self.cards]
        cards_list_sorted = sorted(cards_list,
                                   key=lambda leaderboard: leaderboard.rating,
                                   reverse=True)
        leaderboard = []
        for n, card in enumerate(cards_list_sorted, 1):
            leaderboard.append(f"{n}. {card.name} - Rating: {card.rating} "
                               f"({card.wins}-{card.losses})")
        return leaderboard

    def generate_tournament_report(self) -> dict:
        cards_list = [self.cards[card] for card in self.cards]
        avg_rating = int(sum(card.rating for card in cards_list)
                         / len(cards_list))
        return {"total_cards": len(cards_list),
                "matches_played": self.matches,
                "avg_rating": avg_rating,
                "platform_status": "active" if self.is_active else "inactive"}
