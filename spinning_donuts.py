import os
import math
import time
import shutil

def spinning_donut():
    A = 0
    B = 0

    while True:
        # Obter o tamanho do terminal
        cols, rows = shutil.get_terminal_size()
        width = cols - 1  # Largura do terminal
        height = rows - 1  # Altura do terminal

        # Ajustar proporção para formato dos caracteres
        aspect_ratio = 2  # Compensação para caracteres achatados
        scaled_width = width // aspect_ratio

        # Inicializar a tela e o z-buffer
        output = [" "] * (width * height)
        zbuffer = [0] * (width * height)

        # Renderizar o donut
        for theta in range(0, 628, 7):  # Ângulo do círculo (0 a 2π, passos de 0.07 rad)
            for phi in range(0, 628, 2):  # Ângulo de rotação do torus
                sinA = math.sin(A)
                cosA = math.cos(A)
                sinB = math.sin(B)
                cosB = math.cos(B)

                sinTheta = math.sin(theta / 100)
                cosTheta = math.cos(theta / 100)
                sinPhi = math.sin(phi / 100)
                cosPhi = math.cos(phi / 100)

                # Coordenadas do torus
                circleX = cosTheta + 2  # Raio maior do torus
                circleY = sinTheta

                x = circleX * (cosB * cosPhi + sinA * sinB * sinPhi) - circleY * cosA * sinB
                y = circleX * (sinB * cosPhi - sinA * cosB * sinPhi) + circleY * cosA * cosB
                z = 1 / (circleX * sinA * sinPhi + circleY * sinA * cosB + cosA * cosPhi + 5)
                screenX = int(scaled_width / 2 + scaled_width * z * x)
                screenY = int(height / 2 + height * z * y / 2)  # Proporção vertical corrigida

                brightness = int(8 * (cosTheta * cosPhi * sinB - cosA * cosTheta * sinPhi + sinTheta * cosB))
                brightness = max(0, min(7, brightness))  # Garante que fique entre 0 e 7

                if 0 <= screenX < width and 0 <= screenY < height and z > zbuffer[screenY * width + screenX]:
                    zbuffer[screenY * width + screenX] = z
                    output[screenY * width + screenX] = " .:-=+*#@"[brightness]

        # Exibir o donut na tela
        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join("".join(output[i:i + width]) for i in range(0, len(output), width)))

        # Atualizar os ângulos para girar o donut
        A += 0.04
        B += 0.08
        time.sleep(0.03)

# Executar o código
spinning_donut()
