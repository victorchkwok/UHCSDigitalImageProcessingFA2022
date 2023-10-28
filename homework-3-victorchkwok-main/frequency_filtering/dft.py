import numpy as np
import math 
# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries


class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        tmatrix = np.zeros((matrix.shape[0] ,matrix.shape[1]),dtype=complex)
        for u in range(tmatrix.shape[0]):
            for v in range(tmatrix.shape[1]):
                for i in range(tmatrix.shape[0]):
                    for j in range(tmatrix.shape[1]):
                        tmatrix[u,v] = tmatrix[u,v] + matrix[i,j]*(math.cos((2*math.pi/15)*(u*i+v*j))-(1j)*(math.sin((2*math.pi/15)*(u*i+v*j))))
        return tmatrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""
        tmatrix = np.zeros((matrix.shape[0] ,matrix.shape[1]),dtype=complex)
        for u in range(tmatrix.shape[0]):
            for v in range(tmatrix.shape[1]):
                for i in range(tmatrix.shape[0]):
                    for j in range(tmatrix.shape[1]):
                        tmatrix[u,v] = tmatrix[u,v] + matrix[i,j]*(math.cos((2*math.pi/15)*(u*i+v*j))+(1j)*(math.sin((2*math.pi/15)*(u*i+v*j))))
        return tmatrix

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        tmatrix = np.zeros((matrix.shape[0] ,matrix.shape[1]),dtype=complex)
        for u in range(tmatrix.shape[0]):
            for v in range(tmatrix.shape[1]):
                    tmatrix[u,v] = math.sqrt(math.pow(np.real(matrix[u,v]), 2) + math.pow(np.imag(matrix[u,v]), 2))
        return tmatrix
        