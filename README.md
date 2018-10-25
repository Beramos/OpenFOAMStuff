# OpenFOAM_extensions
A personal collection of custom solvers, utitilies and other extensions for OpenFOAM

## Content

### codedFunctionObjects
### wallShearStress_improved
* **Compatible with:** OpenFOAM 4.0.x
* **Backward compatible:** no

OpenFOAMs *wallShearStress* functionObject also includes the normal stress in the computation of wall shear stress. This extension removes the normal stress from the stress tensor.

### meshDiagnostics
* **Compatible with:** OpenFOAM 3.0.x
* **Backward compatible:** untested

Some Dict-files and a reference geometry are provided to be used with the surfaceSubset utility.

### auxiliary scripts
This folders contains various scripts to perform basic post- and preprocessing tasks

**Scripts:**
- *expansion_calculator.py*: computes the cell sizes for a given number of cells, the domain length and an expansion ratio

