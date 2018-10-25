#!/usr/bin/python
#def compute_cell_size():
import numpy as np
from numpy.linalg import solve
import sys

def compute_cell2cell_exp_ratio(start_end_ratio,num_cells):
    return start_end_ratio**(1./(num_cells-1))

def construct_matrices(num_cells,length,exp_ratio):
    '''
        Constructs A and B matrix to solve the linear system A*dX = B

        The system of equation used (3 cell example):
        | dX1 + dX2 + dX3 = length
       <  dX1/dX2 = expansion ratio
        | dX2/dX3 = expansion ratio 
        
        Parameters:
        -----------
        - num_cells: total number of cells
        - length:    domain length
        - exp_ratio: expansion ratio between consecutive cells

        Output:
        -------
        - A: A-matrix
        - B: B-matrix  
    '''

    
    A = np.zeros((num_cells,num_cells))
    A[0] = 1
    A[1:,0:-1] = np.eye(num_cells-1)
    A = A-np.eye(num_cells)*exp_ratio
    A[0,0] = 1
    B = np.zeros((num_cells,1))
    B[0,0] = length
    return A, B

def compute_cellsizes(A,B):
        '''
        Computes the cell sizes dX1, dX2, dX3 from a linear set of equation in matrix form

        The system of equation used (3 cell example):
        | dX1 + dX2 + dX3 = length
       <  dX1/dX2 = expansion ratio
        | dX2/dX3 = expansion ratio 
        
        Parameters:
        -----------
        - A: A-matrix
        - B: B-matrix

        Output:
        -------
        - dX: cellsize array    
    '''
        
        return solve(A,B)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: no arguments provided. \n")
        print("Example: \n number of cells: 5 \n domain length: 2 \n expansion ratio: 0.9 \n")
        print(">> A,B = construct_matrices(5,2.,0.9)")
        A,B = construct_matrices(5,2.,0.9)
        print("A matrix:")
        print(A)
        print("\nB matrix:")
        print(B)

        dX=compute_cellsizes(A,B)
        print("\n>> dX=compute_cellsizes(A,B)")
        print("dX:")
        print(dX)
        print("If the ratio of first to last cell is given (OpenFOAM), use --compute_exp_ratio=True flag")
    else:
        num_cells = int(sys.argv[1])
        length  = float(sys.argv[2])
        exp_ratio = float(sys.argv[3])

        if any([(argument == '--compute_exp_ratio=True') for argument in sys.argv ]):
            exp_ratio = compute_cell2cell_exp_ratio(exp_ratio,num_cells)

        A,B = construct_matrices(num_cells,length,exp_ratio)
        dX=compute_cellsizes(A,B)

        print("Min cellsize: " + str(min(dX)))
        print("Max cellsize: " + str(max(dX)))
        

        if any([(argument == '--verbose')|(argument == '-v') for argument in sys.argv ]):
            print(dX)
