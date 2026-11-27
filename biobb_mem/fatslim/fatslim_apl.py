#!/usr/bin/env python3

"""Module containing the FATSLiM Area per Lipid class and the command line interface."""
from pathlib import Path
import csv
from biobb_common.generic.biobb_object import launcher
from biobb_common.tools import file_utils as fu
from biobb_mem.fatslim.common import FatslimBase


class FatslimAPL(FatslimBase):
    """
    | biobb_mem FatslimAPL
    | Wrapper of the `FATSLiM area per lipid <https://pythonhosted.org/fatslim/documentation/apl.html>`_ module for area per lipid calculation.
    | FATSLiM is designed to provide efficient and robust analysis of physical parameters from MD trajectories, with a focus on processing large trajectory files quickly.

    Args:
        input_top_path (str): Path to the input topology file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.pdb>`_. Accepted formats: tpr (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), brk (edam:format_2033), ent (edam:format_1476).
        input_traj_path (str) (Optional): Path to the GROMACS trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/A01JD.xtc>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), cpt (edam:format_2333), gro (edam:format_2033), g96 (edam:format_2033), pdb (edam:format_1476), tng (edam:format_3876).
        input_ndx_path (str) (Optional): Path to the input index NDX file for lipid headgroups and the interacting group. File type: input. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/data/A01JD/headgroups.ndx>`_. Accepted formats: ndx (edam:format_2033).
        output_csv_path (str): Path to the output CSV file with the area of each lipid in each analysed frame. File type: output. `Sample file <https://github.com/bioexcel/biobb_mem/raw/main/biobb_mem/test/reference/fatslim/apl.csv>`_. Accepted formats: csv (edam:format_3752).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **lipid_selection** (*str*) - ("not protein and element P") Headgroups MDAnalysis `selection <https://docs.mdanalysis.org/stable/documentation_pages/selections.html>`_.
            * **protein_selection** (*str*) - ("protein and not element H") Protein selection interacting with the membrane.
            * **cutoff** (*float*) - (3) This option allows user to specify the cutoff distance (in nm) to be used when performing the neighbor search needed by the APL calculation algorithm
            * **limit** (*float*) - (10) This option allows user to specify the upper limit (in nm2) for a valid area per lipid value.
            * **begin_frame** (*int*) - (-1) Index of the first trajectory frame analysed (-1: the first frame).
            * **end_frame** (*int*) - (-1) Index of the trajectory frame where the analysis stops, not analysed (-1: up to the last frame).
            * **ignore_no_box** (*bool*) - (False) Ignore the absence of box information in the trajectory. If the trajectory does not contain box information, the box will be set to the minimum and maximum positions of the atoms in the trajectory.
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
                              output_csv_path='/path/to/apl.csv',
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
        tmp_dir = Path(self.create_tmp_dir())
        _, cmd = self.fatslim_cmd(tmp_dir, "apl", {"headgroups": self.lipid_selection, "protein": self.protein_selection})
        self.cmd = cmd + [
            "--begin-frame", str(self.begin_frame),
            "--end-frame", str(self.end_frame),
            "--export-apl-raw", self.staged_path(tmp_dir / "apl.csv"),
            "--apl-cutoff", str(self.cutoff),
            "--apl-limit", str(self.limit)
        ]
        self.run_biobb()

        # fatslim writes one CSV per analysed frame: apl_frame_00000.csv for the first one
        frame_csvs = sorted(tmp_dir.glob("apl_frame_*.csv"))
        if not frame_csvs:
            fu.log("No area per lipid file: FATSLiM analysed no frame or failed.", self.out_log, self.global_log)
            return
        first_frame = max(0, self.begin_frame)
        with open(self.sandbox_file("output_csv_path"), "w", newline="") as output_csv:
            writer = csv.writer(output_csv)
            for i, frame_csv in enumerate(frame_csvs):
                with open(frame_csv, newline="") as f:
                    header, *rows = csv.reader(f)
                if i == 0:
                    writer.writerow(["frame", *header])
                frame = first_frame + int(frame_csv.stem.rsplit("_", 1)[1])
                writer.writerows([frame, *row] for row in rows)


fatslim_apl = launcher(FatslimAPL)

if __name__ == '__main__':
    FatslimAPL.main()
