# Acessibilidade_Parte_2_Segmenta-o_de_textos

O código principal em Python se encontra na pasta "/scr", e os métodos extras se encontram no caderno Jupyter.

Esse repositório contém implementação python e formulação matemática das combinações completas ordenadas de palavras em uma frase. Sua implementação está ligada a combinação de palavras utilizadas que podem ser utilizadas na linguagem Libras.

Obter todas as combinações de quebra que a frase pode apresentar, por examplo:

**Entrada**: `eu gosto de café`

**Saída**: 

```python
[
['eu gosto de café'],
['eu', 'gosto de café'],
['eu gosto', 'de café'],
['eu gosto de', 'café'],
['eu', 'gosto', 'de café'],
['eu', 'gosto de', 'café'],
['eu gosto', 'de', 'café'],
['eu', 'gosto', 'de', 'café']
]
```
Pode ser feita de diversas maneiras. A mais comum, imediata, e presente no código python na pasta /scr, é através de funções recursivas. A primeira palavra se combina ou se serata do resto da frase, e o mesmo tratamento é feito recursivamente para o resto da frase até que sobrem apenas a ultima palavra. Alcançando a ultima palavra a regressão retorna, palavra a palavra, criando sequências através de separação ou combinação com a palavra anterior. Essa implementação é simples e elegante graças a recursão.

Uma segunda implementação nada elegante, mas mais interessante é fantendo uso de combinações completas, através da transformação do problema em pauzinhos e bolinhas e realizando uma combinação simples. Imagine que cada palavra é uma bolinha e os separadores são pauzinhos que separam as bolinhas. Temos (n-1) pauzinhos (um a menos que o numero de bolinhas), totalizando 2n-1 elementos. O desafio se resume agora a escolher as n-1 posições dos pauzinhos dentre as 2n-1 disponíveis (combinação simples 2n-1, n-1 a n-1). Com os indices das posições dos pauzinhos podemos saber facilmente as posições e combinações das palavras (bolinhas). Essa é uma bordagem não ortodoxa, que apresenta por vezes elementos repetidos ignorados. Apresenta-se no caderno Jupyter e no link do Google colab https://colab.research.google.com/drive/1Hf01Xpjirfmj_gBQ5igq8yRJwPd3kW8X?usp=sharing uma versão implementada dessa estratégia paralelizada através do pacote parsl.

Por fim uma análise mais detalhada de combinações completas e seu uso, juntamente com detalhes da solução recursiva, está presente no artigo do Medium.
