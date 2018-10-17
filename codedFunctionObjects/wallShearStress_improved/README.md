# wallShearStress_improved

codedFunctionObject to calculate the magnitude of wall shear which excludes normal stresses

```c++
shearStress
    {
        // Load the library containing the 'coded' functionObject
        // need to read information on codedFunctionObjects in OF4: https://bugs.openfoam.org/view.php?id=2441
        libs ("libutilityFunctionObjects.so");

        type coded;
        writeControl   adjustableRunTime;
        writeInterval  0.1;

        // Name of on-the-fly generated functionObject
        redirectType realWallShearStress;

        codeWrite
        #{
          /*------- User changes ------*/
          const int patchNumber = 3; //patchNumber of patch where shear stress is computed

          /*------- Initialisation of variables -------*/
          const volVectorField& U = mesh().lookupObject<volVectorField>("U");
          const volScalarField& nut = mesh().lookupObject<volScalarField>("nut");
          const fvMesh& mesh = refCast<const fvMesh>(obr_); // there are probably better ways to get to the current time

          surfaceVectorField normals
          (
              IOobject
              (
                  "normals",
                  mesh.time().timeName(),
                  mesh,
                  IOobject::NO_READ,
                  IOobject::AUTO_WRITE
              ),
              mesh,
              dimensionedVector
              (
                  "normals",
                  dimensionSet(0, 0, 0, 0, 0, 0 ,0),
                  vector::zero
              )
          );

          volVectorField tractionVector
          (
              IOobject
              (
                  "tractionVector",
                  mesh.time().timeName(),
                  mesh,
                  IOobject::NO_READ,
                  IOobject::AUTO_WRITE
              ),
              mesh,
              dimensionedVector
              (
                  "tractionVector",
                  sqr(dimLength)/sqr(dimTime),
                  vector::zero
              )
          );

          volScalarField normalStress
          (
              IOobject
              (
                  "normalStress",
                  mesh.time().timeName(),
                  mesh,
                  IOobject::NO_READ,
                  IOobject::AUTO_WRITE
              ),
              mesh,
              dimensionedScalar
              (
                  "normalStress",
                  sqr(dimLength)/sqr(dimTime),
                  0
              )
          );

          volScalarField shearStress
          (
              IOobject
              (
                  "shearStress",
                  mesh.time().timeName(),
                  mesh,
                  IOobject::NO_READ,
                  IOobject::AUTO_WRITE
              ),
              mesh,
              dimensionedScalar
              (
                  "shearStress",
                  sqr(dimLength)/sqr(dimTime),
                  0
              )
          );

          /*------- Computation -------*/
          // Equations from http://www.continuummechanics.org/tractionvector.html

          vectorField& ssp = tractionVector.boundaryFieldRef()[patchNumber]; // stress tensor at boundary
          scalarField& sig = normalStress.boundaryFieldRef()[patchNumber];   // normal stress at boundary
          scalarField& S_n = shearStress.boundaryFieldRef()[patchNumber];    // shear stress at boundary
          const vectorField Sfp = mesh.Sf().boundaryField()[patchNumber];    // normal vector at boundary
          const scalarField magSfp = mesh.magSf().boundaryField()[patchNumber]; // magnitude of normal vector at boundary

          const volTensorField T = nut*fvc::grad(U);                         // compute stress tensor
          const tensorField Reffp = T.boundaryField()[patchNumber];          // stress tensor at boundary
          ssp = (-Sfp/magSfp) & Reffp;      // project stress tensor on wall
          sig = (-Sfp/magSfp) & ssp;        // compute normal stress
          S_n = sqrt(magSqr(ssp)-sqr(sig)); // compute magnitude of shear stress at boundary

          shearStress.write();

          Info<< "Writing wall shear stress\n" <<  endl;
```

The TJunction case is a tutorial that exemplifies the uses of this codedFunctionObject in the *controlDict*
