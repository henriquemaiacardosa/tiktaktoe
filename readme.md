# Jogo da Velha com Quadrado Mágico de Lo Shu

## Descrição

Este projeto implementa o tradicional **Jogo da Velha (Tic-Tac-Toe)** em Python, utilizando o **Quadrado Mágico de Lo Shu** para verificar as condições de vitória.

O jogo é disputado entre um jogador humano (`X`) e o computador (`O`) em um tabuleiro 3x3.

---

## Abordagem Utilizada

A solução utiliza o **Quadrado Mágico de Lo Shu**, representado pela matriz:

| 4 | 9 | 2 |
| - | - | - |
| 3 | 5 | 7 |
| 8 | 1 | 6 |

Uma propriedade desse quadrado é que qualquer linha, coluna ou diagonal soma **15**.

Assim, em vez de verificar diretamente as combinações do tabuleiro, cada posição ocupada pelo jogador é convertida para o número correspondente do quadrado mágico. O jogador vence quando existe alguma combinação de três números cuja soma seja igual a 15.

### Estratégia do Computador

A inteligência do computador segue a seguinte ordem de prioridade:

1. Fazer uma jogada vencedora, se disponível;
2. Bloquear uma vitória iminente do jogador humano;
3. Ocupar o centro do tabuleiro;
4. Escolher um canto livre aleatoriamente;
5. Escolher uma borda livre aleatoriamente;
6. Escolher qualquer posição livre restante.

Essa estratégia torna o jogo mais competitivo sem utilizar algoritmos complexos como Minimax.

---

## Funcionalidades

* Jogo Humano vs Computador;
* Validação de entradas do usuário;
* Verificação de vitória usando o Quadrado Mágico de Lo Shu;
* Detecção de empate;
* Escolha automática de jogadas pelo computador.

---

## Como Executar

### Requisitos

* Python 3.x

### Execução

No terminal:

```bash
python jogo_velha.py
```

---

## Exemplo de Execução

```text
=== JOGO DA VELHA - Quadrado Magico de Lo Shu ===
Voce e 'X', o computador e 'O'. Posicoes numeradas de 1 a 9.

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Sua jogada (1-9): 5

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computador jogou na posicao 1.

 O | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9
```

---

## Estrutura do Código

### Principais Funções

* `tabuleiro_novo()`: cria um tabuleiro vazio.
* `imprimir_tabuleiro()`: exibe o tabuleiro.
* `posicoes_livres()`: retorna as posições disponíveis.
* `numeros_do_jogador()`: converte posições em números do Lo Shu.
* `venceu()`: verifica se existe uma combinação cuja soma seja 15.
* `jogada_que_vence()`: identifica jogadas vencedoras.
* `escolher_jogada_computador()`: define a jogada da IA.
* `ler_jogada_humano()`: valida a entrada do usuário.
* `main()`: controla o fluxo principal do jogo.

---

## Conclusão

O projeto demonstra uma forma alternativa e elegante de implementar a lógica de vitória do Jogo da Velha utilizando propriedades matemáticas do Quadrado Mágico de Lo Shu. A estratégia do computador permite partidas equilibradas e atende aos requisitos de um jogo funcional entre humano e máquina.
