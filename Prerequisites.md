# Prerequisites
## Description
What classes can Jordan take?

## Statement
Jordan is trying to figure out his schedule for next semester, and he knows that certain classes are required to be taken
before others, but he can't figure out which classes he's allowed to take. Can you help him figure out which classes he's
allowed to take?

## Input
The first line of input consists of 3 integers: **C**, **P**, and **T**.

The next **C** lines each contain one
class that is being offered.

The next **P** lines each contain one prerequisite composed as <code style="display: inline">&lt;class-1&gt; -&gt; &lt;class-2&gt;</code>,
meaning that class 1 must be taken before class 2.

The next **T** lines each contain one class that Jordan has
already taken. Note that Jordan can only take classes that he has not already taken and for which he has already
completed all prerequisites.

## Output
Output consists of the classes that Jordan is allowed to take in alphabetical order, each on a line by itself.

## Constraints
1 &le; **C**, **P**, **T** &le; 100

The input is guaranteed to be logically consistent. Jordan has already completed the prerequisites for other classes
he has taken, and the prerequisites will form a directed acyclic graph (there will be no loops of "Class A prerequires 
class B and class B prerequires class A").