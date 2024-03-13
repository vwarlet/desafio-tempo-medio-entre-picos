# Função para encontrar picos verdadeiros
def encontrar_picos_verdadeiros(valores, distancia):
    picos_verdadeiros = []
    for i in range(1, len(valores) - 1):
        # Considerar apenas valores entre 0 e 100
        if valores[i] < 0 or valores[i] > 100:
            pass
        if valores[i] >= 50 and valores[i] > valores[i - 1] and valores[i] > valores[i + 1]:
            pico_verdadeiro = True
            # Verifica se o pico é válido comparando com os vizinhos dentro da distância especificada
            for j in range(1, distancia + 1):
                if i - j >= 0:
                    if valores[i] <= valores[i - j]:
                        pico_verdadeiro = False
                        break
                if i + j < len(valores):
                    if valores[i] <= valores[i + j]:
                        pico_verdadeiro = False
                        break
            if pico_verdadeiro:
                picos_verdadeiros.append((i, valores[i]))
    return picos_verdadeiros

# Lê os valores do arquivo .txt
arquivo = 'exemplo.txt'
with open(arquivo, 'r') as arquivo:
    valores = [int(linha.strip()) for linha in arquivo.readlines()]

# Define a distância para validar os picos
distancia = 5

# Encontra os picos verdadeiros
picos_verdadeiros = encontrar_picos_verdadeiros(valores, distancia)

# Imprime os picos verdadeiros
print("Picos verdadeiros: (Segundo, Valor)")
for pico in picos_verdadeiros:
    print(pico)

def calcular_tempo_medio_entre_picos(picos):
    diferenca_total = 0
    # Itera sobre os picos, começando do segundo
    for i in range(1, len(picos)):
        # Calcula a diferença entre os índices de pares de picos consecutivos
        diferenca = picos[i][0] - picos[i-1][0]
        diferenca_total += diferenca
    # Calcula o tempo médio entre os picos em segundos
    tempo_medio = diferenca_total / (len(picos) - 1)
    # Converte o tempo médio para minutos e segundos
    minutos = int(tempo_medio // 60)
    segundos = int(tempo_medio % 60)
    # Formata o resultado como "mm:ss"
    resultado_formatado = f"{minutos:02}:{segundos:02}"
    return resultado_formatado

# Calcula o tempo médio entre os picos
tempo_medio_entre_picos = calcular_tempo_medio_entre_picos(picos_verdadeiros)

# Imprime o tempo médio entre os picos
print("\nTempo médio entre os picos \nTMEP =", tempo_medio_entre_picos)
