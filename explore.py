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
            a uma lista de dicionários, cada um representando uma sonda
    """
    with open(file_path) as file_:
        file_data = file_.read().splitlines()
    rect_x, rect_y = file_data[0].split()
    coordinate = (int(rect_x), int(rect_y))
    explorers = make_explorers(file_data[1:])
    return coordinate, explorers


def make_explorers(explorers_data: List[str]) -> List[dict]:
    """Transforma os dados das sondas em informações

    Args:
        explorers_data (List[str]): Dados referentes às sondas extraídos
            do arquivo inicial

    Returns:
        List[dict]: Lista de dicionários contendo as chaves 'ini_pos', 'att'
            e 'seq_mov', representando a posição inicial, a orientação inicial
            e a sequência de movimentos, respectivamente
    """
    explorers = []
    for index in range(0, len(explorers_data), 2):
        explorer_init = explorers_data[index].split()
        explorer_info = {
            'ini_pos': (int(explorer_init[0]), int(explorer_init[1])),
            'att': explorer_init[2],
            'seq_mov': explorers_data[index+1]
        }
        explorers.append(explorer_info)
    return explorers


def main(args):
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'caminho', type=str,
        help='caminho do arquivo de texto contendo as informações '
             'do planalto e das sondas enviadas')
    main(parser.parse_args())
