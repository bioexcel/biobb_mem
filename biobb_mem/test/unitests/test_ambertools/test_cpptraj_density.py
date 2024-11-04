from biobb_common.tools import test_fixtures as fx
from biobb_mem.ambertools.cpptraj_density import cpptraj_density


class TestCpptrajDensityDefault():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


class TestCpptrajDensityMask():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_mask')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)


class TestCpptrajDensityComplex():
    def setup_class(self):
        fx.test_setup(self, 'cpptraj_density_complex')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_cpptraj_density(self):
        returncode = cpptraj_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_cpptraj_path'])
        assert fx.equal(self.paths['output_cpptraj_path'], self.paths['ref_output_cpptraj_path'])
        assert fx.exe_success(returncode)
