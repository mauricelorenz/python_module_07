from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "wizard":
            return CreatureCard(**{"name": "Ice Wizard",
                                   "cost": 4,
                                   "rarity": "Rare",
                                   "attack": 3,
                                   "health": 4})
        return CreatureCard(**{"name": "Fire Dragon",
                               "cost": 5,
                               "rarity":
                               "Legendary",
                               "attack": 7,
                               "health": 5})

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return SpellCard(**{"name": "Meteor",
                            "cost": 8,
                            "rarity":
                            "Legendary",
                            "effect_type":
                            "damage"})

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArtifactCard(**{"name": "Mana Crystal",
                               "cost": 2,
                               "rarity": "Common",
                               "durability": 5,
                               "effect": "Permanent: +1 mana per turn"})

    def create_themed_deck(self, size: int) -> dict:
        spells = []
        curr_size = 3
        while curr_size < size:
            spells.append(self.create_spell())
            curr_size += 1
        return {"creatures": [self.create_creature(),
                              self.create_creature("wizard")],
                "spells": spells,
                "artifacts": [self.create_artifact()]}

    def get_supported_types(self) -> dict:
        return {"creatures": ["dragon", "wizard"],
                "spells": ["meteor"], "artifacts": ["mana_crystal"]}
