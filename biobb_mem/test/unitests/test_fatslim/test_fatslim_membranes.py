from biobb_common.tools import test_fixtures as fx
from biobb_mem.fatslim.fatslim_membranes import fatslim_membranes


class TestFatslimMembranescDefault():
    def setup_class(self):
        fx.test_setup(self, 'fatslim_membranes')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_fatslim_membranes(self):
        returncode = fatslim_membranes(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_ndx_path'])
        assert fx.equal(self.paths['output_ndx_path'], self.paths['ref_output_ndx_path'])
        assert fx.exe_success(returncode)

    def test_fatslim_membranes_disable_sandbox(self):
        # The inputs are in the test data dir, not in the cwd
        properties = {**self.properties, 'disable_sandbox': True}
        returncode = fatslim_membranes(properties=properties, **self.paths)
        assert fx.not_empty(self.paths['output_ndx_path'])
        assert fx.equal(self.paths['output_ndx_path'], self.paths['ref_output_ndx_path'])
        assert fx.exe_success(returncode)
