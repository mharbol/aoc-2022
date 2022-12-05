# Day 4
## Thoughts
Whew, this was a good one. I know using sets and intersections would be super easy for
this one but wanted to go a little more efficient and use some maff.
Interestingly enough, I learned about python set intersections; I could have just used
something like `set_1 & set_2` to get the intersection.
Will keep that in mind for later.
## Attacking the problem
As I stated, wanted to make this a bit more math-y and use what I knew about the ranges rather than
default to using sets again. Not sure what the "new thing" is for today... but it's Sunday so
I'll let it slide for now.

I arrange the section assignments so that the "leftmost" range is the one I see first.
"Leftmost" will be the one that starts furthest to the left (lowest start value).
In the case both ranges start with the same value, the leftmost tiebreaker will be the range that extends farthest
to the right. We will refer to the four points that make up our ranges `l0` and `r0` for the leftmost range and
`l1` and `r1` for the rightmost range.
This means automatically that `l0 <= l1`.
Visualizing these ranges there are 3 general forms they can take relative
to each other:
### Leftmost Envelops Rightmost
This can be represented as below or where the left values align. What makes this an envolpment under the rules
is that `r0 >= r1`.
```
l0---------r0 
  l1-----r1
```
### Overlap
Visualized below. Under these conditions, overlap occurs when `r0 >= l1` and `r0 <= r1`. An overlap is a superset
of an envelopment.
```
l0------r0
   l1------r1
```
### No Intersection
Visualized below. The two ranges are distict ranges. This happens when `r0 < l1`.
```
l0--r0
       l1--r1
```