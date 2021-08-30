#!/usr/bin/env python3.9
from argparse import ArgumentParser
from typing import List
from explorer import Explorer


def get_mission_info(file_path: str) -> List[Explorer]:
    """
    Define os limites do planalto e extrai informações referentes às sondas do
    arquivo de entrada

    Args:
        file_path (str): Caminho do arquivo contendo as informações do
            planalto e das sondas enviadas

    Returns:
        List[Explorer]: Lista de objetos do tipo Explorer (sondas)
    """
    with open(file_path) as file_:
        file_data = file_.read().splitlines()
    Explorer.set_limits(file_data[0].split())
    return make_explorers(file_data[1:])


def make_explorers(explorers_data: List[str]) -> List[Explorer]:
    """
    Transforma os dados das sondas em objetos sonda (Explorer)

    Args:
        explorers_data (List[str]): Lista com os dados de sondas extraídos do
            arquivo de entrada

    Returns:
        List[Explorer]: Lista de objetos do tipo Explorer (sondas)
    """
    explorers = []
    for index in range(0, len(explorers_data), 2):
        explorer_init = explorers_data[index].split()
        explorer = Explorer(
            int(explorer_init[0]), int(explorer_init[1]),
            explorer_init[2],
            explorers_data[index+1])
        if explorer is not None:
            explorers.append(explorer)
        else:
            print(f'Sonda #{index//2+1} ignorada. Parâmetros inválidos.')
    return explorers


def main(args):
    try:
        explorers = get_mission_info(args.caminho)
    except ValueError as e:
        print(e)
    else:
        for explorer in explorers:
            print(explorer.find_final_state())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        'caminho', type=str,
        help='caminho do arquivo de texto contendo as informações '
             'do planalto e das sondas enviadas')
    main(parser.parse_args())
