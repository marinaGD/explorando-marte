
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
                    return (f"ERRO! Ultima coordenada registrada: "
                            f"{self.pos_x} {self.pos_y} {self.attitude}")
            elif move.upper() in ['L', 'R']:
                self.update_attitude(move.upper())
        return f"{self.pos_x} {self.pos_y} {self.attitude}"
