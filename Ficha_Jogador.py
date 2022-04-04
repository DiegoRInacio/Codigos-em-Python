def ficha(nome='', gol=''):
    if nome == '':
        nome = 'DESCONHECIDO'
    if not gol.isdigit():
        gol = 0
    print(f'O jogador {nome} fez {gol} gols no campeonato')


nome = input('Nome do Jogador: ').strip().title()
gol = input('Nº de gols: ').strip()
ficha(nome, gol)