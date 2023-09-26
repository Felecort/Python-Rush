
class FlyingBird:
    def __init__(self, speed):
        self.fl_speed = speed

    def fly(self):
        print(f"I'm flying at speed {self.fl_speed}")


class RunningBird:
    def __init__ (self, speed):
        self.rn_speed = speed
    
    def run(self):
        print(f"I'm running at speed {self.rn_speed}")


class Duck(FlyingBird, RunningBird):
    # If no __init__, super(FlyingBird).__init__(speed) - will cal
    def __init__(self, speed):
        super(FlyingBird, self).__init__(speed)
        super(RunningBird, self).__init__(speed)

        pass


d = Duck(10)
d.fly()
d.run()
