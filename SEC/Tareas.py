from MisPaquetes.pPerTask import PerTask
from MisPaquetes.pEspTask import EspTask

T1 = PerTask(1,10,60,1)
T2 = EspTask(2,20,30,2)

T1.print_param()

print("Periodo: "+str(T1.periodo)+ " s")

T2.print_param()