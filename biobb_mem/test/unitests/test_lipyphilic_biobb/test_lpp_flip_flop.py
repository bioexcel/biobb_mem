from biobb_common.tools import test_fixtures as fx
from biobb_mem.lipyphilic_biobb.lpp_flip_flop import lpp_flip_flop


class TestLipyphilicLeafletsDefault():
    def setup_class(self):
        fx.test_setup(self, 'lpp_flip_flop')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_lipyphilic_leaflets_default(self):
        returncode = lpp_flip_flop(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_flip_flop_path'])
        assert fx.equal(self.paths['output_flip_flop_path'], self.paths['ref_output_flip_flop_path'])
        assert fx.exe_success(returncode)
