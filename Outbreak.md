# Outbreak
## Description
Save the world!

## Statement
The world is in the middle of a pandemic of the dreaded *yellow virus*. Some people in certain cities are already infected, and new infections happen randomly in certain cities, incrementing the infection rate of that city. If an infection occurs in a city with an infection rate of 3, an ***outbreak*** will occur. The infection rate of a city cannot exceed 3, but all of the neighboring cities will have their infection rates incremented. Outbreaks can cascade to multiple cities, but they cannot cycle back into an infinite loop.

For example, Greenville and Charlotte are connected, and Charlotte and Raleigh are connected. The infection rates are Greenville: 3, Charlotte: 3, and Raleigh: 1. When Greenville gets infected again, it will outbreak, meaning that its neighbor Charlotte will get an infection. This infection will push Charlotte over the edge to an outbreak, and its neighbors will also get infected. Since Greenville has already had an outbreak this round, it doesn't get infected from Charlotte again (because that would lead to an infinite loop), but Raleigh's infection rate increases to 2.

![Outbreak](https://i.ibb.co/y0rBVyK/outbreak.png)

Given the infection rates of various cities and where outbreaks will happen, can you calculate how many outbreaks will happen?

**NOTE**: The mechanics of this problem come from the board game Pandemic<sup>TM</sup>, which is really fun by the way.

<style>
img {
  max-width: 50%;
	  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.3);
	}
</style>

## Input
The first line of input consists of 3 integers: **C**, **N**, and **I**.

The next **C** lines each contain one city along with an integer indicating its infection rate.

The next **N** lines each contain two *neighboring* cities. Note that the neighbor property is symmetric; A being a neighbor of B implies that B is a neighbor of A.

The next **I** lines each contain a city where an infection will occur. These **I** infections are treated as independent rounds and each city can only outbreak once within a given round.


## Output
Output starts with a line with a single integer: the number of outbreaks that occur.

The following **C** lines consist of the list of cities in alphabetical order followed by the infection rate of that city at the end.

**NOTE**: there is no mechanism for the infection rate of a city to decrease.

## Constraints
1 &le; **C**, **N**, **I** &le; 100