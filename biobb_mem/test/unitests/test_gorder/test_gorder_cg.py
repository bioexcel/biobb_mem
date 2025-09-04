from biobb_common.tools import test_fixtures as fx
from biobb_mem.gorder.gorder_cg import gorder_cg


class TestGOrderCG():
    def setup_class(self):
        fx.test_setup(self, 'gorder_cg')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_gorder_cg(self):
        returncode = gorder_cg(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_order_path'])
        assert fx.equal(
            self.paths['output_order_path'],
            self.paths['ref_output_order_path'],
            ignore_list=[0])
        assert fx.exe_success(returncode)
