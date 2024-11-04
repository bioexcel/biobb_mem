from biobb_common.tools import test_fixtures as fx
from biobb_mem.chap.chap_run import chap_run


class TestChapDefault():
    def setup_class(self):
        fx.test_setup(self, 'chap_run')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_chap_default(self):
        returncode = chap_run(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_obj_path'])
        assert fx.equal(self.paths['output_obj_path'], self.paths['ref_output_obj_path'])
        assert fx.exe_success(returncode)
