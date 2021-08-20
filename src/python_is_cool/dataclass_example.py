from dataclasses import dataclass


@dataclass
class Test:
    """ Nothing... """
    engine: float
    wheel: str
    color: str


t = Test(1.5, 'medium', 'black')
print(t.engine)
print(t.wheel)
print(t.color)
