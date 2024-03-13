# Execução

Basta executar o arquivo main.py no diretório do projeto

```
python main.py
```

Com o arquivo 'exemplo.txt' fornecido, a saída será:

```
Picos verdadeiros: (Segundo, Valor)
(11, 70)
(29, 65)
(44, 78)
(59, 67)

Tempo médio entre os picos
TMEP = 00:16
```

## Testes de Execução

Foi testado com mais alguns arquivos, há mais 2 disponibilizados juntos neste repositório.

Os arquivos foram gerados com IA para tentar simular cenários com mais ou menos picos verdadeiros

Para testar com outros dados, basta alterar na linha 25 de `main.py`, o nome do arquivo .txt, contido na variável `arquivo`:
```
arquivo = 'exemplo.txt'
```

# Observações

O desafio foi encontrar os picos verdadeiros, estabelecendo uma `distancia` padrão para considerar os valores próximos como picos e montar a lógica ao redor disto.

Definir uma distância mínima entre os picos ajuda a dicernir entre um pico verdadeiro e um falso, implementar essa lógica foi um desafio.


# Implementação

O código lê os valores de um arquivo, encontra os picos verdadeiros nesses valores, calcula o tempo médio entre os picos e imprime os resultados.


### 1. Função encontrar_picos_verdadeiros:

- Esta função recebe uma lista de valores e uma distância como entrada.
- Percorre os valores da lista, ignorando o primeiro e o último elemento (pois não podem ser picos verdadeiros).
- Verifica se o valor atual é maior ou igual a 50 e se é maior do que os valores adjacentes (anterior e posterior).
- Se todas as condições forem atendidas, considera o valor como um pico verdadeiro e verifica se ele é maior do que os valores dentro da distância especificada.
- Se o pico for válido, adiciona-o à lista de picos verdadeiros.
- Retorna a lista de picos verdadeiros.


### 2. Leitura dos valores do arquivo exemplo.txt:

- Abre o arquivo ".txt", especificado na variável `arquivo`, em modo de leitura.
- Lê cada linha do arquivo, converte os valores para inteiros e os armazena em uma lista chamada valores.


### 3. Definição da distância para validar os picos:

- Define a distância como 5. Isso significa que o algoritmo considerará os valores dentro de uma distância de 5 segundos em relação ao pico atual ao verificar se o pico é verdadeiro ou falso.


### 4 Encontrar os picos verdadeiros:

- Chama a função `encontrar_picos_verdadeiros` passando a lista de valores e a distância como argumentos.
- Armazena os picos verdadeiros retornados pela função na lista `picos_verdadeiros`.


### 5. Imprimir os picos verdadeiros:

- Imprime os picos verdadeiros encontrados na lista `picos_verdadeiros`. Em forma de tupla (Segundo, Valor)


### 6. Função calcular_tempo_medio_entre_picos:

- Recebe a lista de picos verdadeiros como entrada.
- Itera sobre a lista de picos, calculando as diferenças entre os índices dos picos consecutivos.
- Soma todas as diferenças.
- Calcula o tempo médio entre os picos em segundos.
- Converte o tempo médio para minutos e segundos.
- Retorna o tempo médio formatado como "mm:ss".


### 7. Cálculo e impressão do tempo médio entre os picos:

- Chama a função `calcular_tempo_medio_entre_picos` passando a lista de picos verdadeiros como argumento.
- Armazena o tempo médio retornado pela função na variável `tempo_medio_entre_picos`.
- Imprime o tempo médio entre os picos.
