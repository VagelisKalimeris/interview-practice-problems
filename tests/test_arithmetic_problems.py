from problems.arithmeric_problems import *


class TestPowerRaise:
    def test_powers(self):
        assert power(3, 1) == 3
        assert power(3, 2) == 9
        assert power(2, 3) == 8
        assert power(2, 8) == 256

    def test_edge_powers(self):
        assert power(255, 0) == 1
        assert power(2555, 1) == 2555
        assert power(0, 0) == 0
        assert power(0, 1) == 0
        assert power(1, 1) == 1


