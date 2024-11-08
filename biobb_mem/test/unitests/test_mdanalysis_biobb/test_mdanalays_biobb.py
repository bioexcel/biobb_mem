from biobb_common.tools import test_fixtures as fx
from biobb_mem.mdanalysis_biobb.mda_hole import mda_hole


class TestMDAHole():
    def setup_class(self):
        fx.test_setup(self, 'mda_hole')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_mda_hole_default(self):
        returncode = mda_hole(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_hole_path'])
        assert fx.equal(self.paths['output_hole_path'], self.paths['ref_output_hole_path'])
        assert fx.exe_success(returncode)
