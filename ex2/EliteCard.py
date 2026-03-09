from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 offense: int, defense: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.offense = offense
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite effect"}

    def attack(self, target: Card) -> dict:
        return {"attacker": self.name, "target": target.name,
                "damage": self.offense, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> dict:
        return {"defender": self.name, "damage_taken": incoming_damage,
                "damage_blocked": self.defense,
                "still_alive": incoming_damage < self.defense}

    def get_combat_stats(self) -> dict:
        return {"name": self.name, "offense": self.offense,
                "defense": self.defense}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {"caster": self.name, "spell": spell_name,
                "targets": [target.name for target in targets],
                "mana_used": self.mana}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"name": self.name, "mana": self.mana}
