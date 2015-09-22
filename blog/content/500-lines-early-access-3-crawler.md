Title: Early Access Release of "A Web Crawler With asyncio Coroutines"
Date: 2015-09-15 11:00
Author: Michael DiBernardo
Category: 500lines

Today we've [published the third
chapter](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)
in our [early access
release](http://aosabook.org/blog/2015/09/500-lines-or-less-early-access-web-release/)
for 500 Lines. The chapter was written by [A. Jesse Jiryu Davis](https://twitter.com/jessejiryudavis) and [Guido
van Rossum](https://twitter.com/gvanrossum).

We hope that this chapter provides Python programmers with a deep introduction
to how coroutines work, and why and when we should use them. Coroutines first
became a hot topic in Python with the release of the asyncio framework; now, in
Python 3.5, they are also built directly into the language itself. 

Beyond Python, there has been a longstanding tension between
[thread-based](https://web.stanford.edu/~ouster/cgi-bin/papers/threads.pdf) and
[event-based](http://www.cs.berkeley.edu/~brewer/papers/threads-hotos-2003.pdf)
systems in computer science. It can be helpful to a practising programmer to
understand the nuances in this debate, as anyone building things atop
frameworks that use these constructs will eventually have to understand them.

We will have chapters on building thread-based and event-based systems in "500
Lines or Less", and we think that this chapter will serve as an interesting
contrast to both of these contributions in the final draft of the book.

If you find errors you think are worth reporting, please open an issue on our
[GitHub tracker](https://github.com/aosabook/500lines/issues). 

Enjoy!
