# Lista de exercícios #3

## Regressão Polinomial

1- Suponha que você esteja usando regressão polinomial. Você plota as **curvas de aprendizado** e percebe que há uma grande diferença entre o erro de treinamento e o erro de validação. O que está acontecendo? Quais são as três maneiras de resolver isso?
**OBS.: Curvas de aprendizado**: são gráficos mostrando o desempenho do modelo no conjunto de treinamento e no conjunto de validação em função do tamanho do conjunto de treinamento (ou da iteração do treinamento). 

Isso acontece devido a maldição da complexidade.
Subajuste ou bias: erros de treinamento e validação tendem a serem elevados.
Sobre ajustes ou variância: erro de trenamento é baixo mas erro de validação é alto.
Sobreajuste - situação em que o modelo se ajusta tão bem aos exemplos do conjunto de treinamento que ele aprende até o ruído presente nos mesmos, ou seja, o modelo apresenta baixo erro de treinamento. Porém, o modelo produz erros significativos quando apresentados a dados inéditos (alto erro de erro de generalização).

Existem diversas formas de validação cruzada,, sendo as mais utilizadas:  

* Holdout
* k-fold
* Leave-p-out

Existem outras formas, mas todas outras podem ser vistas como variações de uma dessas três.

---