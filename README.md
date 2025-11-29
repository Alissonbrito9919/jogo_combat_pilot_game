# ✈️ Combat Pilot Game

Um jogo de tiro 2D (Space Shooter) desenvolvido em **Python** utilizando o framework **Pygame Zero**.

O projeto foi criado para demonstrar conceitos fundamentais de desenvolvimento de jogos e Programação Orientada a Objetos (POO).

## 🎮 Funcionalidades

* **Menu Interativo:** Sistema de estados (Menu/Jogo) com botões clicáveis e controle de áudio (Mute/Unmute).
* **Fundo Infinito (Parallax):** Lógica matemática para criar a ilusão de um cenário contínuo.
* **Animação de Sprites:** O jogador e os inimigos possuem animações de quadros (frames) para movimento e ação.
* **Múltiplos Inimigos:** Gerenciamento de inimigos através de Listas e laços de repetição.
* **Sistema de Colisão:** Detecção precisa de colisão entre Míssil/Inimigo e Jogador/Inimigo.
* **Áudio:** Trilha sonora em loop e efeitos sonoros de disparo e explosão.

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.12+
* **Biblioteca:** Pygame Zero (`pgzero`)
* **Conceitos de POO:** Herança (Classes `Player`, `Enemy`, `Missile` herdando de `Actor`), Encapsulamento e Instanciação.
* **Lógica de Jogo:** Game Loop, Máquina de Estados, Aritmética Modular (para animação e background).

## 🚀 Como rodar o projeto

### Pré-requisitos
Você precisa ter o [Python](https://www.python.org/) instalado em sua máquina.

### Instalação
1. Clone este repositório:
     git clone [https://github.com/SEU-USUARIO/combat-pilot-game.git](https://github.com/SEU-USUARIO/combat-pilot-game.git)
2-Entre na pasta do projeto:
     cd combat-pilot-game
3-Instale a dependência necessária:
     pip install pgzero
4-Para iniciar o jogo, execute o comando no terminal:
     pgzrun main.py

🕹️ Controles

Tecla / Ação,Função
Setas (↑ / ↓),Movimentar o Avião
Espaço,Atirar Míssil
Mouse (Clique),Interagir com o Menu
     
