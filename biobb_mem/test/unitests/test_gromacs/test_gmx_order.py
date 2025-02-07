from biobb_common.tools import test_fixtures as fx
from biobb_mem.gromacs.gmx_order import gmx_order
import numpy as np


def compare_xvg(file_a: str, file_b: str, percent_tolerance: float = 1.0) -> bool:
    """ Compare two files using size """
    print("Comparing size of both files:")
    print(f"     FILE_A: {file_a}")
    print(f"     FILE_B: {file_b}")
    arrays_tuple_a = np.loadtxt(file_a, comments=["#", "@"], unpack=True)
    arrays_tuple_b = np.loadtxt(file_b, comments=["#", "@"], unpack=True)
    for array_a, array_b in zip(arrays_tuple_a, arrays_tuple_b):
        if not np.allclose(array_a, array_b, rtol=percent_tolerance / 100):
            return False
    return True


class TestGMXOrder():
    def setup_class(self):
        fx.test_setup(self, 'gmx_order')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_gmx_order(self):
        returncode = gmx_order(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_deuter_path'])
        assert fx.compare_xvg(self.paths['output_deuter_path'], self.paths['output_deuter_path'])
        assert fx.exe_success(returncode)
