# Scrambled Polygons
## Description
Those polygons got all scrambled up!

## Statement
Erica is working on a visual editor for polygons. She is writing a function that takes a polygon (defined as a list of vertices), translates it along the x and/or y axes, and renders the output to the screen. However, somewhere in Erica's code, the output points are being scrambled after they are translated!

You are given the input polygon's vertices as (x, y) points in order. You are also given the output polygon's *scrambled* vertices. Given these sets of data, can you determine what the translation was on the x and y axes?

![Scrambled Polygons](https://i.ibb.co/hBWMmVt/scrambled-polygons.png)

<style>
img {
  max-width: 50%;
	  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.3);
	}
</style>

## Input
The first line contains one integer, **Q**, the number of queries. The next **Q** sets of lines are as follows:

The first line contains one integer, **V**, the number of vertices in the polygon.

The next line contains **V** points describing the input polygon, in the format <code style="display: inline;">(x,y) (x,y) (x,y)...</code>. All coordinates are integers.

The next line contains **V** points describing the scrambled output polygon, in the format <code style="display: inline;">(x,y) (x,y) (x,y)...</code>. All coordinates are integers.

## Output
For each test case, output the translation on the x and y axes as a single point in the form <code style="display: inline;">(x,y)</code>.

## Constraints
* 1 &le; **Q** &le; 100
* 1 &le; **V** &le; 100
* For each polygon, all points are unique. The polygon is not guaranteed to be convex or regular.