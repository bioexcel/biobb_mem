""" Common functions for package biobb_mem.lipyphilic_biobb """
import numpy as np
from MDAnalysis.transformations import translate, set_dimensions
from biobb_common.tools import file_utils as fu


def set_box(u):
    """Set the box dimensions of the universe based on the positions of the atoms."""
    # Initialize min and max positions with extreme values
    min_pos = np.full(3, np.inf)
    max_pos = np.full(3, -np.inf)

    # Iterate over all frames to find the overall min and max positions
    for ts in u.trajectory:
        positions = u.atoms.positions
        min_pos = np.minimum(min_pos, positions.min(axis=0))
        max_pos = np.maximum(max_pos, positions.max(axis=0))

    # Calculate the dimensions of the box
    box_dimensions = max_pos - min_pos
    transformations = [
        set_dimensions([*box_dimensions, 90, 90, 90]),
        translate(np.array([0.0, 0.0, -min_pos[2]]))  # Shift the system so that the minimum z is at 0
    ]
    u.trajectory.add_transformations(*transformations)


def ignore_no_box(u, ignore_no_box, out_log, global_log):
    if u.dimensions is None:
        if ignore_no_box:
            fu.log('Setting box dimensions using the minimum and maximum positions of the atoms.',
                   out_log, global_log)
            set_box(u)
        else:
            fu.log('The trajectory does not contain box information. '
                   'Please set the ignore_no_box property to True to ignore this error.',
                   out_log, global_log)
            raise ValueError("Box dimensions are required but not found in the trajectory.")
