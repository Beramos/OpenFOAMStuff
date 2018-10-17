# Surface diagnosis

This dictionaries are to be used to visualise the output of the *surfaceCheck* utility in paraVIEW.

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
