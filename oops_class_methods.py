class Inhibitor:
    intensity=0 #class object variable
    def __init__(self, element, reason):
        self.element = element
        self.reason = reason
    def indisp(self):
        print("Inhibitor gives a stopper to growth")


inhibitor_1 = Inhibitor("Auxin", "inhibits growth")
print(inhibitor_1.element)
print(inhibitor_1.indisp())
inhibitor_2 = Inhibitor("Abscisic Acid", "hinders development in plants")
print(inhibitor_2.intensity)