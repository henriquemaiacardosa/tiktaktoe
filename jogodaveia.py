import random
from itertools import combinations

JOGADOR_HUMANO = 'X'
JOGADOR_COMPUTADOR = 'O'
VAZIO = ' '
QUADRADO_LO_SHU = [4, 9, 2,
                   3, 5, 7,
                   8, 1, 6]

CENTRO = 4          
CANTOS = [0, 2, 6, 8]
BORDAS = [1, 3, 5, 7]


def tabuleiro_novo():
    return [VAZIO] * 9


def imprimir_tabuleiro(tab):
    def celula(i):
        return tab[i] if tab[i] != VAZIO else str(i + 1)
    linhas_str = []
    for l in range(3):
        i = l * 3
        linhas_str.append(f" {celula(i)} | {celula(i+1)} | {celula(i+2)} ")
    print("\n" + "\n---+---+---\n".join(linhas_str) + "\n")


def posicoes_livres(tab):
    return [i for i, v in enumerate(tab) if v == VAZIO]


def numeros_do_jogador(tab, jogador):
    """Converte as casas marcadas pelo jogador nos numeros de Lo Shu
    correspondentes a essas casas."""
    return [QUADRADO_LO_SHU[i] for i, v in enumerate(tab) if v == jogador]


def venceu(tab, jogador):
    """Vitoria = existe algum trio dos numeros do jogador cuja soma e 15."""
    numeros = numeros_do_jogador(tab, jogador)
    if len(numeros) < 3:
        return False
    return any(sum(trio) == 15 for trio in combinations(numeros, 3))


def empate(tab):
    return VAZIO not in tab


def jogada_que_vence(tab, jogador):
    for pos in posicoes_livres(tab):
        copia = tab[:]
        copia[pos] = jogador
        if venceu(copia, jogador):
            return pos
    return None


def escolher_jogada_computador(tab):
    
    pos = jogada_que_vence(tab, JOGADOR_COMPUTADOR)
    if pos is not None:
        return pos
    pos = jogada_que_vence(tab, JOGADOR_HUMANO)
    if pos is not None:
        return pos
    if tab[CENTRO] == VAZIO:
        return CENTRO
    cantos_livres = [c for c in CANTOS if tab[c] == VAZIO]
    if cantos_livres:
        return random.choice(cantos_livres)
    bordas_livres = [b for b in BORDAS if tab[b] == VAZIO]
    if bordas_livres:
        return random.choice(bordas_livres)
    return random.choice(posicoes_livres(tab))


def ler_jogada_humano(tab):
    while True:
        entrada = input("Sua jogada (1-9): ").strip()
        if not entrada.isdigit():
            print("Digite um numero de 1 a 9.")
            continue
        pos = int(entrada) - 1
        if pos < 0 or pos > 8:
            print("Posicao fora do tabuleiro.")
            continue
        if tab[pos] != VAZIO:
            print("Posicao ja ocupada, escolha outra.")
            continue
        return pos


def main():
    tab = tabuleiro_novo()
    print("=== JOGO DA VELHA - Quadrado Magico de Lo Shu ===")
    print("Voce e 'X', o computador e 'O'. Posicoes numeradas de 1 a 9.")
    imprimir_tabuleiro(tab)

    while True:
        pos = ler_jogada_humano(tab)
        tab[pos] = JOGADOR_HUMANO
        imprimir_tabuleiro(tab)
        if venceu(tab, JOGADOR_HUMANO):
            print("Voce venceu!")
            break
        if empate(tab):
            print("Empate!")
            break

        pos = escolher_jogada_computador(tab)
        tab[pos] = JOGADOR_COMPUTADOR
        print(f"Computador jogou na posicao {pos + 1}.")
        imprimir_tabuleiro(tab)
        if venceu(tab, JOGADOR_COMPUTADOR):
            print("Computador venceu!")
            break
        if empate(tab):
            print("Empate!")
            break


if __name__ == "__main__":
    main()