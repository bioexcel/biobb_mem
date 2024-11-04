from biobb_common.tools import test_fixtures as fx
from biobb_mem.lipyphilicBB.assign_leaflets import assign_leaflets


class TestLipyphilicDefault():
    def setup_class(self):
        fx.test_setup(self, 'assign_leaflets')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_lipyphilic_default(self):
        returncode = assign_leaflets(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_leaflets_path'])
        assert fx.equal(self.paths['output_leaflets_path'], self.paths['ref_output_leaflets_path'])
        assert fx.exe_success(returncode)
