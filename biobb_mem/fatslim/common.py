from MDAnalysis.transformations.boxdimensions import set_dimensions


def calculate_box(u):
    # Calculate the dimensions of the box
    positions = u.atoms.positions
    box_dimensions = positions.max(axis=0) - positions.min(axis=0)
    u.trajectory.add_transformations(set_dimensions([*box_dimensions, 90, 90, 90]))
