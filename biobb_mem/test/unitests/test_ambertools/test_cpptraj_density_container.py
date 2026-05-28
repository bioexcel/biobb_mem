from biobb_common.tools import test_fixtures as fx
from biobb_mem.ambertools.cpptraj_density import cpptraj_density
import pytest
import sys


class TestCpptrajDensityDefaultDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density_docker(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


class TestCpptrajDensityMaskDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_mask_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density_mask_docker(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


class TestCpptrajDensityComplexDocker():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_complex_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density_complex_docker(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestCpptrajDensityDefaultSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density_singularity(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestCpptrajDensityMaskSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_mask_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density_mask_singularity(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestCpptrajDensityComplexSingularity():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_complex_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density_complex_singularity(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)