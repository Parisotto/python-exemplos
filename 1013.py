dados = input().split(" ")

maior = (int(dados[0]) + int(dados[1]) + abs(int(dados[0]) - int(dados[1]))) / 2
maior = (maior + int(dados[2]) + abs(maior - int(dados[2]))) / 2
print(f"{maior:.0f} eh o maior")
