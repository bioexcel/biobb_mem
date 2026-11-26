"""Common class of the gorder blocks of package biobb_mem."""
from biobb_common.generic.biobb_object import BiobbObject
import gorder


class GorderBase(BiobbObject):
    """Base class of the gorder blocks: the gorder analysis of the inputs with the analysis type of each block."""

    def analysis_type(self):
        """Go from the properties of the block to its gorder analysis type."""
        raise NotImplementedError

    def run(self) -> None:
        """Go from the structure and trajectory to the order parameters, in the format of the output extension."""
        out = self.sandbox_file("output_order_path")
        analysis = gorder.Analysis(
            structure=self.sandbox_file("input_top_path"),
            trajectory=self.sandbox_file("input_traj_path"),
            analysis_type=self.analysis_type(),
            output_yaml=out if out.endswith('.yaml') else None,
            output_csv=out if out.endswith('.csv') else None,
            output_xvg=out if out.endswith('.xvg') else None,
            handle_pbc=self.handle_pbc,
        )
        analysis.run().write()
