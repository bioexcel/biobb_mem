"""Common class of the FATSLiM blocks of package biobb_mem."""
from pathlib import Path, PurePath
import sys
import MDAnalysis as mda
from biobb_common.generic.biobb_object import BiobbObject
from biobb_mem.common import ignore_no_box


class FatslimBase(BiobbObject):
    """Base class of the FATSLiM blocks: the input files of fatslim and the start of its command line."""

    def fatslim_cmd(self, tmp_dir: Path, command: str, groups: dict[str, str],
                    frame: int | None = None) -> tuple[mda.Universe, list[str]]:
        """Go from a fatslim command to the universe of the inputs and the start of the command line, with the
        index (input_ndx_path or the **groups** selections) and the files fatslim reads written in **tmp_dir**.
        fatslim reads the whole trajectory, or only its **frame** when given."""
        # MDAnalysis runs in the host, so it reads the original input files
        top_path = self.io_dict["in"]["input_top_path"]
        traj_path = self.io_dict["in"].get("input_traj_path")
        u = mda.Universe(top_path, traj_path) if traj_path else mda.Universe(top_path)
        box_set = ignore_no_box(u, self.ignore_no_box, self.out_log, self.global_log)

        if self.io_dict["in"].get("input_ndx_path"):
            ndx = self.sandbox_file("input_ndx_path")
        else:
            ndx = str(tmp_dir / "groups.ndx")
            with mda.selections.gromacs.SelectionWriter(ndx, mode="w") as ndx_file:
                for name, selection in groups.items():
                    ndx_file.write(u.select_atoms(selection), name=name)

        # fatslim reads the topology from a GRO file with the box
        if frame is not None:
            u.trajectory[frame]
        conf = tmp_dir / "conf.gro"
        u.atoms.write(str(conf))

        if self.container_path or PurePath(self.binary_path).name != "fatslim":
            cmd = [self.binary_path]
        else:
            # FATSLiM 0.2.2 uses NumPy aliases removed in modern NumPy versions
            compat = tmp_dir / "fatslim_numpy_compat.py"
            compat.write_text("import sys\nimport numpy as np\nif not hasattr(np, 'int'):\n    np.int = int\n"
                              "from fatslimlib import main\nsys.exit(main(sys.argv[1:]))\n")
            cmd = [sys.executable, self.staged_path(compat)]
        cmd += [command, "-n", self.staged_path(ndx), "-c", self.staged_path(conf)]

        if traj_path and frame is None:
            traj = self.sandbox_file("input_traj_path")
            # fatslim reads xtc, trr and gro files with a box; a container sees only the files of its volume
            if box_set or PurePath(traj).suffix.lower() not in (".xtc", ".trr", ".gro") or (
                    self.container_path and Path(self.staged_path(traj)).is_absolute()):
                traj = str(tmp_dir / "traj.xtc")
                with mda.Writer(traj, u.atoms.n_atoms) as writer:
                    for _ in u.trajectory:
                        writer.write(u.atoms)
            cmd += ["-t", self.staged_path(traj)]
        return u, cmd
