from models.calculate import Calculate

def main() -> None:
    points: int = 0
    play(points)

def play(points: int) -> None:
    difficulty: int = int(input('Informe o nível de dificuldade desejado[1, 2, 3, 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('Informe o resultado para a seguinte operção: ')
    calc.show_operation()

    result: int = int(input())

    if calc.result_check(result):
        points += 1
        print(f'Você tem {points} ponto(s).')

    continues: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - nao] '))

    if continues:
        play(points)
    else:
        print(f'Vcoê finalizou com {points} ponto(s).')
        print('Até a próxima!')




if __name__ == '__main__':
    main()

