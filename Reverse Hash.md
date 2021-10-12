# Reverse Hash
## Description
It should be impossible to reverse a hash... but maybe it's possible...

## Statement
Victor has covered his basement floor with an enormous square array of gears. Each gear in the grid can be rotated into
any of 12 positions. If Victor rotates a gear in position (_r_, _c_) by _k_ turns, then all of the gears in the same
row (row _r_) or the same column (column _c_) will also rotate forward by _k_ positions. For example, if a gear in
position 6 is rotated 8 turns, it's now in position 2 (since 6 + 8 % 12 = 2). Note that gear positions are 1-indexed, so
turning a gear at position 6 forward by 6 turns results in position 12, and the next position after 12 is position 1.

Victor doesn't want anyone to know the original position of the gears, so he rotates several of the gears to encrypt the
position. Given the final positions of the gears and the sequence of rotations that Victor made, can you recover the
original position of the grid?

## Input
The first line contains two integers: **N**, the number of rows/columns of the square array of gears, and **T**, the
number of turns Victor performed.

The next **N** lines contain **N** integers apiece corresponding to the positions of the gears after all of Victor's
changes, where the integer on line **r** and position **c** gives the position of the gear on the **r<sup>th</sup>** row and **c<sup>th</sup>** column.

The next **T** lines each contain 3 integers: **R**, **C**, and **K**, indicating that the gear in position (**R**,
**C**)
was turned forward by **K** turns (along with all the other gears in row **R** and column **C**). Note that **R**
and **C** are 1-indexed. This sequence is given in chronological order, so Victor's first move is given in the first
line, etc.

## Output
Output **N** lines of **N** space separated integers, where the integer in line **R** and column **C**
gives original position of that gear.

## Constraints
* Each gear's position _p_ is an integer 1 &le; _p_ &le; 12.
* 1 &le; **N** &le; 100
* 0 &le; **T** &le; 100
* 1 &le; **R**, **C** &le; **N**
* 0 &le; **K** &le; 12 (a rotation of 0 or 12 has no effect, however)