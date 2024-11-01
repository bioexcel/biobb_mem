#!/usr/bin/env python3

"""Module containing the Cpptraj Density class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools.file_utils import launchlogger
import MDAnalysis as mda
from lipyphilic.lib.assign_leaflets import AssignLeaflets as lipyAssignLeaflets
import pandas as pd
import numpy as np


class AssignLeaflets(BiobbObject):
    """
    | biobb_mem AssignLeaflets
    | Wrapper of the Lipyphilic AssignLeaflets module for assigning lipids to leaflets in a bilayer.
    | LiPyphilic is a Python package for analyzing MD simulations of lipid bilayers. The parameter names and defaults are the same as the ones in the official `Lipyphilic documentation <https://lipyphilic.readthedocs.io/en/latest/reference/analysis/leaflets.html>`_.

    Args:
        input_top_path (str): Path to the input structure or topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.pdb>`_. Accepted formats: crd (edam:3878), gro (edam:2033), mdcrd (edam:3878), mol2 (edam:3816), pdb (edam:1476), pdbqt (edam:1476), prmtop (edam:3880), psf (edam:3882), top (edam:3881), tpr (edam:2333), xml (edam:2332), xyz (edam:3887).
        input_traj_path (str): Path to the input trajectory to be processed. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.xtc>`_. Accepted formats: arc (edam:2333), crd (edam:3878), dcd (edam:3878), ent (edam:1476), gro (edam:2033), inpcrd (edam:3878), mdcrd (edam:3878), mol2 (edam:3816), nc (edam:3650), pdb (edam:1476), pdbqt (edam:1476), restrt (edam:3886), tng (edam:3876), trr (edam:3910), xtc (edam:3875), xyz (edam:3887).
        output_leaflets_path (str): Path to the output leaflet assignments. File type: output. `Sample file <https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/reference/lipyphilicBB/leaflets.csv>`_. Accepted formats: csv (edam:format_3752).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **start** (*int*) - (None) Starting frame for slicing.
            * **stop** (*int*) - (None) Ending frame for slicing.
            * **step** (*int*) - (None) Step for slicing.
            * **lipid_sel** (*str*) - ("all") Selection string for the lipids in a membrane. The selection should cover **all** residues in the membrane, including cholesterol.
            * **midplane_sel** (*str*) - (None) Selection string for residues that may be midplane. Any residues not in this selection will be assigned to a leaflet regardless of its proximity to the midplane. The default is `None`, in which case all lipids will be assigned to either the upper or lower leaflet.
            * **midplane_cutoff** (*float*) - (0) Minimum distance in *z* an atom must be from the midplane to be assigned to a leaflet rather than the midplane. The default is `0`, in which case all lipids will be assigned to either the upper or lower leaflet. Must be non-negative.
            * **n_bins** (*int*) - (1) Number of bins in *x* and *y* to use to create a grid of membrane patches. Local membrane midpoints are computed for each patch, and lipids assigned a leaflet based on the distance to their local membrane midpoint. The default is `1`, which is equivalent to computing a single global midpoint.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mem.lipyphilicBB.assign_leaflets import assign_leaflets
            prop = {
                'lipid_sel': 'name GL1 GL2 ROH',
            }
            assign_leaflets(input_top_path='/path/to/myTopology.tpr',
                        input_traj_path='/path/to/myTrajectory.xtc',
                        output_leaflets_path='/path/to/leaflets.csv',
                        properties=prop)

    Info:
        * wrapped_software:
            * name: Lipyphilic
            * version: 0.10.0
            * license: GPL-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_top_path, input_traj_path, output_leaflets_path,
                 properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_top_path": input_top_path, "input_traj_path": input_traj_path},
            "out": {"output_leaflets_path": output_leaflets_path}
        }

        # Properties specific for BB
        self.lipid_sel = properties.get('lipid_sel', 'all')
        self.midplane_sel = properties.get('midplane_sel', None)
        self.midplane_cutoff = properties.get('midplane_cutoff', None)
        self.n_bins = properties.get('n_bins', 1)
        self.start = properties.get('start', None)
        self.stop = properties.get('stop', None)
        self.step = properties.get('step', None)
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`AssignLeaflets <lipyphilicBB.assign_leaflets.AssignLeaflets>` lipyphilicBB.assign_leaflets.AssignLeaflets object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Load the trajectory
        u = mda.Universe(self.stage_io_dict["in"]["input_top_path"], self.stage_io_dict["in"]["input_traj_path"])

        # Create AssignLeaflets object
        leaflets = lipyAssignLeaflets(
            universe=u,
            lipid_sel=self.lipid_sel,
            midplane_sel=self.midplane_sel,
            midplane_cutoff=self.midplane_cutoff,
            n_bins=self.n_bins
        )

        # Run the analysis
        leaflets.run(
            start=self.start,
            stop=self.stop,
            step=self.step
        )
        # Save the results
        frames = leaflets.leaflets.shape[1]
        resnames = np.repeat(leaflets.membrane.resnames, frames)
        resindices = np.tile(leaflets.membrane.resnums, frames)
        frame_numbers = np.repeat(np.arange(frames), leaflets.membrane.n_residues)

        df = pd.DataFrame({
            'resname': resnames,
            'resindex': resindices,
            'frame': frame_numbers,
            'leaflet_index': leaflets.leaflets.T.flatten()
        })

        # Save the DataFrame to a CSV file
        df.to_csv(self.stage_io_dict["out"]["output_leaflets_path"], index=False)

        # Copy files to host
        self.copy_to_host()
        # remove temporary folder(s)
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir")
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def assign_leaflets(input_top_path: str, input_traj_path: str, output_leaflets_path: str = None, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`AssignLeaflets <lipyphilicBB.assign_leaflets.AssignLeaflets>` class and
    execute the :meth:`launch() <lipyphilicBB.assign_leaflets.AssignLeaflets.launch>` method."""

    return AssignLeaflets(input_top_path=input_top_path,
                          input_traj_path=input_traj_path,
                          output_leaflets_path=output_leaflets_path,
                          properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Assign lipids to leaflets in a bilayer.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_top_path', required=True, help='Path to the input structure or topology file. Accepted formats: crd, gro, mdcrd, mol2, pdb, pdbqt, prmtop, psf, top, tpr, xml, xyz.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the input trajectory to be processed. Accepted formats: arc, crd, dcd, ent, gro, inpcrd, mdcrd, mol2, nc, pdb, pdbqt, restrt, tng, trr, xtc, xyz.')
    required_args.add_argument('--output_leaflets_path', required=True, help='Path to the output processed analysis.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    assign_leaflets(input_top_path=args.input_top_path,
                    input_traj_path=args.input_traj_path,
                    output_leaflets_path=args.output_leaflets_path,
                    properties=properties)


if __name__ == '__main__':
    main()
