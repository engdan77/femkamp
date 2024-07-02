# Five Battle Summarization Tool 🎯

## Background

This year I was to help out with this years "[femkamp](https://visitsweden.com/what-to-do/culture-history-and-art/swedish-traditions/midsummer-tradition/midsummer-sweden-something-another-world/)" but considering going to make up each event as the day carries on and us also making up the score that could be anything from meassure in centimeters, or score on a dart board .. or based on how many balls you hit into the buckets .. you can't just summarize the scores that would be biased to the event with the highest numbers, so would be best count in which order you came within each event I think would be found most fair. E.g. if there's 20 names participating the winning person gets 20 points. But a lot of math, and considering all the [snaps](https://en.wikipedia.org/wiki/Snaps) 🥃 consumed during the day I felt I would quickly need a tool or things will definately go wrong .. 🥴

*The solution ...* 

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
1: Daniel [Score: 5] 🥇
2: Nils [Score: 4] 🥈
```

.. so for each competition I can tell who was the winner and who was the true winner at the end 🏆

## Symbols

Medals are shown for the summary 🥇, 🥈 or 🥉. And if there's a tie between competitor you can pay attention to a 🤝 that means you may need to take this into account.

Requirements

- [Pythonista3](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://apps.apple.com/us/app/pythonista-3/id1085978097&ved=2ahUKEwi6m__Gz4eHAxWWExAIHVj4B8wQFnoECBcQAQ&usg=AOvVaw3bRq2p9kAOLiy2adnnJViz) in IOS (e.g. iPhone or iPad)
- [Numbers](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://apps.apple.com/us/app/numbers/id361304891&ved=2ahUKEwjzp_Xcz4eHAxWgHRAIHdBqDpQQFnoECBIQAQ&usg=AOvVaw2AJR2YTDAgs76wFDXHCm_K)
- The Python script

## Installation

Copy the `femkamp.py`  to your Pythonista3 app, and then follow the "[share sheet](https://omz-software.com/pythonista/docs-3.4/py3/ios/pythonista_shortcuts.html#pythonista-share-extension)" instructions to create a shortcut to this Python script.

## License

Copyright (c) [2024] [Daniel Engvall]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.