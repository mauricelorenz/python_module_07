from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("attack must be positive")
        if health <= 0:
            raise ValueError("health must be positive")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def attack_target(self, target: "CreatureCard") -> dict:
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": self.attack, "combat_resolved": True}
