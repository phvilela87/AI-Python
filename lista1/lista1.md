# TP555 – AI/ML

## Lista de Exercícios #1

1. Defina com suas próprias palavras:

	a. Inteligência <br/>
	É a faculdade de conhecer, compreender e aprender.
	
	b. Inteligência artificial <br/>
	Inteligência Artificial é um ramo da ciência da computação que se propõe a 		elaborar dispositivos que simulem a capacidade humana de raciocinar, perceber, tomar decisões e resolver problemas.

	c. Aprendizado de máquina <br/>
	É a habilidade de um sistema computacional de aprender sem a necessidade de ter sido previamente programado.

3. Diz-se que um programa de computador aprende com a experiência **E** com relação a alguma tarefa **T** e alguma medida de desempenho **D**, se seu desempenho em **T**, medido por **D**, melhorar com a experiência **E**. Suponha que um algoritmo de aprendizado seja alimentado com muitos dados climáticos históricos, e aprenda a prever o tempo. Qual seria uma escolha razoável para **D**?

	a. A probabilidade de prever corretamente o tempo de uma data futura;
	b. A tarefa de previsão do tempo;
	c. O processo do algoritmo que examina uma grande quantidade de dados climáticos históricos;
	d. Nenhuma das alternativas anteriores.  

Letra C. Uma das maneiras de avaliar seu desempenho seria através de sua capacidade de análise de dados históricos.  

3. Diz-se que um programa de computador aprende com a experiência **E** com relação a alguma tarefa **T** e alguma medida de desempenho **D**, se seu desempenho em **T**, medido por **D**, melhorar com a experiência **E**. Suponha que você esteja trabalhando numa agência meteorológica e deseje treinar um algoritmo de aprendizado com dados climáticos históricos para que este preveja o tempo. Neste caso, o que seriam **T** e **E**?  

**T** (tarefa) – previsão climática dentro de um período de tempo
**E** (experiência) – resultante do que foi previsto e do que realmente aconteceu

4. Suponha que você esteja trabalhando em uma agência meteorológica com previsão do tempo, e que a agência faça uma das três previsões para o clima de cada dia: **ensolarado**, **nublado** ou **chuvoso**. Você deseja usar um algoritmo de aprendizado para prever o tempo de amanhã. Você trataria essa tarefa como uma tarefa de **classificação** ou de **regressão**? Justifique sua escolha.  

Classificação. A previsão do tempo por si só, poderia ser classificada como regressão. Porém, como as previsões são valores finitos, conhecidos, a melhor opção é classificação. 

5. Suponha que você esteja trabalhando em uma empresa de investimentos na previsão do mercado de ações e gostaria de prever o preço de uma determinada ação amanhã (medido em reais). Você deseja usar um algoritmo de aprendizado para isso. Você trataria essa tarefa como uma tarefa de **classificação** ou de **regressão**? Justifique sua escolha.

Regressão.

7. Que tipo de algoritmo de aprendizado de máquina você usaria para permitir que um robô andasse em vários terrenos desconhecidos? **Dica:** o robô precisa, através de sensores, entender o estado do terreno (buracos, paredes, subidas íngremes, etc.) e baseado neste estado executar ações (se mover para frente/trás, esquerda/direita) e dependendo do resultado dessas ações decidir quais são as ações corretas para que ele ande sem problemas pelo terreno.

Aprendizado por reforço.

7. Que tipo de algoritmo de aprendizado de máquina você usaria para segmentar clientes de uma grande empresa de e-commerce em vários grupos? **Dica:** você pode ter os grupos já definidos e treinar um modelo para alocar novos clientes a esses grupos ou querer descobrir diferentes tipos de grupos de clientes.

Aprendizado não-supervisionado.  

8. Pesquise a literatura sobre IA/ML e descubra se as seguintes tarefas podem ser
solucionadas por computadores. Se as tarefas puderem ser solucionadas, descreva
**sucintamente** o algoritmo/método de IA/ML utilizado e como o problema é solucionado.
Utilize o link abaixo como ponto de partida para sua pesquisa:
https://mlc.committees.comsoc.org/research-library/

	a. Alocação de recursos em redes móveis (e.g., LTE, 5G-NR, etc.)
	
	Título: Energy Efficiency in Reinforcement Learning for Wireless Sensor Networks
	Descrição:
	Aprendizado: Reforço
	Algoritmo: Markov Decision Processes (MDP)

	b. Mitigação de colisões em redes sem-fio e móveis

	Título: Deep Learning-Based Spectrum Prediction Collision Avoidance for Hybrid Wireless Environments
	Aprendizado: Deep Learning
	Algoritmo: Convolutional Neural Network (CNN)

	c. Projeto e otimização de esquemas de modulação e codificação 

	Título: A Deep Learning Wireless Transceiver with Fully Learned Modulation and 				Synchronization
	Aprendizado: Deep Neural Network (DNN)
	Algoritmo: Autoencoders

	d. Sensoriamento espectral

	Título: Deep Learning for Spectrum Sensing
	Aprendizado: Reforço
	Algoritmo: Deep Learning - Convolutional Long short-term Deep Neural
	Network (CLDNN)

	e. Posicionamento e localização em ambientes indoor Roteamento de redes

	Título: Analysis and Visualization of Deep Neural Networks in Device-Free
Wi-Fi Indoor Localization
	Aprendizado: Deep Neural Network (DNN)
	Algoritmo: Naive Bayes classifier

	f. Detecção e estimação de canal em sistemas de transmissão ópticos

	Título: Learning-based network path planning for traffic engineering
	Aprendizado: Deep Learning
	Algoritmo: Natural Language Processing (NPL)

	g. Pré-distorção digital de não-linearidades de front-ends de RF

	Título: An Overview on Application of Machine Learning Techniques in Optical Networks
	Aprendizado: Supervisionado
	Algoritmo: Traffic flow classification and Path computation

	h. Segurança e robustez em redes de comunicação 
	
	Título:
	Aprendizado:
	Algoritmo: 

	i. Segurança e robustez em redes de comunicação

	Título: Performance of Statistical and Machine Learning Techniques for Physical Layer Authentication
	Aprendizado: Supervisionado
	Algoritmo: k-nearest neighbors (k-NN) e SVM
