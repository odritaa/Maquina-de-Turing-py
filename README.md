# Maquina-de-Turing-py

Trabajo Práctico "Figuritas"

El trabajo práctico consta de interpretar los comandos para dibujar figuras geométricas en el plano. Las siguientes funciones dibujan un gráfico:

  •circle r:dibuja un círculo de radio r con centro en las coordenadas (0,0) retornando un círculo.
  •box ancho alto:dibuja un rectángulo con una esquina en (0,0) y la opuesta en (ancho,alto), retornando un rectángulo.

Las siguientes funciones reciben un objeto gráfico como parámetro. Su resultado es el gráfico modificado según se indica:

  •move dx dy g : Desplaza el gráfico g una distancia dx sobre el eje x y dy sobre el eje y.
  •scale fx fy g : Cambia la escala del gráfico g, multiplicando la unidad por un factor fx en el eje x y por un factor fy en el eje y
  •rotate a g : Rota el gráfico g un ángulo de a grados en sentido antihorario con respecto a las coordenadas (0,0)

Se pide realizar los autómatas para reconocer cada uno de los comandos y realizar el gráfico correspondiente.
