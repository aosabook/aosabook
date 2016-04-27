Title: Early Access Release of "Event-Driven Web Framework" Chapter
Date: 2016-04-27 11:00
Author: Michael DiBernardo
Category: 500lines

Today we've [published the twenty-first (and second-last!) chapter](http://aosabook.org/en/500L/an-event-driven-web-framework.html) in our [early access
release](http://aosabook.org/blog/2015/09/500-lines-or-less-early-access-web-release/)
for 500 Lines. The chapter was written by [Leo Zovic](http://langnostic.inaimathi.ca/).

Throughout the course of this early access release, we've already seen a couple of different concurrency models -- a [thread-based webserver](http://aosabook.org/en/500L/a-simple-web-server.html), and a [web crawler that uses coroutines](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html). In this chapter, we apply another approach to concurrency by building an _event-driven_ webserver in Common Lisp. We then extend this server into a full-featured web framework by leveraging the power of domain-specific languages.

Next week, we'll be releasing the final chapter in the early-access program. We'll be then doing a test print of the final draft, and the first print version will become available a couple of weeks after that. More on that to follow!

As usual, if you find errors you think are worth reporting, please open an issue on our
[GitHub tracker](https://github.com/aosabook/500lines/issues). 

Enjoy!
