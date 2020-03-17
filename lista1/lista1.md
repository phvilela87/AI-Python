# TP555 – AI/ML

 ## Lista de Exercícios #1

1.  Defina com suas próprias palavras:
    
    a. Inteligência  
    É a faculdade de conhecer, compreender e aprender.
    
    b. Inteligência artificial  
    Inteligência Artificial é um ramo da ciência da computação que se propõe a elaborar dispositivos que simulem a capacidade humana de raciocinar, perceber, tomar decisões e resolver problemas.
    
    c. Aprendizado de máquina  
    É a habilidade de um sistema computacional de aprender sem a necessidade de ter sido previamente programado.
    
2.  Diz-se que um programa de computador aprende com a experiência  **E**  com relação a alguma tarefa  **T**  e alguma medida de desempenho  **D**, se seu desempenho em  **T**, medido por  **D**, melhorar com a experiência  **E**. Suponha que um algoritmo de aprendizado seja alimentado com muitos dados climáticos históricos, e aprenda a prever o tempo. Qual seria uma escolha razoável para  **D**?
    
    a. A probabilidade de prever corretamente o tempo de uma data futura;  
    b. A tarefa de previsão do tempo;  
    c. O processo do algoritmo que examina uma grande quantidade de dados climáticos históricos;  
    d. Nenhuma das alternativas anteriores.  
    
Letra C. Uma das maneiras de avaliar seu desempenho seria através de sua capacidade de análise de dados históricos.

3.  Diz-se que um programa de computador aprende com a experiência  **E**  com relação a alguma tarefa  **T**  e alguma medida de desempenho  **D**, se seu desempenho em  **T**, medido por  **D**, melhorar com a experiência  **E**. Suponha que você esteja trabalhando numa agência meteorológica e deseje treinar um algoritmo de aprendizado com dados climáticos históricos para que este preveja o tempo. Neste caso, o que seriam  **T**  e  **E**?

T (tarefa) – previsão climática baseada em dados históricos
E  (experiência) – resultante do que foi previsto e do que realmente aconteceu

4.  Suponha que você esteja trabalhando em uma agência meteorológica com previsão do tempo, e que a agência faça uma das três previsões para o clima de cada dia:  **ensolarado**,  **nublado**  ou  **chuvoso**. Você deseja usar um algoritmo de aprendizado para prever o tempo de amanhã. Você trataria essa tarefa como uma tarefa de  **classificação**  ou de  **regressão**? Justifique sua escolha.

Classificação. A previsão do tempo por si só, poderia ser classificada como regressão por levar em conta inúmeros parâmetros. Porém, como as previsões possuem valores finitos (ensolarado, nublado ou chuvoso), a melhor opção é classificação. Deste modo, o algoritmo encontrará os limiares de decisão que irão classificar cada nova informação de entrada.

5.  Suponha que você esteja trabalhando em uma empresa de investimentos na previsão do mercado de ações e gostaria de prever o preço de uma determinada ação amanhã (medido em reais). Você deseja usar um algoritmo de aprendizado para isso. Você trataria essa tarefa como uma tarefa de  **classificação**  ou de  **regressão**? Justifique sua escolha.

Regressão. A regressão é muito utilizada com informações contínuas, onde todos os dados conhecidos devem ser utilizados para alcançar a melhor projeção do valor da ação desejada.

6.  Que tipo de algoritmo de aprendizado de máquina você usaria para permitir que um robô andasse em vários terrenos desconhecidos?  **Dica:**  o robô precisa, através de sensores, entender o estado do terreno (buracos, paredes, subidas íngremes, etc.) e baseado neste estado executar ações (se mover para frente/trás, esquerda/direita) e dependendo do resultado dessas ações decidir quais são as ações corretas para que ele ande sem problemas pelo terreno.

Aprendizado por reforço. Assim, o robô observa o estado do ambiente em que está inserido executando ações de “melhor estratégia” e realimentando seu bando de dados com os resultados obtidos.

7.  Que tipo de algoritmo de aprendizado de máquina você usaria para segmentar clientes de uma grande empresa de e-commerce em vários grupos?  **Dica:**  você pode ter os grupos já definidos e treinar um modelo para alocar novos clientes a esses grupos ou querer descobrir diferentes tipos de grupos de clientes.

Aprendizado não-supervisionado. Um exemplo seria o uso do Algoritmo de detecção de anomalias, que deve verificar se uma nova observação pertence aos grupos já conhecidos de clientes ou pode ser descrito como algo novo. Essa nova entrada, pode ser associada a um algoritmo regra de associação, capaz de formar novos grupos ou padrões.

8.  Pesquise a literatura sobre IA/ML e descubra se as seguintes tarefas podem ser solucionadas por computadores. Se as tarefas puderem ser solucionadas, descreva  **sucintamente**  o algoritmo/método de IA/ML utilizado e como o problema é solucionado. <br/>
Utilize o link abaixo como ponto de partida para sua pesquisa: <br/>[https://mlc.committees.comsoc.org/research-library/](https://mlc.committees.comsoc.org/research-library/) <br/>
    
    a. Alocação de recursos em redes móveis (e.g., LTE, 5G-NR, etc.) <br/>
    
    Título: [Energy Efficiency in Reinforcement Learning for Wireless Sensor Networks](https://arxiv.org/pdf/1812.02538.pdf) <br/>
    Descrição:  Cruzamento de dados aleatórios da potência do sinal recebido (RSSI) com informações provenientes de diversos sensores, construídos no elemento. Tais sensores desempenham o papel de acão-reusltado-recompensa, além de contribuir na construção de um dataset a ser utilizado <br/>
    Aprendizado: Reforço <br/>
    Algoritmo: Markov Decision Processes (MDP) <br/>   
    
    b. Mitigação de colisões em redes sem-fio e móveis <br/>
    
    Título: [Deep Learning-Based Spectrum Prediction Collision Avoidance for Hybrid Wireless Environments](https://ieeexplore.ieee.org/document/8684944) <br/>
    Descrição: Predição de uso do espectro das redes vizinhas <br/>
    Aprendizado: Deep Learning  Supervisionado <br/>
    Algoritmo: Convolutional Neural Network (CNN) <br/>
    
    c. Projeto e otimização de esquemas de modulação e codificação <br/>
    
    Título: [A Deep Learning Wireless Transceiver with Fully Learned Modulation and Synchronization](https://arxiv.org/pdf/1905.10468.pdf) <br/>
    Descrição: <br/>
    Aprendizado: Deep Neural Network (DNN) <br/>
    Algoritmo: Autoencoders <br/>
    
    d. Sensoriamento espectral <br/>
    
    Título: [Deep Learning for Spectrum Sensing](https://arxiv.org/pdf/1909.02730.pdf) <br/>  
    Descrição: Treinamento com base em um dataset com variadas modulações digitais e variação de SNR. A rede cria um conhecimento inerente sobre sistemas modulados, o que aumenta drasticamente o desempenho quando detectando energia <br/>
    Aprendizado: Reforço <br/>
    Algoritmo: Deep Learning - Convolutional Long short-term Deep Neural Network (CLDNN) <br/>  
    
    e. Posicionamento e localização em ambientes indoor Roteamento de redes <br/>
    
    Título: [Analysis and Visualization of Deep Neural Networks in Device-Free Wi-Fi Indoor Localization](https://arxiv.org/pdf/1904.10154.pdf) <br/> 
    Descrição: A rede neural aprende automaticamente os recursos que discriminam as medições ruidosas de sinal sem fio, utilizando a informação do estado do canal (CSI) <br/>
    Aprendizado: Deep Neural Network (DNN) <br/>
    Algoritmo: Naive Bayes classifier <br/>
    
    f. Detecção e estimação de canal em sistemas de transmissão ópticos <br/>
    
    Título: [Learning-based network path planning for traffic engineering](https://www.sciencedirect.com/science/article/pii/S0167739X18313244) <br/>
    Descrição: Inspirado pela análise de sentenças do NLP, é criado um modelo sequence-to-sequence (S2S) para capturar as características intrínsecas da rede, melhorando o encaminhamento de pacotes <br/>
    Aprendizado: Deep Learning <br/>
    Algoritmo: Natural Language Processing (NPL) <br/>
    
    g. Pré-distorção digital de não-linearidades de front-ends de RF <br/>
    
    Título: [An Overview on Application of Machine Learning Techniques in Optical Networks](https://www.researchgate.net/publication/328821936_An_Overview_on_Application_of_Machine_Learning_Techniques_in_Optical_Networks) <br/>  
    Descrição: Overview de uma aplicação utilizando machine learning para comunicações óticas <br/>
    Aprendizado: Supervisionado <br/>
    Algoritmo: Traffic flow classification and Path computatio <br/>  
    
    h. Segurança e robustez em redes de comunicação <br/>
    
    Título: <br/>  
    Descrição: <br/>
    Aprendizado: <br/> 
    Algoritmo: <br/> 
    
    i. Segurança e robustez em redes de comunicação <br/>
    
    Título: [Performance of Statistical and Machine Learning Techniques for Physical Layer Authentication](https://arxiv.org/pdf/2001.06238.pdf) <br/>
    Descrição: Avaliação de desempenho de técnicas de autenticação na camada física considerando métodos de algoritmos de critério estatístico e machine learning <br/>
    Aprendizado: Supervisionado <br/>
    Algoritmo: k-nearest neighbors (k-NN) e SVM <br/>
