<p align="center">
  <img src="https://avatars.githubusercontent.com/u/8749848?s=280&v=4" />
</p>

<h1 align ="center">Using_PCQA_Python</h1>

<p align="center">applicating pcqa in coding with python</p>

<h2 align ="left">O que foi feito?</h2>

Primeiramente foi acessado o site do Dataquest.io em busca do Projeto Guiado: " Guided Project: Predicting Car Prices ", onde foi realizado o download do projeto. em seguida validei os arquivos criando um novo notebook na plataforma do Google Colaboratory onde realizei varios testes sobre os dados disponibilizado no projeto, com o código rodando gerei um arquivo .py, com o script.py em mãos fui até o software Jupyter e comecei analisar o código gerado, a partir do pylint foi mostrado varios problemas de qualidade, então para começar a tratar esse problemas primeiro utilizei a ferramente pep8 para fazer breves mudanças de tabulação, posicionamento e etc, o comando autopep8 --in-place --aggressive --aggressive script.py realizou tais mudanças, e a partir delas comecei a trabalhar mudanças no código, foram feitas mudanças nos nomes de parametros, funções repetidas, deletados alguns comentarios desnecessarios e criação de algumas documentações do Docstrings entre outras mudanças realizadas até alcançar nota 10.0/10.0 pela ferramenta do pylint.

![Alt Text](https://github.com/Julio-CSilva/Using_PCQA_Python/blob/main/refactoring/Screenshot_1.png)

<h2 align ="left">O que precisa instalar para executar?</h2>

A unica ferramente que foi necessarias baixar foi Anaconda, na qual já conta com as ferramentas Pylint e Pep8 instaladas.

- [ANACONDA](https://www.anaconda.com)

<h2 align ="left">Como executar?</h2>

1. Baixe a pasta refactoring do repositorio.
2. Depois de instalado o ANACONDA, basta iniciar o ANACONDA.NAVIGATOR e depois clickar em "Launch" do JupyterLab.
3. Abra um Terminal.
4. Vá até o diretorio onde se encontra a pasta baixada.
5. e execute o comando: pylint script.py
