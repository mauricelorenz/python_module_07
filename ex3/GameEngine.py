from ex0.Card import Card
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand: list[Card] | None = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.hand = [self.factory.create_creature(),
                     self.factory.create_creature("wizard"),
                     self.factory.create_artifact()]
        turn_result = self.strategy.execute_turn(self.hand, ["Target Player"])
        self.turns_simulated += 1
        self.total_damage += turn_result["damage_dealt"]
        self.cards_created += len(self.hand)
        return turn_result

    def get_engine_status(self) -> dict:
        return {"turns_simulated": self.turns_simulated,
                "strategy_used": self.strategy.get_strategy_name(),
                "total_damage": self.total_damage,
                "cards_created": self.cards_created}
