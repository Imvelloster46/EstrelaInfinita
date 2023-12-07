from turtle import *  # Importa todas as funções da biblioteca turtle
import colorsys  # Importa a biblioteca colorsys

title("Estrela Infinita by- idCodex7")
bgcolor("black")
speed(20)

def desenha_estrela(radius, speed_factor):  # Define uma função com dois parâmetros
    iteration = 0  # Inicializa a variável de iteração
    while True:
        hue = (360 * iteration) / 10  # Ajusta a velocidade das cores
        saturation = 1.0
        value = 1.0
        color_rgb = colorsys.hsv_to_rgb(hue / 360, saturation, value)  # Converte a cor de HSV para RGB
        color(color_rgb)  # Define a cor da tartaruga (cursor)

        forward(radius)  # Move a tartaruga para frente pelo raio especificado
        right(300)
        left(250)
        backward(radius)
        right(360 * speed_factor)  # Gira a tartaruga para a direita pelo fator de velocidade multiplicado por 30

        iteration += 1  # Incrementa a variável de iteração
        if iteration >= 100:  # Se a iteração for maior ou igual a 100
            iteration = 1  # Reinicia a variável de iteração
            clear()  # Limpa a tela para evitar desordem

desenha_estrela(150, 1.5)  # Chama a função com um raio de 100 e um fator de velocidade de 1.5
done()  # Finaliza o desenho