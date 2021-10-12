# Water Glasses
## Description
Can you make a song from water glasses?

## Statement
Saoirse is a water-glass musician. She puts glasses of water in a circle and walks around it counter-clockwise, playing
the glasses in order, one at a time. Each glass emits a different pitch based on how much water is in it.

But sometimes Saoirse wants to play a song that has more notes than there are glasses in the circle. For this to work,
she must redistribute the water as she goes. Immediately after she plays a glass, she can pour it completely into one of
the other glasses. So if she just played Glass #3, with 3 liters, and she pours it into Glass #7 with 5 liters, now
Glass #3 is empty and Glass #7 has 8 liters. This means that she can use Glass #7 for a different pitch when she reaches
it again!

Saoirse wants to know, given the contents of the glasses she has set up, can she play a given song? Note that **she can
begin playing at any point in the circle of glasses**, and will continue in a counter-clockwise direction (without
skipping any glasses) until she finishes. For instance, if the circle has 10 glasses and the song has 45 notes, then
four-and-a-half times around the circle would be needed to complete the song.

Here is a simulation of a more complex song and water circle:

<iframe src="https://jacobbrazeal.com/misc/water-glass-sim" style="width:100%; height: 650px;"></iframe>

## Input
The first line contains two integers, **G**, the number of glasses, and **N**, the number of notes in the song.

The second line contains **G** integers, **A**[1] through **A**[**G**], describing the initial water glass circle in a
counter-clockwise order. Each integer gives the number of liters of water in the glass. Note that glass **G** is
adjacent to glass 1 in the circle.

The third line contains **N** integers, **B**[1] through **B**[**N**], describing the song she wants to play. Each
integer gives the number of liters of water needed for each note in the song.

## Output
Print the string <code style="display: inline;">Yes</code> if Saoirse can play the song. Otherwise print <code style="display: inline;">No</code>.

## Constraints
* 0 &le; **A**[i], **B**[j] &le; 12 for 1 &le; i &le; **G** and 1 &le; j &le; **N**.
* 1 &le; **G** &le; 10
* 1 &le; **N** &le; 50
* You can assume that all the glasses have unlimited volume.