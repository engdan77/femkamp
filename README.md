# Five Battle Summarization Tool 🎯

Background

This year I was to help out with this years "[femkamp](https://visitsweden.com/what-to-do/culture-history-and-art/swedish-traditions/midsummer-tradition/midsummer-sweden-something-another-world/)" but considering going to make up each event as the day carries on and us also making up the score that could be anything from meassure in centimeters, or score on a dart board .. or based on how many balls you hit into the buckets .. you can't just summarize the scores that would be biased to the event with the highest numbers, so would be best count in which order you came within each event I think would be found most fair. E.g. if there's 20 names participating the winning person gets 20 points. But a lot of math, and considering all the [snaps](https://en.wikipedia.org/wiki/Snaps) 🥃 consumed during the day I felt I would quickly need a tool or things will definately go wrong .. 🥴

The solution ... 

Pythonista on my iPhone to the rescue, and quickly putting together some Python code that would take my sheet from [Numbers](https://apps.apple.com/se/app/numbers/id361304891?l=en-GB) based in input such as:

```
+--------+-------------+------+---------------+
|  name  | throw_rings | dart | frog_spitting |
+--------+-------------+------+---------------+
| Daniel |           3 |   25 |            75 |
| Nils   |           5 |   15 |            68 |
+--------+-------------+------+---------------+
```

.. that would do the math and return something like:

```
==============throw_rings===============
Nils: 2 [Competition score: 5]
Daniel: 1 [Competition score: 3]

==================dart==================
Daniel: 2 [Competition score: 25]
Nils: 1 [Competition score: 15]

=============frog_spitting==============
Daniel: 2 [Competition score: 75]
Nils: 1 [Competition score: 68]

=============Summary score==============
1: Daniel [Score: 5]
2: Nils [Score: 4]
```

.. so for each competition I can tell who was the winner and who was the true winner at the end 🏆

