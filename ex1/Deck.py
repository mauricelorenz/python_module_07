from random import shuffle
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        cards_count = len(self.cards)
        creatures_count = sum(1 for card in self.cards
                              if isinstance(card, CreatureCard))
        spells_count = sum(1 for card in self.cards
                           if isinstance(card, SpellCard))
        artifacts_count = sum(1 for card in self.cards
                              if isinstance(card, ArtifactCard))
        total_cost = sum(card.cost for card in self.cards)
        avg_cost = total_cost / cards_count if cards_count else 0.0
        return {"total_cards": cards_count,
                "creatures": creatures_count,
                "spells": spells_count,
                "artifacts": artifacts_count,
                "avg_cost": avg_cost}
