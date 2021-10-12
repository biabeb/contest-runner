# Jigsaw Puzzle
## Description
Can you put together the jigsaw puzzle... with code?

## Statement
Stephen really likes putting together jigsaw puzzles, but he's come across one puzzle that he can't figure out, so he's asked you to help him put it together. He has represented the puzzle as a series of ***pieces***, each with a ***color*** and four ***edges***. The color and each of the edges is represented by a number. The puzzle pieces form a grid; each piece (except for the edge pieces) has one neighbor each to the top, right, bottom, and left. The connection between neighboring pieces is assigned a unique number, and the ***edge*** on both sides of that connection will recieve that number. For example if piece A is above piece B and they have a connection with number 53, the bottom ***edge*** of piece A and the top ***edge*** of piece B will both have id 53. Stephen will also give you the picture from the box that shows what color each piece should be. He also knows that the rotation of each piece is correct. Given the list of pieces and picture on the box, can you help him put together the puzzle?

![Jigsaw Puzzle](https://i.ibb.co/JmxwZjV/Slide1.png)

<style>
img {
  max-width: 50%;
	  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.3);
	}
</style>

## Input
Input starts with a line with 2 integers: **W** and **H**, the width and height of the puzzle.

The next **W** x **H** lines each contain 6 integers: **ID**, **C**, **T**, **R**, **B**, **L**. **C** represents the color of the piece, and **T**, **R**, **B**, and **L** represent the edges of the piece.

The next **H** lines each contain **W** integers, representing the colors of the pieces on the grid.

**NOTE**: the edge numbers are globally unique in the puzzle, but colors can be repeated. Pieces on the edge of the puzzle will have those edges denoted as a zero.

## Output
Output consists of **H** lines each containing **W** integers representing the ids of the puzzle pieces in proper order.

## Constraints
1 &le; **W**, **H** &le; 100  
1 &le; **C**, **T**, **R**, **B**, **L**. **C** &le; 10<sup>9</sup> + 7  