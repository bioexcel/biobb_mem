from biobb_common.tools import test_fixtures as fx
from biobb_mem.gromacs.gmx_order import gmx_order


class TestGMXOrder():
    def setup_class(self):
        fx.test_setup(self, 'gmx_order')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_gmx_order(self):
        returncode = gmx_order(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_deuter_path'])
        assert fx.equal(self.paths['output_deuter_path'], self.paths['output_deuter_path'])
        assert fx.exe_success(returncode)
