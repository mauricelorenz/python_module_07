from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = sorted(hand, key=lambda card: card.cost)[:2]
        mana_used = sum(card.cost for card in cards_played)
        targets_attacked = self.prioritize_targets(battlefield)
        damage_dealt = sum(card.attack for card in cards_played
                           if hasattr(card, "attack"))
        return {'cards_played': [card.name for card in cards_played],
                'mana_used': mana_used,
                'targets_attacked': targets_attacked,
                'damage_dealt': damage_dealt}

    def get_strategy_name(self) -> str:
        return type(self).__name__

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            return available_targets
        player_target = [target for target in available_targets
                         if "player" in target.lower()]
        if not player_target:
            return [available_targets[0]]
        return [player_target[0]]
