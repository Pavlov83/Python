class Hero:

    def __init__(self, health, mana):
        self._health = health
        self._mana = _mana

    def attack(self) -> int:
        '''Returns the attack damage of the
        Hero'''

        return 1

    def take_damage(self, damage: int):
        self._health -= take_damage

    def is_alive(self):

        return self._health > 0
