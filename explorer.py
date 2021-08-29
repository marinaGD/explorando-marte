
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
