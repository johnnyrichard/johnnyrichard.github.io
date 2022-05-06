Title: The dark side of abstractions
Date: 2022-05-06 23:00
Modified: 2012-05-06 23:20
Summary: The dark side of abstractions

After a long time, I finally decided to write something here. If you found this
blog probably you are a developer or you are someone who loves programming.
Most of the content will be about software, so if you don't like it, feel free
to find something else interesting on the internet. :^)

If you are still here let's go to the point of this post.

I've been working as a developer for awhile and I've noticed a common pattern
that started to annoy me. Software is getting unreliable and developers know
less about computers.

I think due to the lack of professionals in software industry and the high
amount of job offers, companies started to invest in tools that abstract the
machines in an attempt to "protect" the programmers of making mistakes, so that
the developers become more "productive".

Don't get me wrong, I'm not against abstractions, they are really good, but
maybe we went too far, and the cost now is very high. Fragile software and
developers that don't know what they are doing are consequences.

Have you ever meet developers with the following characteristics?

- Ruby On Rails developers that doesn't know Ruby
- ReactJS programmers who do not know JavaScript
- Docker images managed by professionals that never had run Linux

It is very common nowadays, and the result of these practices are faulty
programs. Try to count the amount of bugs you've faced during 1 day. You will
be surprised.

During a conference I saw a person suffering with a text editor running in a
browser engine with autocompletion done by a **TCP server**[^1] (You know which
text editor I'm talking about). In an attempt of showing off a tool, this
person failed because the autocomplete feature was not working (looks like no
one reads docs anymore).

Maybe no one cares since everyone gets well paid, until some real problem
appears.

So, if you are someone who suffers of imposter syndrome and feel like you know
nothing about software, my advice is LEARN YOUR TOOL. Be pragmatic about it. If
you are using *git* to versioning your source code, you need to understand the
git internals, if you are a web developer, you need at least to understand how
sockets, TCP, HTTP works. If something goes wrong with your brand new
framework, you will understand the problems and limitations because you know
how computers works.

If you want to understand better what I've tried to say in this post, I would
recommend you to watch a awesome talk[^2] titled *Preventing the Collapse of
Civilization* (unfortunately on YouTube) by Jonathan Blow, which explains very
well this problem.

---

Have comments? Send an email to my [public-inbox](mailto:~johnnyrichard/public-inbox@lists.sr.ht)
and let's begin a discussion. :^) ([mailing list etiquette](https://man.sr.ht/lists.sr.ht/etiquette.md))

[^1]: Language server protocol https://microsoft.github.io/language-server-protocol/
[^2]: Jonathan Blow - Preventing the Collapse of Civilization: https://www.youtube.com/watch?v=pW-SOdj4Kkk

