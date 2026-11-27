# Biobb Membrane changelog

## [Unreleased]

### Changes

* [FIX] `fatslim_apl` and `fatslim_membranes` read the trajectory. Before, they analysed the coordinates of the topology file only and, when it had no box, with a box made from the extent of the atoms (`ignore_no_box`), so the areas per lipid near the box edges were wrong.
* [FIX] `fatslim_apl` analyses the frames from `begin_frame` to `end_frame` (all of them by default; `end_frame` itself is not analysed), not only the first one. The output CSV has the areas of every analysed frame, with a new first column `frame`.
* [CHANGE] `fatslim_membranes` identifies the leaflets of one frame, chosen with the new `frame` property (the first one by default, -1 for the last one). Its `begin_frame` and `end_frame` properties are removed: FATSLiM can not write the leaflets of every frame.
* [CHANGE] `fatslim_apl`: trajectories in the formats FATSLiM can not read (cpt, g96, pdb, tng) and trajectories without box (with `ignore_no_box`) are converted to XTC for FATSLiM.
* [CHANGE] `ignore_no_box` of the FATSLiM blocks sets the box as in the lipyphilic blocks: from the extent of the atoms in all the frames, with the system shifted so that its minimum z is 0.
* [CHANGE] `fatslim_apl` and `fatslim_membranes` remove their temporary files also with `disable_sandbox` (unless `remove_tmp` is False).
* [CHANGE] `gorder_aa`, `gorder_ua` and `gorder_cg`: `output_order_path` is a required argument also in Python, as documented.

## What's new in version [5.3.1](https://github.com/bioexcel/biobb_mem/releases/tag/v5.3.1)?

### Changes

* [FIX] `fatslim_apl` and `fatslim_membranes` no longer fail with `disable_sandbox` when the input files are outside the working directory.

## What's new in version [5.3.0](https://github.com/bioexcel/biobb_mem/releases/tag/v5.3.0)?

### Changes

* [UPDATE] Update to biobb_common 5.3.1

## What's new in version [5.2.2](https://github.com/bioexcel/biobb_mem/releases/tag/v5.2.2)?

### Changes

* [UPDATE] Update to biobb_common 5.2.2

## What's new in version [5.2.1](https://github.com/bioexcel/biobb_mem/releases/tag/v5.2.1)?

### Changes

* [Fix] Fix leaflets numpy type for flip flops.

## What's new in version [5.2.0](https://github.com/bioexcel/biobb_mem/releases/tag/v5.2.0)?

### Changes

* [UPDATE] Update to biobb_common 5.2.0

## What's new in version [5.1.2](https://github.com/bioexcel/biobb_mem/releases/tag/v5.1.2)?
### New features
* [UPDATE] Enable Python 3.12 support.
* [UPDATE] Update lipyphilic dependency.
* [UPDATE] fatslim installation is done via conda.
* [FIX] Remove tmp file from FatslimMembranes.

## What's new in version [5.1.1](https://github.com/bioexcel/biobb_mem/releases/tag/v5.1.1)?
### New features
* [UPDATE]: Update to biobb_common 5.1.1
* [FEATURE] Add gorder deuterium analyses for all atoms, coarse grained and united atom systems.
* [REMOVE] Remove gmx order.
* [REMOVE] Python 3.9 support.

## What's new in version [5.1.0](https://github.com/bioexcel/biobb_mem/releases/tag/v5.1.0)?
### New features
* [FIX](https://github.com/bioexcel/biobb_mem/commit/4b4e03c6268f180060a3e7d82fadd74ce30e9988) Fix entry points
* [UPDATE]: Update to biobb_common 5.1.0

## What's new in version [5.0.6](https://github.com/bioexcel/biobb_mem/releases/tag/v5.0.6)?
### New features

* [FEATURE] Add FATSLiM area per lipid analysis.
* [FEATURE] Add GROMACS acyl chain order analysis.
* [FEATURE] Add Lipyphilic flip-flop analysis.

## What's new in version [5.0.5](https://github.com/bioexcel/biobb_mem/releases/tag/v5.0.5)?
### New features

* [UPDATE] Add return_hydrogen to FATSLiM.

## What's new in version [5.0.4](https://github.com/bioexcel/biobb_mem/releases/tag/v5.0.4)?
### New features

* [UPDATE] New output_csv_path argument for mda_hole.

## What's new in version [5.0.3](https://github.com/bioexcel/biobb_mem/releases/tag/v5.0.3)?
### New features

* [FEATURE] New lpp_zpositions analysis.
* [UPDATE] Adding ignore_no_box property to fatslim_membranes.
* [UPDATE] Adding display_fatslim helper function for fatslim_membranes.
* [UPDATE] Adding display_hole helper function for mda_hole.
* [UPDATE] Adding display_nglview helper function for lpp_assign_leaflets.

## What's new in version [5.0.2](https://github.com/bioexcel/biobb_mem/releases/tag/v5.0.2)?
### New features

* [UPDATE] Adding ignore_no_box property to lpp_assign_leaflets.
* [FEATURE] New fatslim_membranes analysis.

## What's new in version [5.0.1](https://github.com/bioexcel/biobb_mem/releases/tag/v5.0.1)?
New package for membrane structure analysis.

### New features

* New package biobb_mem
* Update to biobb_common 5.0.0
