
class Explorer:
    limit_x = None
    limit_y = None
    directions = ['N', 'E', 'S', 'W']

    def __init__(
            self, init_x: int, init_y: int, init_att: str, instructions: str):
        self.pos_x = init_x
        self.pos_y = init_y
        self.attitude = init_att
        self.instructions = instructions

    @classmethod
    def create_explorer(
            cls, init_x: int, init_y: int, init_att: str, instructions: str):
        """
        Valida os parâmetros de entrada e cria uma nova sonda

        Args:
            init_x (int): Posição inicial da sonda em X
            init_y (int): Posição inicial da sonda em Y
            init_att (str): Orientação inicial da sonda
            instructions (str): Lista de instruções para movimentação da sonda

        Returns:
            Explorer: Retorna uma nova sonda quando os parâmetros são válidos,
                em outro caso, retorna None
        """
        if (not isinstance(init_x, int) or not isinstance(init_y, int)
                or init_x > Explorer.limit_x or init_x < 0
                or init_y > Explorer.limit_y or init_y < 0
                or init_att not in Explorer.directions
                or not all(inst in ['R', 'L', 'M'] for inst in instructions)):
            return None
        return Explorer(init_x, init_y, init_att, instructions)

    def move(self):
        """
        Movimenta a sonda na direção atual

        Raises:
            ValueError: Quando a movimentação resulta em uma coordenada
                inválida
        """
        if self.attitude == 'N':
            self.pos_y += 1
        elif self.attitude == 'S':
            self.pos_y -= 1
        elif self.attitude == 'E':
            self.pos_x += 1
        else:
            self.pos_x -= 1
        if (self.pos_x > Explorer.limit_x or self.pos_y > Explorer.limit_y
                or self.limit_x < 0 or self.limit_y < 0):
            raise ValueError

    def update_attitude(self, move: str):
        """
        Atualiza a orientação da sonda conforme rotação

        Args:
            move (str): Movimento de rotação da sonda. Opções: 'L' ou 'R'
        """
        index = Explorer.directions.index(self.attitude)
        if move == 'R':
            self.attitude = Explorer.directions[(index+1) % 4]
        else:
            self.attitude = Explorer.directions[index-1]

    def find_final_state(self) -> str:
        """
        Movimenta a sonda de acordo com as instruções

        Returns:
            str: O estado final da sonda, incluindo coordenadas e orientação
                no formato: 'X Y Orientação'. No caso de coordenadas inválidas,
                o retorno indica erro e o último estado registrado
        """
        for move in self.instructions:
            if move.upper() == 'M':
                try:
                    self.move()
                except ValueError:
                    return (f"ERRO! Última coordenada registrada: "
                            f"{self.pos_x} {self.pos_y} {self.attitude}")
            elif move.upper() in ['L', 'R']:
                self.update_attitude(move.upper())
        return f"{self.pos_x} {self.pos_y} {self.attitude}"
