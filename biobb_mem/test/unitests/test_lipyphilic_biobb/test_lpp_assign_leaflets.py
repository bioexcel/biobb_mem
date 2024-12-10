from biobb_common.tools import test_fixtures as fx
from biobb_mem.lipyphilic_biobb.lpp_assign_leaflets import lpp_assign_leaflets


class TestLipyphilicLeafletsDefault():
    def setup_class(self):
        fx.test_setup(self, 'lpp_assign_leaflets')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_lipyphilic_leaflets_default(self):
        returncode = lpp_assign_leaflets(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_leaflets_path'])
        assert fx.equal(self.paths['output_leaflets_path'], self.paths['ref_output_leaflets_path'])
        assert fx.exe_success(returncode)
