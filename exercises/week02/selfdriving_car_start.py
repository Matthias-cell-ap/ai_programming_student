"""
Oefening 1: Self-Driving Car (Model-based Reflex Agent)
========================================================
Implementeer een agent die zijn voorligger volgt.
"""


class LidarSensorInput:
    def __init__(self, distance=0.0):
        self.DistanceTo = distance


class Brake:
    def __str__(self):
        return "BRAKE"


class Nothing:
    def __str__(self):
        return "NOTHING"


class SelfDrivingCar:
    def __init__(self):
        # TODO: interne state — welke variabele heb je nodig?
        self.DistanceTo = None
        self.PrevDistance = None

    def process(self, sensor_input):
        # TODO: bereken relatieve snelheid en tijd tot botsing; 
        #       rem als tijd < 5 seconden
        self.DistanceTo = sensor_input.DistanceTo
        if self.PrevDistance == None:
            self.PrevDistance = self.DistanceTo

        speed = self.PrevDistance - self.DistanceTo
        self.PrevDistance = self.DistanceTo

        action = Nothing()
        if speed > 0 and self.DistanceTo / speed < 5:
            action = Brake()
        
        return action


if __name__ == "__main__":
    sensor = LidarSensorInput(10)
    agent = SelfDrivingCar()

    for afstand in [10, 15, 13, 10, 8, 6, 4, 3]:
        sensor.DistanceTo = afstand
        action = agent.process(sensor)
        print(f"Afstand: {afstand}m -> {action}")