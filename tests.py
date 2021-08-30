import unittest
from explorer import Explorer


class TestMovingExplorer(unittest.TestCase):
    def setUp(self):
        self.data_working = [
            ((5, 5), {
                'init_x': 1, 'init_y': 2, 'init_att': 'N',
                'instructions': 'LMLMLMLMM'}, '1 3 N'),
            ((5, 5), {
                'init_x': 3, 'init_y': 3, 'init_att': 'E',
                'instructions': 'MMRMMRMRRM'}, '5 1 E'),
            ((8, 20), {
                'init_x': 3, 'init_y': 3, 'init_att': 'N',
                'instructions': 'MMMMMMMMMMMMMRMMRMMMMM'}, '5 11 S'),
            ((1, 1), {
                'init_x': 0, 'init_y': 0, 'init_att': 'N',
                'instructions': 'MRMLLMLMLMLM'}, '1 1 N')
        ]
        self.data_wrong_parameters = [
            ((5, 5), {
                'init_x': 3, 'init_y': 3, 'init_att': 'E',
                'instructions': 'MMKMMRMRRM'}),
            ((3, 3), {
                'init_x': 0, 'init_y': -1, 'init_att': 'N',
                'instructions': 'MMLMMLMLM'})
        ]
        self.data_out_of_rect = [
            ((3, 3), {
                'init_x': 0, 'init_y': 0, 'init_att': 'N',
                'instructions': 'MMLMMLMLM'},
                'ERRO! Última coordenada registrada: -1 2 W'),
            ((3, 3), {
                'init_x': 3, 'init_y': 3, 'init_att': 'N',
                'instructions': 'MMLMMLMLM'},
                'ERRO! Última coordenada registrada: 3 4 N')
        ]
        self.data_raises_error = [(0, 5), (5, 'M'), (8, -20), (0, 0)]

    def test_working(self):
        for rect_coord, expl_data, expected_result in self.data_working:
            Explorer.set_limits(rect_coord)
            explorer = Explorer.create_explorer(**expl_data)
            result = explorer.find_final_state()
            self.assertEqual(result, expected_result)

    def test_wrong_parameters(self):
        for rect_coord, explorer_data in self.data_wrong_parameters:
            Explorer.set_limits(rect_coord)
            explorer = Explorer.create_explorer(**explorer_data)
            self.assertEqual(explorer, None)

    def test_out_of_rect(self):
        for rect_coord, expl_data, expected_result in self.data_out_of_rect:
            Explorer.set_limits(rect_coord)
            explorer = Explorer.create_explorer(**expl_data)
            result = explorer.find_final_state()
            self.assertEqual(result, expected_result)

    def test_raises_error(self):
        for rect_coord in self.data_raises_error:
            self.assertRaises(ValueError, Explorer.set_limits, rect_coord)


if __name__ == '__main__':
    unittest.main()
