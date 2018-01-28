# coding=utf-8

#5.  Faça um programa para resolver o seguinte problema: 
#São dadas as coordenadas reais x e y de um ponto, um número natural n, 
# e as coordenadas reais de n pontos (1 < n < 100). 
# Deseja-se calcular e imprimir sem repetição os raios das circunferências centradas
#  no ponto (x,y) que passam por pelo menos um dos n pontos dados.
import math

points = [(-1.0, 1.2), (1.5, 2.0), (0.0, -2.0), (0.0, 0.5), (4.0, 2.0)]
(x, y) = (1.0, 1.0)


def dist_betwen_points(point1, point2):
    a, b = point1
    c, d = point2
    distance = math.sqrt(math.pow((a-c), 2) + math.pow((b-d), 2))
    return distance

# Calcular a distância de cada ponto
# Eliminar as distâncias repetidas
# Imprimir as distâncias restantes

radius_list = []
for point in points:
    t, r = point
    radius = dist_betwen_points((x, y), (t, r))
    if radius not in radius_list:
        radius_list.append(radius)

answear = "Há {0} circunferências com raios: {1:.2f}, {2:.2f} e {3:.2f}".format(
    len(radius_list), radius_list[0], radius_list[1], radius_list[2]
    ) 
print(answear)
    