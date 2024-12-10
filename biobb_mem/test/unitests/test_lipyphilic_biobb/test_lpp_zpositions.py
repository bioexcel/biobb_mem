from biobb_common.tools import test_fixtures as fx
from biobb_mem.lipyphilic_biobb.lpp_zpositions import lpp_zpositions


class TestLipyphilicPositionsDefault():
    def setup_class(self):
        fx.test_setup(self, 'lpp_zpositions')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_lipyphilic_positons_default(self):
        returncode = lpp_zpositions(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_positions_path'])
        assert fx.equal(self.paths['output_positions_path'], self.paths['output_positions_path'])
        assert fx.exe_success(returncode)
