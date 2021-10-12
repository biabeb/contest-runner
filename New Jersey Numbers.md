# New Jersey Numbers
## Description
Help the ACM set up jerseys for their contest.

## Statement
The ACM has decided to add some flair to their yearly programming competitions. This year, they require all teams to customize their own jersey colors, and each member on the team must choose a jersey number. However, since each programmer is identified by their number, any two teams cannot have the same number.

For example, team A has the jersey numbers 3 6 9, team B has 4 6 8, and team C has 3 5 7. Since teams A and B both have 6, a single member from either A or B must change their jersey. Since teams A and C both have 3, a single member from either A or C must also change. In total, a minimum of 2 members must change their jerseys.

Can you help the ACM determine the minimum amount of members that need to change their jerseys to guarantee that no two teams have the same number?

## Input
The first line contains two integers **T** and **M**: the number of teams, and the number of members on each team.

The next **T** lines contain **M** integers each: the number on that member's jersey.

## Output
Output one integer: the minimum members that need to change their jerseys to guarantee that no two teams have the same number.

## Constraints
* 1 &le; **T, M** &le; 1000