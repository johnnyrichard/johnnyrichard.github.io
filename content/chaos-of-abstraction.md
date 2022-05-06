Title: Chaos of abstraction
Date: 2022-05-03 10:20
Modified: 2012-05-03 19:30
Summary: Chaos of abstraction in software
Status: draft

After a long time, I finally decided write something here. If you found this
blog probably you are a developer or you are someone who loves programming.
Most of the content will be about software, so if you don't like it, feel free
to find something else interesting on internet. :^)

If you are still here let's go to the point of this post.

I've been working as a developer for awhile and I've noticed a common pattern
that started to annoying me. Software it's getting unreliable and developers
know less about computer.

I think due to the leak of professionals in software industry and the high
amount of job offers, companies started to invest in tools that abstract the
machines in an attempt of "protect" the programmers of making mistakes, so that
the "developers" become more "productive".

Don't get me wrong, I'm not against abstractions, they are really good, but
maybe we went too far, and the cost now is very high. Fragile software and
developers that doesn't know what they are doing are consequences.

Have you ever meet developers with the following characteristics?

- Ruby On Rails developers that doesn't know Ruby
- ReactJS programmers who do not know JavaScript
- Docker images managed by professionals that never had run Linux

It is very common now a days, and the result of these practice is faulty
programs. Try to count the amount of bugs you've faced during 1 day. You will
be surprised.

During a conference I saw a person suffering with a text editor running in a
browser engine with autocompletion done by a **TCP server**[^1] (You know which
text editor I'm talking about). In an attempt of showing off a tool, this
person failed because the autocomplete feature was not working (looks like no
one reads docs anymore).

Maybe no one cares since everyone get well paid, until some real problem
appears.

So, if you are someone who suffers of imposter syndrome and feels like know
nothing about software, my advice is LEARN YOUR TOOL. Be pragmatic about it.
If you are using *git* to versioning your source code, you need understand
the git internals, if you are a web developer, you need to understand how
sockets, TCP, HTTP works. If someday something goes wrong with your brand new
framework, you will understand the problems and limitations because you know
how computer works.

If you want to understand better what I've tried to say in this post, I would
recommend you to watch this awesome talk[^2] (unfortunately on YouTube) by
Jonathan Blow, which explains very well this problem.

---

Have comments? Send me an email to my [public-inbox](mailto:~johnnyrichard/public-inbox@lists.sr.ht)
and let's begin a discussion. :^) ([mailing list etiquette](https://man.sr.ht/lists.sr.ht/etiquette.md).)

[^1]: Language server protocol https://microsoft.github.io/language-server-protocol/
[^2]: Jonathan Blow - Preventing the Collapse of Civilization: https://www.youtube.com/watch?v=pW-SOdj4Kkk

