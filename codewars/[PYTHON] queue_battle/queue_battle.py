from collections import deque
from typing import Optional, Tuple


# HAS a list of Armies
class Battle:
    def __init__(self, distance: int, *armies: Tuple[int, ...]):
        self._distance = distance
        self.armies = [Army(id, army, distance) for id, army in enumerate(armies)]

    @property
    def distance(self) -> int:
        return self._distance

    def round(self) -> None:
        for army in self.armies:
            army.update_bullets()
        for army in self.armies:
            bullet = army.fire()
            if bullet is not None:
                self.target_army(army).add_bullet(bullet)
            army.rotate()

    def check_winner(self) -> Optional[Tuple[int, Tuple[int, ...]]]:
        if not self.is_over():
            return None
        if len(self.armies) == 0:
            return (-1, ())
        winner = self.armies[0]
        return (winner.id, tuple(soldier.id for soldier in winner.soldiers))

    def is_over(self) -> bool:
        for id, army in reversed(list(enumerate(self.armies))):
            if not army.alive():
                self.armies.pop(id)
                self.reposition()
        return False if len(self.armies) > 1 else True

    def reposition(self) -> None:
        for army in self.armies:
            army.clear_bullets()

    def target_army(self, army: "Army") -> "Army":
        return self.armies[(self.armies.index(army) + 1) % len(self.armies)]


# HAS a deque of Soldiers
# HAS a list of Bullets incoming
class Army(Battle):
    def __init__(self, id: int, army: Tuple[int, ...], distance: int):
        super().__init__(distance)
        self._id = id
        self.soldiers = deque(
            Soldier(id, rifle_speed) for id, rifle_speed in enumerate(army)
        )
        self.bullets_incoming: list[Bullet] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def head(self) -> "Soldier":
        return self.soldiers[0]

    def alive(self) -> bool:
        return len(self.soldiers) > 0

    def clear_bullets(self) -> None:
        self.bullets_incoming.clear()

    def fire(self) -> Optional["Bullet"]:
        return self.head.fire()

    def rotate(self) -> None:
        if self.head.is_alive:
            self.soldiers.rotate(-1)
        else:
            self.soldiers.popleft()

    def add_bullet(self, bullet: "Bullet") -> None:
        self.bullets_incoming.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets_incoming:
            bullet.update()
        self.bullets_incoming.sort(key=lambda bullet: bullet.distance_travelled)
        if len(self._bullets_hit()) > 0:
            self.head.is_alive = False

    def _bullets_hit(self) -> list["Bullet"]:
        bullets_hit: list[Bullet] = []
        while (
            self.bullets_incoming
            and self.bullets_incoming[-1].distance_travelled >= self.distance
        ):
            bullets_hit.append(self.bullets_incoming.pop())
        return bullets_hit


class Soldier:
    def __init__(self, id: int, rifle_speed: int):
        self._id = id
        self._rifle_speed = rifle_speed
        self.is_alive = True

    @property
    def id(self) -> int:
        return self._id

    @property
    def rifle_speed(self) -> int:
        return self._rifle_speed

    def fire(self) -> Optional["Bullet"]:
        return Bullet(self.rifle_speed) if self.is_alive else None


class Bullet:
    def __init__(self, speed: int):
        self._speed = speed
        self._distance_travelled = 0

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def distance_travelled(self) -> int:
        return self._distance_travelled

    def update(self) -> None:
        self._distance_travelled += self._speed


def queue_battle(dist, *armies):
    battle = Battle(dist, *armies)
    winner = None
    while winner is None:
        battle.round()
        winner = battle.check_winner()
    return winner


example_tests = (
	(100,(25,38,55,46,82),(64,90,37,25,58)),
	(200,(61,83,37,55,92,35,68,72),(90,81,36,114,67,25,31,84)),
	(300,(98,112,121,95,63),(120,94,90,88,30),(116,144,45,200,32)),
	(400,(186,78,56,67,78,127,78,192),(78,67,208,45,134,212,82,99),(327,160,49,246,109,98,44,57)),
	(500,(345,168,122,269,151),(56,189,404,129,101),(364,129,209,163,379),(520,224,154,74,420)),
)
example_sols = (
	(1,(3,2)),
	(0,(6,7)),
	(0,(2,)),
	(2,(0,2,5)),
	(-1,()),
)

for i, v in enumerate(example_tests):
    winner = queue_battle(*v)
    print(winner)
