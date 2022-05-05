Title: Chaos of abstraction
Date: 2022-05-03 10:20
Modified: 2012-05-03 19:30
Summary: Chaos of abstraction in software
Status: draft

After a long time, I finally decided write something here. If you found this
blog probably you are a developer or you are someone who loves programming.
Most of the content will be about software, so if you don't like it, feel free
to leave.

If you are still here let's go to the point of this post.

I've been working as a developer for awhile and I noticed a common pattern that
started to annoying me. Software it's getting unreliable and developers know
less about computer. 

I think due to the leak of professionals in software industry and the high
amount of job offers, companies started to invest in tools that abstract the
machines in an attempt of "protect" the programmers of making mistakes, so that
the "developers" become more "productive".

Don't get me wrong, I'm not against abstractions, they are really good, but
maybe we went too far and the cost now is very high. Fragile software and
developers that doesn't know what they are doing. Have you ever meet developers
like listed below?

- Ruby On Rails developers that doesn't know Ruby
- ReactJS programmers who doesn't know JavaScript
- Docker images managed by people that never had run Linux
- Infrastructure professionals that doesn't know how to configure a single server

It is very common now a days, and the result of these practice is faulty
programs. Try to count the amount of bugs you faced during 1 days and you
will be surprised.

During a conference I saw a person suffering with a text editor running in a
browser engine with auto completion done by a **TCP SERVER**[^1] (You know
which text editors I'm talking about). In an attempt of show off a tool, this
person couldn't do it because the autocomplete feature was not working (looks
like no one reads docs anymore).

Maybe no one cares since everyone have good salaries, until some real problem
appears.

So, if you are someone who suffers of imposter syndrome and feels like know
nothing about software, my advice is LEARN YOUR TOOL. Be pragmatic about it.
If you are using *git* to versioning your source code, you need understand
the git internals, if you are a web developer, you need to understand how
sockets, tcp, http works. If someday someting goes wrong with you brand new
framework, you will understand the problems and limitations because you know
how computer works.

If you want to understand better what I tried to say in this post, I would
recommend you to watch this awesome talk[^2] (unfortunately only found on
Youtube) by Jonathan Blow, which explains very well this problem.

---

Have comments? Send me an email on my [public-inbox](mailto:~johnnyrichard/public-inbox@lists.sr.ht)
to start a discussion. [mailing list etiquette](https://man.sr.ht/lists.sr.ht/etiquette.md).

[^1]: Language server protocol https://microsoft.github.io/language-server-protocol/
[^2]: Jonathan Blow - Preventing the Collapse of Civilization: https://www.youtube.com/watch?v=pW-SOdj4Kkk

