class Proceso:
    def __init__(self):
        self.nombre = ""
        self.llegada = 0
        self.cpu = 0
        self.instante = 0
        self.t_fin = 0
        self.t_e = 0
        self.t_r = 0
        self.penalizacion = 0.0

# Función de comparación para usar con sorted
def comparar_procesos(proceso):
    return proceso.nombre

print("+------------------------------------------------------+")
print("|            El proceso mas corto                     |")
print("+------------------------------------------------------+")

num_procesos = int(input("Ingrese el numero de procesos: "))

procesos = [Proceso() for _ in range(num_procesos)]
 
for i in range(num_procesos):
    print(f"Ingrese la hora de llegada del proceso {i + 1}: ", end="")
    procesos[i].llegada = int(input())
    print(f"Ingrese la duracion del proceso {i + 1}: ", end="")
    procesos[i].cpu = int(input())
    procesos[i].nombre = chr(ord('A') + i)

tiempo_actual = 0
penalizacion_total = 0.0

print("+---------+---------+-----+----------+-------+------+-----------------------+")
print("| proceso | llegada | cpu | instante | t.fin | t.e  | t.r | penalizacion       |")
print("+---------+---------+-----+----------+-------+------+-----------------------+")

while True:
    proceso_ejecutar = -1
    menor_tiempo_cpu = -1

    for i in range(num_procesos):
        if procesos[i].llegada <= tiempo_actual and procesos[i].cpu > 0:
            if proceso_ejecutar == -1 or procesos[i].cpu < menor_tiempo_cpu:
                proceso_ejecutar = i
                menor_tiempo_cpu = procesos[i].cpu

    if proceso_ejecutar == -1:
        break

    p = procesos[proceso_ejecutar]
    p.instante = tiempo_actual
    p.t_fin = p.instante + p.cpu
    p.t_e = p.instante - p.llegada
    p.t_r = p.t_e + p.cpu

    if p.t_e == 0:
        p.penalizacion = 0
    else:
        p.penalizacion = p.t_r / p.t_e

    penalizacion_total += p.penalizacion
    tiempo_actual = p.t_fin

    print(f"|    {p.nombre}    |    {p.llegada:2d}   |  {p.cpu:2d} |    {p.instante:2d}    |  {p.t_fin:3d}  |  {p.t_e:2d}  |  {p.t_r:2d}  |    {p.penalizacion:.8f}   |")

    p.cpu = 0


promedio_penalizacion = penalizacion_total / num_procesos
print(f"Promedio de penalizacion: {promedio_penalizacion:.8f}")
