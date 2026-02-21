from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from enum import Enum
from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass
