#!/usr/bin/env python3

"""Module containing the FATSLiM Membranes class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools.file_utils import launchlogger
import MDAnalysis as mda
import os


class FatslimMembranes(BiobbObject):
    """
    | biobb_mem FatslimMembranes
    | Wrapper of the `FATSLiM membranes <https://pythonhosted.org/fatslim/documentation/leaflets.html>`_ module for leaflet and membrane identification.
    | FATSLiM is designed to provide efficient and robust analysis of physical parameters from MD trajectories, with a focus on processing large trajectory files quickly.

    Args:
        input_top_path (str): Path to the input topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.pdb>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.xtc>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        output_ndx_path (str): Path to the output index NDX file. File type: output. `Sample file <https://github.com/bioexcel/biobb_mem/raw/master/biobb_mem/test/data/A01JD/A01JD.ndx>`_. Accepted formats: ndx (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **selection** (*str*) - ("resname DPPC and element P") Molecules used in the identification using MDAnalysis selection language.
            * **cutoff** (*float*) - (2) Cutoff distance (in nm) to be used when leaflet identification is performed.
            * **binary_path** (*str*) - ("fatslim") Path to the fatslim executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mem.fatslim.fatslim_membranes import fatslim_membranes
            prop = {
                'selection': '(resname DPPC and name P8)',
                'cutoff': 2.2
            }
            fatslim_membranes(input_top_path='/path/to/myTopology.tpr',
                              input_traj_path='/path/to/myTrajectory.xtc',
                              output_ndx_path='/path/to/newIndex.ndx',
                              properties=prop)

    Info:
        * wrapped_software:
            * name: FATSLiM
            * version: 0.2.2
            * license: GNU
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_top_path, input_traj_path, output_ndx_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_top_path": input_top_path,
                   "input_traj_path": input_traj_path},
            "out": {"output_ndx_path": output_ndx_path}
        }

        # Properties specific for BB
        self.selection = properties.get('selection', "resname DPPC or resname POPC) and element P")
        self.cutoff = properties.get('cutoff', 2.2)
        self.binary_path = properties.get('binary_path', 'fatslim')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`FatslimMembranes <fatslim.fatslim_membranes.FatslimMembranes>` fatslim.fatslim_membranes.FatslimMembranes object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Create index file using MDAnalysis
        u = mda.Universe(self.stage_io_dict["in"]["input_top_path"],
                         self.stage_io_dict["in"]["input_traj_path"])
        # Build the index to select the atoms from the membrane
        tmp_ndx = 'headgroups.ndx'
        with mda.selections.gromacs.SelectionWriter(tmp_ndx, mode='w') as ndx:
            ndx.write(u.select_atoms(self.selection), name='headgroups')
        # Convert topology .gro and add box dimensions if not available in the topology
        tmp_gro = 'output.gro'
        self.cmd = ['gmx', 'editconf',
                    '-f', self.stage_io_dict["in"]["input_top_path"],
                    '-o ', tmp_gro,
                    '-box', ' '.join(map(str, u.dimensions[:3]))
                    ]

        # Build command
        self.cmd.extend([
            ';',
            self.binary_path, "membranes",
            "-c", 'output.gro',
            "-n", tmp_ndx,
            "--output-index", 'output.ndx',
            "--cutoff", str(self.cutoff)
        ])

        # Run Biobb block
        self.run_biobb()
        os.rename('output_0000.ndx', self.stage_io_dict["out"]["output_ndx_path"])
        # Copy files to host
        self.copy_to_host()

        # Remove temporary files
        self.tmp_files.append(self.stage_io_dict.get("unique_dir"))
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def fatslim_membranes(input_top_path: str, input_traj_path: str, output_ndx_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`FatslimMembranes <fatslim.fatslim_membranes.FatslimMembranes>` class and
    execute the :meth:`launch() <fatslim.fatslim_membranes.FatslimMembranes.launch>` method."""

    return FatslimMembranes(input_top_path=input_top_path,
                            input_traj_path=input_traj_path,
                            output_ndx_path=output_ndx_path,
                            properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Calculates the density along an axis of a given cpptraj compatible trajectory.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_top_path', required=True, help='Path to the input structure or topology file. Accepted formats: ent, gro, pdb, tpr.')
    required_args.add_argument('--input_traj_path', required=True, help='Path to the input trajectory to be processed. Accepted formats: gro, pdb, tng, trr, xtc.')
    required_args.add_argument('--output_ndx_path', required=True, help='Path to the GROMACS index file. Accepted formats: ndx')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    fatslim_membranes(input_top_path=args.input_top_path,
                      output_ndx_path=args.output_ndx_path,
                      properties=properties)


if __name__ == '__main__':
    main()
