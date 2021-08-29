from argparse import ArgumentParser


def read_file(file_path: str) -> list[dict]:
    """Lê informações do arquivo de entrada e retorna uma lista de dicionários

    Args:
        file_path (str): Caminho do arquivo contendo as informações do
            planalto e das sondas enviadas

    Returns:
        list[dict]: Uma lista contendo dicionários onde cada dicionário contém
            as chaves 'ini_pos' e 'seq_mov', respectivamente a posição inicial
            e sequência de movimentações de uma sonda
    """
    pass


def find_final_coordinate(sonda: dict) -> str:
    """Encontra a orientação e coordenada final de uma sonda

    Args:
        sonda (dict): Dicionário contendo as chaves 'ini_pos' e 'seq_mov',
            representando a posição inicial e sequência de movimentações,
            respectivamente

    Returns:
        str: Uma string no formato '{int} {int} {char}' indicando a coordenada
            e orientação finais da sonda
    """
    pass


def main(args):
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'caminho',
        help='caminho do arquivo de texto contendo as informações '
             'do planalto e das sondas enviadas')
    main(parser.parse_args())
