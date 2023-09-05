dados = input().split(" ")

print(f"TRIANGULO: {(float(dados[0]) * float(dados[2]) / 2):.3f}")
print(f"CIRCULO: {3.14159 * pow(float(dados[2]), 2):.3f}")
print(f"TRAPEZIO: {((float(dados[0]) + float(dados[1])) * float(dados[2])) / 2:.3f}")
print(f"QUADRADO: {pow(float(dados[1]), 2):.3f}")
print(f"RETANGULO: {(float(dados[0]) * float(dados[1])):.3f}")
