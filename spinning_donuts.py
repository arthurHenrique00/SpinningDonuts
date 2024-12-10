import os
import math
import time
import shutil

def spinning_donut():
    A, B = 0, 0

    while True:
        cols, rows = shutil.get_terminal_size()
        width, height = cols - 1, rows - 1

        aspect_ratio = 2
        scaled_width = width // aspect_ratio

        output = [' '] * (width * height)
        zbuffer = [0] * (width * height)

        for theta in range(0, 628, 7):
            for phi in range(0, 628, 2):
                sinA, cosA = math.sin(A), math.cos(A)
                sinB, cosB = math.sin(B), math.cos(B)
                sinTheta, cosTheta = math.sin(theta / 100), math.cos(theta / 100)
                sinPhi, cosPhi = math.sin(phi / 100), math.cos(phi / 100)


                circleX = cosTheta + 2
                circleY = sinTheta

                x = circleX * (cosB * cosPhi + sinA * sinB * sinPhi) - circleY * cosA * sinB
                y = circleX * (sinB * cosPhi - sinA * cosB * sinPhi) + circleY * cosA * cosB
                z = 1 / (circleX * sinA * sinPhi + circleY * sinA * cosB + cosA * cosPhi + 5)

                screenX = int(scaled_width / 2 + scaled_width * z * x)
                screenY = int(height / 2 + height * z * y / 2)

                brightness = int(8 * (cosTheta * cosPhi * sinB - cosA * cosTheta * sinPhi + sinTheta * cosB))
                brightness = max(0, min(7, brightness))

                if 0 <= screenX < width and 0 <= screenY < height and z > zbuffer[screenY * width + screenX]:
                    zbuffer[screenY * width + screenX] = z
                    output[screenY * width + screenX] = " .:-=+*#@"[brightness]

        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join("".join(output[i:i + width]) for i in range(0, len(output), width)))

        A += 0.04
        B += 0.08
        time.sleep(0.03)

spinning_donut()

