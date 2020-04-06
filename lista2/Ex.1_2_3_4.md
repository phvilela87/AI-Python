# Lista de exercícios #2

## Regressão Linear

1- Qual técnica de regressão linear você usaria se tivesse um conjunto de treinamento com milhares de features? Explique por quais razões você utilizaria esta técnica.

Para um conjunto de treinamento com milhares de features, a técnica mais apropriada seria a técnica de regressão linear com gradiente descendente estocático.   
Esta é uma das abordagens iterativas que permite obtermos uma convergência mais rápida, pois ao contrário do algoritmo em batelada, este modelo utiliza apenas uma parte do conjunto de treinamento de forma aleatória.

---

2- Suponha que as features (i.e., atributos) do seu conjunto de treinamento tenham escalas muito diferentes. Qual técnica de regressão linear pode sofrer com isso e como? O que pode ser feito para mitigar este problema? 

Esse problema ocorre com todo algoritmo que se baseia no cálculo da distância durante a fase de treinamento. Em certas situações, alguns atributos acabam sendo dominantes sobre os demais no sentido de que exercem grande influência sobre o erro cometido pelo modelo. Para evitar esse problema, a variação de todos os atributos deve ser escalonada para que cada atributo contribua com a mesma importância/peso para o cálculo da distância, ou seja, do erro quadrático médio.

---

3- Suponha que você use o gradiente descendente em batelada e plote o erro de cada época. Se você perceber que o erro aumenta constantemente, o que provavelmente está acontecendo? Como você pode consertar isso?

Quando o erro aumenta constantemente, isso pode ser um indicativo de que o passo de aprendizagem utilizado esteja demasiadamente grande, fazendo o aloritmo divergir. Para o que problema seja solucionado é necessário ajustar o passo de aprendizagem adequadamente através de uma análise do gráfico da função de custo em função do número de iterações.

---

4- Entre os algoritmos baseados no gradiente descendente (GD) que discutimos (batch, estocástico e mini-batch), qual deles chega mais rapidamente à vizinhança da solução ótima? Qual deles realmente converge? O que você pode fazer para que os outros também convirjam?

O algoritmo que chega mais rápido é o gradiente descendente estocástico.   
O gradiente descendente em batelada (batch) caminha diretamente para o mínimo. Portanto, ele é o que realmente converge.   
Para que os outros algoritmos também convirjam é necessário modificar o passo de aprendizagem.