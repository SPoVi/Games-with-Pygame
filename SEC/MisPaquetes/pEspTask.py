class EspTask:
    def __init__(self, id, prio, SepMin, D):
        self.id = id
        self.separacionMin= SepMin
        self.prio = prio
        self.deadline = D
        self.tipo = "Esporadica"

    def print_param(self):
        print(self.tipo)
        print("Id: " + str(self.id) + " Per: " + str(self.separacionMin)+ " Prio: " +str(self.prio)+ " Deadline: " + str(self.deadline))
