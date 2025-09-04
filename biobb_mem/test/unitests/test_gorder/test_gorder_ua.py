from biobb_common.tools import test_fixtures as fx
from biobb_mem.gorder.gorder_ua import gorder_ua


class TestGOrderUA():
    def setup_class(self):
        fx.test_setup(self, 'gorder_ua')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_gorder_ua(self):
        returncode = gorder_ua(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_order_path'])
        assert fx.equal(
            self.paths['output_order_path'],
            self.paths['ref_output_order_path'],
            ignore_list=[0])
        assert fx.exe_success(returncode)
