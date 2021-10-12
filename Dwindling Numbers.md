# Dwindling Numbers
## Description
Will Tom or Jerry win the game?

## Statement
Tom and Jerry love playing board games, card games, and all sorts of other games. They also like to invent new games. Tom came up with an idea for a game and proposed it to Jerry. Tom will have a list of numbers in no specific order. Tom and Jerry will take turns. On each turn, the player removes a single number from the list. However, they cannot remove whatever number they choose - they must remove the largest number remaining in the list. The first player who has no numbers left to remove loses the game.

Jerry always plays first. Can you determine who will win the game, given the list of numbers?

## Input
The first line contains one integer **N**: the number of integers in the list for the game.

The next line contains **N** integers describing the game's list.

## Output
Output "Tom" if Tom wins the game, otherwise output "Jerry".

## Constraints
* 1 &le; **N** &le; 10<sup>5</sup>
* -10<sup>4</sup> &le; **N<sub>i</sub>** &le; 10<sup>4</sup>