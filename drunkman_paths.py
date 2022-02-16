import random

def camino_borracho(pasos):
    origen=(0,0)
    coordenada_actual=origen
    
    for _ in range(pasos):
        delta_x, delta_y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        coordenada_nueva_x=coordenada_actual[0]+delta_x
        coordenada_nueva_y=coordenada_actual[1]+delta_y
        coordenada_actual = (coordenada_nueva_x,coordenada_nueva_y)

    distancia_final_x=coordenada_actual[0]
    distancia_final_y=coordenada_actual[1]
    distancia_final=((distancia_final_x)**2+(distancia_final_y)**2)**0.5

    return distancia_final

d=camino_borracho(5)
print(d)
