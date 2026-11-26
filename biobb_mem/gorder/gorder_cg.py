#!/usr/bin/env python3

"""Module containing the gorder coarse-grained class and the command line interface."""
from biobb_common.generic.biobb_object import BiobbObject, launcher
import gorder


class GorderCG(BiobbObject):
    """
    | biobb_mem GorderCG
    | Wrapper of the gorder coarse-grained module for computing lipid order parameters per atom for carbon tails.
    | `gorder <https://ladme.github.io/gorder-manual/cgorder_basics.html>`_ uses `GSL <https://ladme.github.io/gsl-guide/>`_ for all its selections.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/CG/cg_test.tpr>`_. Accepted formats: tpr (edam:format_2333).
        input_traj_path (str): Path to the input trajectory to be processed. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/CG/cg_test.xtc>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), gro (edam:format_2033).
        output_order_path (str): Path to results of the order analysis. File type: output. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/gorder/order_cg.yaml>`_. Accepted formats: yaml (edam:format_3570), xvg (edam:format_2330), csv (edam:format_3752).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **beads** (*str*) - ("@membrane") Selection query specifying the beads to be used in the analysis.
            * **handle_pbc** (*bool*) - (True) If False, ignores periodic boundary conditions (PBC).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mem.gorder.gorder_cg import gorder_cg
            prop = {
                'handle_pbc': False
            }
            gorder_cg(input_top_path='/path/to/myTopology.tpr',
                      input_traj_path='/path/to/myTrajectory.xtc',
                      output_order_path='/path/to/orderAnalysis.yaml',
                      properties=prop)

    Info:
        * wrapped_software:
            * name: gorder
            * version: 1.1.0
            * license: MIT
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self,
                 input_top_path: str,
                 input_traj_path: str,
                 output_order_path: str | None = None,
                 properties: dict | None = None,
                 **kwargs) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`GorderCG <gorder.gorder_cg.GorderCG>` object."""

        out = self.stage_io_dict["out"]["output_order_path"]
        # Run Biobb block
        analysis = gorder.Analysis(
            structure=self.stage_io_dict["in"]["input_top_path"],
            trajectory=self.stage_io_dict["in"]["input_traj_path"],
            analysis_type=gorder.analysis_types.CGOrder(self.beads),
            output_yaml=out if out.endswith('.yaml') else None,
            output_csv=out if out.endswith('.csv') else None,
            output_xvg=out if out.endswith('.xvg') else None,
            handle_pbc=False,
        )

        results = analysis.run()
        results.write()


gorder_cg = launcher(GorderCG)

if __name__ == '__main__':
    GorderCG.main()
