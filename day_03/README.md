# Day 3
## Thoughts
Whew! That was a rough one. Had my feet to the fire figuring out sets and intersections.
Glad I got that one behind me. Had a grand plan to do Part 2 with sets as well but when looking
at all the code and just wanting it to be over I called it a day with the nasty nested loops.
Overall, very happy with how it went.
Also, did the most minimal of header files too. yay
## Attacking the problem
Just like the classic interview problems, there's an easy way with a lot of loops and a harder
way that more than likely involves hashsets and maps. Today I attacked `set`.
Got duped for a second when I didn't realize there could be repeat items on one side of the ruck.
That led me to a serious debugging sesh for a while.

Word to the wise: use an ORDERED set for intersects. `unordered_set` gave me segfaults for a good
20 minutes before I realized what was happening.