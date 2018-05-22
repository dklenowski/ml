Categories: core 
Tags: matrices
      inverse
      inner
      cross

## Convention

    -----> row (i)
    |
    |
    \/ columns (j)

## Zero Matrix

$latex a_{ij}=0 $ for all i and j

## Identity Matrix

- Is the diagonal.
- i.e.

$latex a_{ij}=0\; i\neq j $
$latex a_{ii}=1 $ for all i

e.g.

    $latex \underline{A}=\left[\begin{array}{ccc} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\end{array}\right] $

## Inverse Matrix

- In algebra, the inverse of a number is a number when multiplied to the original gives a product of 1
- i.e. for $latex x $ the inverse is $latex inverse = \frac{1}{x} $ where $latex \left(\frac{1}{x}\right)x=1 $
- In matrix algebra:

$latex \underline{A}\underline{A}^{-1}=\underline{A}^{-1}\underline{A}=\underline{I} $

- Notes:
  - Matrix must be square to have an inverse.
  - Not all square matrices have an inverse (e.g. some dont exist).

e.g.

    $latex \underline{A}=\left[\begin{array}{cccc} a_{11} & .. & .. & a_{1n}\\ .. & & & ..\\ .. & & & ..\\ a_{n1} & .. & .. & a_{nn}\end{array}\right] $

and

    $latex \underline{A}^{-1}=\left[\begin{array}{cccc} a_{11} & .. & .. & a_{1n}\\ .. & & & ..\\ .. & & & ..\\ a_{n1} & .. & .. & a_{nn}\end{array}\right] $

To solve for the first column:

    $latex \overbrace{\left[\begin{array}{cccc} a_{11} & .. & .. & a_{1n}\\ .. & & & ..\\ .. & & & ..\\ a_{n1} & .. & .. & a_{nn}\end{array}\right]}^{knowns}\overbrace{\left[\begin{array}{c} a_{11}\\ ..\\ ..\\ a_{n1}\end{array}\right]}^{Unknowns}=\left[\begin{array}{c} 1\\ 0\\ ..\\ 0\end{array}\right] $

## Matrix Operations

### Addition

$latex \underline{C}=\underline{A}+\underline{B} $ where $latex c_{ij}=a_{ij}+b_{ij} $

### Subtraction

$latex \underline{C}=\underline{A}-\underline{B} $ where $latex c_{ij}=a_{ij}-b_{ij} $

### Multiplication

If $latex \underline{A} $ is an `m*p` (`rows*columns`) matrix and $latex \underline{B} $ is an `p*n` matrix the resultant matrix $latex \underline{A}\underline{B} $ is an `m*n` matrix

i.e.

$latex \underline{C}=\underline{A}\underline{B} $ where
$latex \underline{C}={\displaystyle \sum_{k=1}^{p}a_{ik}b_{kj}} $
$latex i=1\ldots m $
$latex j=1\ldots n $

e.g.

    $latex c_{ij=}\left[\begin{array}{cccc} a_{i1} & a_{i2} & \ldots & a_{ip}\end{array}\right]\left[\begin{array}{c} b_{1j}\\ b_{2j}\\ \ldots\\ b_{pj}\end{array}\right] $

    $latex c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\ldots+a_{ip}b_{pj} $

e.g.

    $latex \underline{A}\underline{B}=\left[\begin{array}{ccc} a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23} \end{array}\right]\left[\begin{array}{cc} b_{11} & b_{12}\\ b_{21} & b_{22}\\ b_{31} & b_{32} \end{array}\right]=\left[\begin{array}{cc} a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31} & ....\\ a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31} & .... \end{array}\right] $


#### Inner and Outer Product

- Related to vectors

##### Inner Product

- aka Scalar Product
- Produces scalar

e.g.

    $latex \underline{a}\centerdot\underline{b}=\underline{a}^{T}\centerdot\underline{b}=\left(\begin{array}{ccc} a_{1} & .... & a_{n}\end{array}\right)\left(\begin{array}{c} b_{1}\\ ....\\ b_{n} \end{array}\right) $
 
    $latex \underline{a}\centerdot\underline{b}={\displaystyle \sum_{i=1}^{n}a_{i}b_{i}} $

##### Outer Product

- aka Vector Product

e.g.

    $latex \underline{a}\times\underline{b}=\underline{a}\times\underline{b}^{T}=\left(\begin{array}{c} a_{1}\\ ..\\ a_{n} \end{array}\right)\left(\begin{array}{ccc} b_{1} & .. & b_{n}\end{array}\right)=\left[\begin{array}{ccc} a_{1}b_{1} & .. & a_{1}b_{n}\\ .. & .. & ..\\ a_{n}b_{1} & .. & a_{n}b_{n} \end{array}\right] $


### Scalar Product

If $latex \underline{A} $ is an `n*n` matrix and k is a real then

$latex \underline{B}=k\underline{A} $

where:

$latex b_{ij}=ka_{ij} $

### Transposition

If $latex \underline{A} $ is an `m*n` matrix, then $latex \underline{A}^{T} $ is called the transposition matrix iff $latex b_{ji}=a_{ij} $ for all i and j.

e.g. The transpose of:

    $latex \underline{A}=\left[\begin{array}{ccc} 2 & 7 & 1\\ 8 & 6 & 4\end{array}\right] $

is

    $latex \underline{A^{'}}=\left[\begin{array}{cc} 2 & 8\\ 7 & 6\\ 1 & 4\end{array}\right] $

## Laws

### Commutative

If $latex \underline{A} $ and $latex \underline{B} $ are both `m*n` matrices, then:
$latex \underline{A}+\underline{B}=\underline{B}+\underline{A} $

### Associative

If $latex \underline{A} $, $latex \underline{B} $ and $latex \underline{C} $ are `m*n` matrices, then:

$latex \underline{A}+(\underline{B}+\underline{C})=(\underline{A}+\underline{B})+\underline{C} $

If $latex \underline{A} $ is `m*n`, $latex \underline{B} $ is `n*p` and $latex \underline{C} $ is `p*r` (where the result, if multiplied together would be a `m*r` matrix), then:

$latex \underline{A}(\underline{B}\underline{C})=(\underline{A}\underline{B})\underline{C} $

### Distributive

If $latex \underline{A} $ and $latex \underline{B} $ are `m*n` and $latex \underline{C} $ and $latex \underline{D} $ are `n*p` (where the result in the following example would be an `m*r` matrix), then:

$latex \underline{A}(\underline{C}+\underline{D})=\underline{A}\underline{C}+\underline{A}\underline{D} $

$latex (\underline{A}+\underline{B})\underline{C}=\underline{A}\underline{C}+\underline{B}\underline{C} $

Note, in general:

$latex \underline{A}\underline{B}\neq\underline{B}\underline{A} $

## Determinant

A scalar, denoted by either $latex det(A) $ or $latex \mid\underline{A}\mid $.

If $latex \underline{A} $ is an `n*n` matrix:

$latex det(A)={\displaystyle \sum_{j=1}^{n}a_{ij}c_{ij}} $

for any $latex i=1,2\ldots n $

$latex c_{ij} $ is called the cofactor

$latex c_{ij}=(-1)^{i+j}m_{ij} $

where $latex m_{ij} $

- Minor entry.
- Determinant of `(n-1)*(n-1)` sub matrix of $latex \underline{A} $ i.e.delete i'th row and j'th column.

e.g. for a 2x2 matrix

    $latex \underline{A}=\left[\begin{array}{cc} a_{11} & a_{12}\\ a_{21} & a_{22}\end{array}\right] $

$latex det(A)=a_{11}a_{22}-a_{12}a_{21} $

e.g. for a 3x3 matrix

    $latex \underline{A}=\left[\begin{array}{ccc} 25 & 5 & 1\\ 64 & 8 & 1\\ 144 & 12 & 1\end{array}\right] $

$latex det(A)={\displaystyle \sum_{j=1}^{3}(-1)^{i+j}a_{ij}m_{ij}\; for\; i=1,2,3} $

Let i=1

    $latex \begin{aligned}det(A) & ={\displaystyle \sum_{j=1}^{3}}(-1)^{1+j}a_{1j}m_{1j}\\ & =(-1)^{1+1}a_{11}m_{11}+(-1)^{1+2}a_{12}m_{12}+(-1)^{1+3}a_{13}m_{13}\\ & =a_{11}m_{11}-a_{12}m_{12}+a_{13}m_{13}\end{aligned} $

    $latex \underline{m}_{11}=\left[\begin{array}{cc} 8 & 1\\ 12 & 1\end{array}\right]=-4 $
    $latex \underline{m}_{12}=\left[\begin{array}{cc} 64 & 1\\ 144 & 1\end{array}\right]=-80 $
    $latex \underline{m}_{13}=\left[\begin{array}{cc} 64 & 8\\ 144 & 12\end{array}\right]=-384 $

    $latex \begin{aligned}det(A) & =a_{11}m_{11}-a_{12}m_{12}+a_{13}m_{13}=25(-4)-5(-80)+1(-384)\\ & =-100+400-384\\ & =-84\end{aligned} $

### Rules

$latex det(AB)=det(A)det(B) $

### Theorems

- If a row or column is all 0, then $latex det(A)=0 $
- If a row is proportional to another, then $latex det(A)=0 $
- If a column is proportional to another, then $latex det(A)=0 $
- If a row or column is multiplied by a constant k (to form $latex \underline{B} $) then $latex det(A)=kdet(B) $

## Eigenvector

Used to solve differential equations.

An eigenvector transforms a maxtrix from its original position, while maintaining the original direction of the matrix.

i.e.

$latex \underline{A}\underline{x}=\lambda\underline{x} $

where:

$latex \lambda $ - scalar, eigenvalue of $latex \underline{A} $ s.t. $latex \underline{x}\neq\underline{0} $

$latex \underline{x} $ - vector, eigenvector of $latex \underline{A} $ s.t. $latex \underline{x}\neq\underline{0} $

### Properties

- Exist for only nxn (square) matrices.
- Given an nxn matrix, there are n eigenvectors (NB there are special cases where no eigenvectors exist.
- All eigenvectors of a nxn matrix are orthogonal to each other (this means you can express $latex \underline{A} $ in termos of this orthogonal eigenvectors (instead of the traditional x,y,z.
- For an nxn triangular matrix $latex \underline{A} $, the eigenvales of $latex \underline{A} $ are diagonal entries of $latex \underline{A} $.
- If $latex \underline{A} $ is singular, $latex \lambda=0 $
- $latex \underline{A} $ and $latex \underline{A}^{T} $ have the same eigenvalues.

### Solving

$latex (\underline{A}\underline{x}-\lambda\underline{x})=\underline{0} $
$latex (\underline{A}-\lambda\underline{I})\underline{x}=\underline{0} $
$latex det(\underline{A}-\lambda\underline{I})\underline{x}=\underline{0} $

e.g. for n=2 (i)

    $latex \left[\begin{array}{cc} (a_{11}-\lambda) & a_{12}\\ a_{21} & (a_{22}-\lambda)\end{array}\right]\left[\begin{array}{c} x_{1}\\ x_{2}\end{array}\right] \left[\begin{array}{c} 0\\ 0\end{array}\right] $

For the above equation to have a solution $latex \underline{x}\neq\underline{0} $ then the coefficient matrix $latex (\underline{A}-\lambda\underline{I}) $ must be singular (i.e. its determinant must equal 0).

    $latex det\left[\begin{array}{cc} (a_{11}-\lambda) & a_{12}\\ a_{21} & (a_{22}-\lambda)\end{array}\right]=(a_{11}-\lambda)(a_{22}-\lambda)-a_{12}a_{22}=0 $

This gives the characteristic equation (ii) with solutions $latex \lambda_{1} $ and $latex \lambda_{2} $

$latex \lambda^{2}-(a_{11}+a_{22})+a_{12}a_{22}-a_{12}a_{21}=0 $

Therefore solve (ii) and insert into (i) to get:

$latex \lambda_{1} $ with eigenvector $latex \underline{x}^{(1)} $.

$latex \lambda_{2} $ with eigenvector $latex \underline{x}^{(2)} $.

Note, if $latex \underline{x} $ is an eigenvector of $latex \underline{A} $, so is $latex k\underline{x} $ for any $latex k\neq0 $.