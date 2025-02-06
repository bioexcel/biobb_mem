from biobb_common.tools import test_fixtures as fx
from biobb_mem.fatslim.fatslim_apl import fatslim_apl


class TestFatslimAPLcDefault():
    def setup_class(self):
        fx.test_setup(self, 'fatslim_apl')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_fatslim_apl(self):
        returncode = fatslim_apl(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_csv_path'])
        assert fx.equal(self.paths['output_csv_path'], self.paths['ref_output_csv_path'])
        assert fx.exe_success(returncode)
