from biobb_common.tools import test_fixtures as fx
from biobb_mem.fatslim.fatslim_membranes import fatslim_membranes
import pytest
import sys


class TestFatslimMembranescDefaultDocker():
    def setup_class(self):
        fx.test_setup(self, 'fatslim_membranes_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_fatslim_membranes_docker(self):
        returncode = fatslim_membranes(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_ndx_path'])
        assert fx.equal(self.paths['output_ndx_path'], self.paths['ref_output_ndx_path'])
        assert fx.exe_success(returncode)

    def test_fatslim_membranes_docker_disable_sandbox(self):
        # The inputs are in the test data dir, not in the cwd
        properties = {**self.properties, 'disable_sandbox': True}
        returncode = fatslim_membranes(properties=properties, **self.paths)
        assert fx.not_empty(self.paths['output_ndx_path'])
        assert fx.equal(self.paths['output_ndx_path'], self.paths['ref_output_ndx_path'])
        assert fx.exe_success(returncode)


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestFatslimMembranescDefaultSingularity():
    def setup_class(self):
        fx.test_setup(self, 'fatslim_membranes_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_fatslim_membranes_singularity(self):
        returncode = fatslim_membranes(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_ndx_path'])
        assert fx.equal(self.paths['output_ndx_path'], self.paths['ref_output_ndx_path'])
        assert fx.exe_success(returncode)

    def test_fatslim_membranes_singularity_disable_sandbox(self):
        # The inputs are in the test data dir, not in the cwd
        properties = {**self.properties, 'disable_sandbox': True}
        returncode = fatslim_membranes(properties=properties, **self.paths)
        assert fx.not_empty(self.paths['output_ndx_path'])
        assert fx.equal(self.paths['output_ndx_path'], self.paths['ref_output_ndx_path'])
        assert fx.exe_success(returncode)
