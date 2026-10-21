from biobb_common.tools import test_fixtures as fx
from biobb_mem.fatslim.fatslim_apl import fatslim_apl
import pytest
import sys


class TestFatslimAPLcDefaultDocker():
    def setup_class(self):
        fx.test_setup(self, 'fatslim_apl_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_fatslim_apl_docker(self):
        returncode = fatslim_apl(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_csv_path'])
        assert fx.equal(self.paths['output_csv_path'], self.paths['ref_output_csv_path'])
        assert fx.exe_success(returncode)

    def test_fatslim_apl_docker_disable_sandbox(self):
        # The inputs are in the test data dir, not in the cwd
        properties = {**self.properties, 'disable_sandbox': True}
        returncode = fatslim_apl(properties=properties, **self.paths)
        assert fx.not_empty(self.paths['output_csv_path'])
        assert fx.equal(self.paths['output_csv_path'], self.paths['ref_output_csv_path'])
        assert fx.exe_success(returncode)


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestFatslimAPLcDefaultSingularity():
    def setup_class(self):
        fx.test_setup(self, 'fatslim_apl_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_fatslim_apl_singularity(self):
        returncode = fatslim_apl(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_csv_path'])
        assert fx.equal(self.paths['output_csv_path'], self.paths['ref_output_csv_path'])
        assert fx.exe_success(returncode)

    def test_fatslim_apl_singularity_disable_sandbox(self):
        # The inputs are in the test data dir, not in the cwd
        properties = {**self.properties, 'disable_sandbox': True}
        returncode = fatslim_apl(properties=properties, **self.paths)
        assert fx.not_empty(self.paths['output_csv_path'])
        assert fx.equal(self.paths['output_csv_path'], self.paths['ref_output_csv_path'])
        assert fx.exe_success(returncode)
