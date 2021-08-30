# Explorando Marte
Implementação em Python3 do controle das sondas de exploração da NASA em Marte. Como proposto no desafio técnico da Xerpay.

## Definição do Escopo
Um conjunto de sondas foi enviado pela NASA à Marte e irá pousar num planalto que será explorado.
A posição e direção de uma sonda são representadas por uma combinação de coordenadas x-y e uma letra representando a direção cardinal para qual a sonda aponta, seguindo a rosa dos ventos em inglês.

O planalto é retangular e dividido numa malha para simplificar a navegação. Sendo (0, 0) as coordenadas do canto inferior esquerdo.
As letras "L", "R" e "M" são enviadas para controlar as sondas:
- L: Vira 90° para a esquerda;
- R: Vira 90° para a direita;
- M: Move para a frente um ponto da malha.

O código processa uma série dessas instruções, tratando sempre uma sonda por vez.

### Entrada
A entrada esperada é o caminho para um arquivo de texto com informações são separadas por linhas.
A primeira linha deve conter as coordenadas do canto superior direito do planalto separadas por um espaço. No caso de serem fornecidos mais de dois valores, os excedentes são silenciosamente ignorados.
As demais linhas são informações das sondas. Cada sonda utiliza duas linhas, a primeira se refere ao estado inicial da sonda e a segunda à sequência de instruções que devem ser seguidas. Um exemplo de entrada é mostrado a seguir:

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

Observação: Existe um caso omisso referente a booleanos informados como coordenadas. Os valores `False` e `True` são interpretados como inteiros 0 e 1, respectivamente.
### Saída
A saída do programa também é dividida por linhas, cada uma informa o estado final de uma sonda. O exemplo de saída para a entrada acima seria:
```
1 3 N
5 1 E
```
Em casos adversos outras saídas são apresentadas: 
- Quando uma sonda ultrapassa os limites do planalto, sua saída apresenta o seguinte prefixo: `ERRO! Última coordenada registrada:`;
- Quando os parâmetros de entrada são inválidos, a sonda é ignorada e sua saída, omitida. Antes das outras saídas, contudo, a seguinte informação é impressa: `Sonda #n ignorada. Parâmetros inválidos.` onde `n` é o número da sonda em ordem de pouso.
## Execução
Para execução em ambiente Linux é necessário que o arquivo `main.py` seja executável e que o Python3.9 esteja instalado, e seu uso é como:
```bash
./main.py "./sondas.txt"
```

## Testes
Foram implementados testes unitários para as funções `find_final_state()` e `set_limits()`. O seguinte comando deve ser utilizado para executá-los:
```bash
python3.9 -m unittest tests.TestMovingExplorer
```
