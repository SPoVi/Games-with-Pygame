class PerTask:
    def __init__(self, id, prio, per, D):
        self.id = id
        self.periodo = per
        self.prio = prio
        self.deadline = D
        self.tipo = "Periodica"

    def print_param(self):
        print(self.tipo)
        print("Id: " + str(self.id) + " Per: " + str(self.periodo)+ " Prio: " +str(self.prio)+ " Deadline: " + str(self.deadline))
