from argparse import ArgumentParser
from typing import Tuple, List


def get_mission_info(file_path: str) -> Tuple[Tuple[int, int], List[dict]]:
    """Extrai informações do arquivo de entrada a respeito do planalto e da sonda

    Args:
        file_path (str): Caminho do arquivo contendo as informações do
            planalto e das sondas enviadas

    Returns:
        Tuple[Tuple[int, int], List[dict]]: Uma tupla em que o primeiro
            elemento contém um par de inteiros correspondendo à coordenada do
            canto superior direito do planalto; o segundo elemento corresponde
            a uma lista de dicionários em que cada um contém as chaves
            'ini_pos' e 'seq_mov', respectivamente a posição inicial e
            sequência de movimentações de uma sonda
    """
    pass


def find_final_coordinate(explorer: dict) -> str:
    """Encontra a orientação e coordenada final de uma sonda

    Args:
        explorer (dict): Dicionário contendo as chaves 'ini_pos' e 'seq_mov',
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
        'caminho', type=str,
        help='caminho do arquivo de texto contendo as informações '
             'do planalto e das sondas enviadas')
    main(parser.parse_args())
