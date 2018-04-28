#Control objects asre responsible for coordination of other object
class Fight:
    class FightOver(Exception):
        def __init__(self,winner, *args, **kwargs):
            self.winner = winner
            super(*args, **kwargs)

    def __init__(self, hero_a:Hero,hero_b: Hero):
        self._hero_a = hero_a
        self.hero_b = hero_b
        self.fight_ongoing = True
        self.winner = None

    def fight(self):
        while self.fight_ongoing:
            self._run_round()
        print(f'The fight has ended!Winner is #{self.winner}')

    def _run_round(self):
        try:
            self._run_attack(self._hero_a, self._hero_b)
            self._run_attack(self._hero_b, self._hero_a)
        except self.FighOver as e:
            self._finish_round(e.winner)

    def _run_attack(self, attacker: Hero, victim: Hero):
        damage = attacker.attack()
        victim.take_damage(damage)
        if not victim.is_alive():
            raise self.FightOver(winner=attacker)

    def _finish_round(self, winner: Hero):
        self.winner = winner
        self.fight_ongoing = False                                    
