#!/usr/bin/env python3

"""Module containing the FATSLiM Area per Lipid class and the command line interface."""
from pathlib import Path, PurePath
import sys
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_mem.fatslim.common import ignore_no_box, move_output_file
import MDAnalysis as mda


class FatslimAPL(BiobbObject):
    """
    | biobb_mem FatslimAPL
    | Wrapper of the `FATSLiM area per lipid <https://pythonhosted.org/fatslim/documentation/apl.html>`_ module for area per lipid calculation.
    | FATSLiM is designed to provide efficient and robust analysis of physical parameters from MD trajectories, with a focus on processing large trajectory files quickly.

    Args:
        input_top_path (str): Path to the input topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str) (Optional): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_ndx_path (str) (Optional): Path to the input index NDX file for lipid headgroups and the interacting group. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/headgroups.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_csv_path (str): Path to the output CSV file. File type: output. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/fatslim/apl.csv>`_. Accepted formats: csv (edam:format_3752).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **lipid_selection** (*str*) - ("not protein and element P") Headgroups MDAnalysis `selection <https://docs.mdanalysis.org/stable/documentation_pages/selections.html>`_.
            * **protein_selection** (*str*) - ("protein and not element H") Protein selection interacting with the membrane.
            * **cutoff** (*float*) - (3) This option allows user to specify the cutoff distance (in nm) to be used when performing the neighbor search needed by the APL calculation algorithm
            * **limit** (*float*) - (10) This option allows user to specify the upper limit (in nm2) for a valid area per lipid value.
            * **begin_frame** (*int*) - (-1) First frame index to be used for analysis.
            * **end_frame** (*int*) - (-1) Last frame index to be used for analysis.
            * **ignore_no_box** (*bool*) - (False) Ignore the absence of box information in the topology. If the topology does not contain box information, the box will be set to the minimum and maximum positions of the atoms.
            * **binary_path** (*str*) - ("fatslim") Path to the fatslim executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('afandiadib/ambertools:serial') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mem.fatslim.fatslim_apl import fatslim_apl
            prop = {
                'lipid_selection': '(resname DPPC and name P8)',
                'cutoff': 3
            }
            fatslim_apl(input_top_path='/path/to/myTopology.tpr',
                              input_traj_path='/path/to/myTrajectory.xtc',
                              output_csv_path='/path/to/newIndex.ndx',
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

    def __init__(self, input_top_path: str, output_csv_path: str, input_traj_path: str | None = None, input_ndx_path: str | None = None, properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`FatslimAPL <fatslim.fatslim_apl.FatslimAPL>` object."""

        unique_dir = self.stage_io_dict.get("unique_dir", "")

        # MDAnalysis runs in the host, so read the original input files
        host_top_path = self.io_dict["in"]["input_top_path"]
        host_traj_path = self.io_dict["in"].get("input_traj_path")

        # Create index file using MDAnalysis
        u = mda.Universe(topology=host_top_path, coordinates=host_traj_path)
        ignore_no_box(u, self.ignore_no_box, self.out_log, self.global_log)

        # Build the index to select the atoms from the membrane
        if self.stage_io_dict["in"].get('input_ndx_path', None):
            tmp_ndx = self.sandbox_file("input_ndx_path")
        else:
            tmp_ndx = str(Path(unique_dir).joinpath('_apl_inp.ndx'))
            with mda.selections.gromacs.SelectionWriter(tmp_ndx, mode='w') as ndx:
                ndx.write(u.select_atoms(self.lipid_selection), name='headgroups')
                ndx.write(u.select_atoms(self.protein_selection), name='protein')

        if self.stage_io_dict["in"]["input_top_path"].endswith('gro'):
            cfg = self.sandbox_file("input_top_path")

        else:
            # Convert topology .gro and add box dimensions if not available in the topology
            cfg = str(Path(unique_dir).joinpath('_output.gro'))
            # Save as GRO file with box information
            u.atoms.write(cfg)

        tmp_csv = str(Path(unique_dir).joinpath('_out.csv'))

        if not self.container_path and PurePath(self.binary_path).name == "fatslim":
            # FATSLiM 0.2.2 uses deprecated NumPy aliases removed in modern NumPy versions.
            fatslim_compat = Path(unique_dir).joinpath('fatslim_numpy_compat.py')
            with open(fatslim_compat, 'w') as compat_script:
                compat_script.write('import sys\n')
                compat_script.write('import numpy as np\n')
                compat_script.write('if not hasattr(np, "int"):\n')
                compat_script.write('    np.int = int\n')
                compat_script.write('from fatslimlib import main\n')
                compat_script.write('sys.exit(main(sys.argv[1:]))\n')
            binary_cmd = [sys.executable, self.staged_path(fatslim_compat)]
        else:
            binary_cmd = [self.binary_path]

        # Build command
        self.cmd = binary_cmd + [
            "apl",
            "-n", self.staged_path(tmp_ndx),
            "-c", self.staged_path(cfg),
            "--export-apl-raw", self.staged_path(tmp_csv),
            "--apl-cutoff", str(self.cutoff),
            "--apl-limit", str(self.limit),
            "--begin-frame", str(self.begin_frame),
            "--end-frame", str(self.end_frame)
        ]

        # Run Biobb block
        self.run_biobb()
        staged_output_csv = self.sandbox_file("output_csv_path")
        move_output_file(tmp_csv, staged_output_csv,
                         self.out_log, self.global_log)


fatslim_apl = launcher(FatslimAPL)

if __name__ == '__main__':
    FatslimAPL.main()
