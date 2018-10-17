# Surface diagnosis
## Usage
Just add these Dict-files to the system folder of your case and the sphere.stl to the base of your OpenFOAM case

These dictionaries are to be used to visualise the output of the *surfaceCheck* utility in paraVIEW.

**badFaces**

```bash
	surfaceSubset surfaceSubsetDict your_geometry.stl badFaces.stl
```

**Everything except badFaces**

```bash
	surfaceSubset surfaceSubsetDict_invert your_geometry.stl problem_illegalFaces.stl
```

**problemFaces**

```bash
	surfaceSubset surfaceSubsetDict_probFaces your_geometry.stl problemFaces.stl
```

