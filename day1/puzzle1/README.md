Notes on Day 1

In part 1, as with many advent of codes challenges, I knew a part 2 was coming. I took a gamble that part 2 would involve (at least) a third list, thus the list of lists instead of a simple list1, list2, done.

In part 2, I missed a bug at first where I didn't bump i when iterating the while loop.

Using while loops as a whole was entirely because I suspected a third list was on the way and was trying to be ready to handle N lists. That itself made it `while i < value` instead of `for x in thing`

turns out infinite loops will run for a long time at 12% CPU and not do much, but we nailed it now

- Block for reading arguments stolen shamelessly from Screevo and the Advent of Code 2023