---
 title: "+1, beers and tada "
 date: 2017-09-09T00:00:00+02:00
 image: "emoji.jpg"
 summary: "Emojis on the CorrelAid Slack"
 author: "Frie"
 draft: true
---


Note: This post is in English because it is based on the Readme of the
corresponding [GitHub
repository](https://github.com/friep/correlaid-slack-analysis)
containing the code etc. And as the *lingua franca* of GitHub is
English, here we are. I hope you don’t mind.

<div id="intro---what-is-slack" class="section level2">

### Intro - what is Slack?

[Slack](https://slack.com/) is a communication tool that the *Core Team*
of CorrelAid uses to communicate with each other to organize our
data-for-good projects - and a lot more. You can imagine the CorrelAid
Slack as a set of so-called channels that organize the conversation by
topic (e.g. channel \#projects). Basically it’s a bunch of WhatsApp or
Facebook group chats with some more features.

By the way, currently, around 60 people are in our Slack, so it is by no
means an exlusive club. If you want to join as well and help organize
CorrelAid, drop an Email to [Regina](mailto:regina.s@correlaid.org).

Anyways, the *by far* most important feature in Slack is that you can
react to the messages others have sent using emojis - similar to
Facebook but with the exception that you can use **all** emojis. Isn’t
that great? Yes! And so we use this feature extensively, mainly because
it’s a quick and easy way to express your opinion. Even if your opinion
might be <f0><U+009F><U+008D><U+00BB>.

So why did I even care to analyze those data? Well… first of all, I’m a
curious person. I always wondered which emoji would top the rankings and
I just wanted to know. Second of all, I like to work with data and if
it’s fun data, even more so! And finally, what’s the most natural thing
to do if you’re a data scientist writing your Master’s thesis? Yeah.
Sure. Let’s procrastinate a bit and pull this data.

If you want to know how I got the data and what the underlying mechanics
are, you can find a bit more on that after the results section. Because,
come on, seeing some emojis is why you clicked in the first place.



<div id="the-results-or-and" class="section level2">

### The results or: <f0><U+009F><U+0091><U+008D>, <f0><U+009F><U+008D><U+00BB>, and <f0><U+009F><U+008E><U+0089>

Using the Slack API, I was able to pull out \~5,800 messages in public
channels out of approximately 20,000 we have sent in total according to
the Slack Analytics tool. I did not have the time to check where the
~~y~~huge difference comes from - I doubt that 3/4 of our messages are
sent in private conversations and private channels which are not covered
by those data - so if anyone can enlighten me, please drop me a message.

Anyway, here's the list of emojis that is used on the CorrelAid Slack –
in decreasing order of appearance. I put the ones occurring less than
ten times in a separate table to save you from scrolling forever -
you’re welcome!

  emoji   emoji\_name     count
  ------- --------------- -------
  <f0><U+009F><U+0091><U+008D>       +1              691
  <f0><U+009F><U+008E><U+0089>       tada            303
  <f0><U+009F><U+0091><U+008C>       ok\_hand        170
  <U+2764>       heart           86
  <f0><U+009F><U+0098><U+008D>       heart\_eyes     39
  <f0><U+009F><U+0098><U+0082>       joy             39
  <f0><U+009F><U+0092><U+00AA>       muscle          39
  <f0><U+009F><U+0098><U+0080>       grinning        19
  <f0><U+009F><U+0098><U+0081>       grin            17
  <f0><U+009F><U+0098><U+0084>       smile           15
  <f0><U+009F><U+0091><U+008F>       clap            13
  <U+261D>       point\_up       12
  <f0><U+009F><U+0099><U+0088>       see\_no\_evil   12
  <f0><U+009F><U+0098><U+008C>       relieved        11
  <f0><U+009F><U+0098><U+00A2>       cry             10
  <f0><U+009F><U+00A4><U+0096>       robot\_face     10
  ???     thomas\_mann    10

------------------------------------------------------------------------

  count   emojis
  ------- ---------------------------------------------------
  8       <f0><U+009F><U+00A4><U+0094> ???
  7       <f0><U+009F><U+0099><U+0082> ??? <f0><U+009F><U+009A><U+0085>
  6       <f0><U+009F><U+00A4><U+0093>
  5       <f0><U+009F><U+0092><U+009A> <f0><U+009F><U+0098><U+008E>
  4       <f0><U+009F><U+0092><U+00AF> <f0><U+009F><U+0091><U+00AB> <f0><U+009F><U+008D><U+00AF> <f0><U+009F><U+0099><U+0089> <f0><U+009F><U+0090><U+00B4> <f0><U+009F><U+0092><U+0081> <f0><U+009F><U+0098><U+0084> <f0><U+009F><U+0098><U+00AD> <f0><U+009F><U+0098><U+009B> <f0><U+009F><U+008F><U+0086><f0><U+009F><U+0098><U+008B>
  3       <f0><U+009F><U+009B><U+00AB> <f0><U+009F><U+008D><U+00BB> <f0><U+009F><U+0098><U+0087> <f0><U+009F><U+0092><U+00B8> <f0><U+009F><U+0098><U+00B1> ??? <f0><U+009F><U+0099><U+0082> <f0><U+009F><U+008D><U+009D> <f0><U+009F><U+0099><U+008A> <f0><U+009F><U+0098><U+0085> <U+2639>
  2       ??? <f0><U+009F><U+0098><U+008A><f0><U+009F><U+0098><U+00B5><f0><U+009F><U+0091><U+00BB><f0><U+009F><U+0098><U+00AC><f0><U+009F><U+0098><U+00BB><f0><U+009F><U+00A4><U+0097><f0><U+009F><U+0098><U+0098><f0><U+009F><U+0094><U+008F><f0><U+009F><U+008E><U+0093><f0><U+009F><U+008E><U+00A5><f0><U+009F><U+0098><U+0084><f0><U+009F><U+0099><U+0086><f0><U+009F><U+0099><U+008C> ??? <f0><U+009F><U+0098><U+0083><f0><U+009F><U+0098><U+008F><f0><U+009F><U+0096><U+0096><f0><U+009F><U+00A6><U+0084><f0><U+009F><U+0099><U+0083><U+270C>
  1       <f0><U+009F><U+0091><U+008E><f0><U+009F><U+0091><U+00B6>???<f0><U+009F><U+008D><U+00BA><f0><U+009F><U+0090><U+00B1><f0><U+009F><U+0098><U+00B0><f0><U+009F><U+0091><U+0091><U+2709><f0><U+009F><U+0098><U+0091><f0><U+009F><U+0091><U+008A><f0><U+009F><U+00A4><U+009E><f0><U+009F><U+0087><U+00BA><f0><U+009F><U+0098><U+00B3><U+270B><U+2049><f0><U+009F><U+0098><U+0086><f0><U+009F><U+008D><U+008B><f0><U+009F><U+0093><U+00AC><f0><U+009F><U+008C><U+0091><f0><U+009F><U+0098><U+00AE>???<f0><U+009F><U+0091><U+0089>???<U+2744><U+2753><f0><U+009F><U+008D><U+0089>???<f0><U+009F><U+0098><U+0092><f0><U+009F><U+0098><U+009C>???<f0><U+009F><U+0091><U+008B><U+2705>???<f0><U+009F><U+0098><U+0089>???

So what can we see? Something that pretty much summarizes my experience
being a Core Team member at CorrelAid: Lots of positivity, party vibes
and love: <f0><U+009F><U+0091><U+008D>, <f0><U+009F><U+008E><U+0089>, <U+2764> and <f0><U+009F><U+0091><U+008C>. I knew this before but look at the numbers.
Those positive emojis outnumber everything else by faaaaar. You just
have to love those people!

Speaking about the numbers: The following barplot shows the `count` for
each emoji sorted by the count. So basically the first bar is <f0><U+009F><U+0091><U+008D>, the
second <f0><U+009F><U+008E><U+0089> and so on. What we see is that the distribution of counts is
heavily skewed to the right.

![](barplot_emoji.png){.img-responsive}*Barplot
of emoji counts*\
\
Some other observations can be made:

1.  In Slack, you can add custom emojis, e.g. upload a small png of your
    favorite football club’s logo and assign an emoji “command” to it.
    We’re obviously huge fans of those custom emojis and have added
    quite a few. But of course, these custom emojis are not supported by
    the R package I used to visualize the emojis (`emo`) and hence
    result in a number of ugly “???”. Hence, if we want to learn more
    about them, we have to look at their names. Because most of them are
    only displayed in the smaller-emoji-table, here are all the *names*
    of the `???` emojis: thomas\_mann, weltherrschaft, effzeh,
    simple\_smile, b04, spock-hand, bvb, demokratie, fingers\_crossed,
    flag-us, leonardo, sge, woman-heart-woman.

Looking at the names, we can see the following themes emerge:

-   football/soccer: emojis bvb, b04, effzeh, sge. Basically our
    \#random channel.
-   culture: emojis thomas\_mann, leonardo. Even data scientists need
    some culture.
-   goal-orientation: emoji weltherrschaft (German for “world
    domination”). Speaks for itself.

2.  For being a Germany-based team, <f0><U+009F><U+008D><U+00BB> performance is disappointing. At
    least, there is no <f0><U+009F><U+008D><U+00B7> emoji at all.

3.  As data scientists, the nerd is strong with some of us. <f0><U+009F><U+00A4><U+0093> and <f0><U+009F><U+00A4><U+0096> are
    doing ok in the rankings (counts 10 respectively 6) but both are
    beaten by the strongest animal on earth - at least emoji-wise: the <f0><U+009F><U+0099><U+0088>
    (12).

That’s it for now. Some more fun analyses and visualizations would be:

-   who gets the most (positive/negative/overall) reactions?
-   bipartite network of users and emojis.
-   …

If you’d have fun “working” on these really important questions, stay
tuned for updates on our meetup that’ll take place from the 17th to 19th
of November in Hamburg. Maybe you’ll get a chance to hack those data??
Who knows… <f0><U+009F><U+0098><U+0089>

Please don’t forget to read the following section on how I got and
processed the data if you want to learn more about that. I promise it’s
beginner-friendly!



<div
id="how-did-i-do-that---a-friendly-introduction-to-apis-http-requests-and-json"
class="section level2">

### How did I do that? - a friendly introduction to APIs, HTTP requests and JSON

Nice! Glad that you made it down here. I’ll try to give you an overview
of how I obtained the data and highlight some problems that I
encountered. Rest assured, it was not a whole lot of code, only
approximately 110 lines of code, rather 80 if you distract library
statements and empty lines.

Anyways, the process looked roughly like that:

1.  Set up an App in Slack to get access to the Slack API.\
2.  Query the API from within R.
3.  Postprocess and clean the data.

<div id="set-up-an-app-in-slack-to-get-access-to-the-slack-api."
class="section level4">

#### 1. Set up an App in Slack to get access to the [Slack API](https://api.slack.com/).

API is short for *Application Programming Interface*. According to our
friend
[Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface),
an API is “a set of clearly defined methods of **communication** between
various software components.” I highlighted the part that is important
for our specific case: communication. In fact, what we want to
communicate to Slack is a request of the form **“hey, please give me all
the messages from our Slack channels, so that I can analyze them”**. The
Slack API is kind of a manual on how exactly we have to send this
message. Maybe a bit like when you have very strict instructions on how
to “communicate” your Master thesis: page margin 2pt, font size 12,
spacing 1.5 and so on.

Coming back to APIs, you might want to think about your Apps on your
phone. It is most likely that some of them actually *communicate* with
each other. For example, Twitter has several APIs that make it possible
to access its functionalities from outside, e.g. when you share
something **to** Twitter. I am no expert but I guess that a lot of
communication between your apps actually relies on APIs?

Although we don’t want to do fancy stuff like this, we actually have to
create our own little personal App within our CorrelAid Slack (see the
[GitHub repository](https://github.com/friep/correlaid-slack-analysis)
for details). We then get a kind of password which we can use to access
our data through R.



<div id="query-the-api-from-within-r." class="section level4">

#### 2. Query the API from within R.

This is quite straight-forward once we know how we have to make our
request, i.e. which of the API method(s) corresponds to our bold request
(pun intended!). Unfortunately, there is no method that directly gives
us all messages from all channels. Instead, we first have to retrieve
list of all channels using `channels:list` and then `channels:history`
to access the history of messages for each of them seperately.

So far so good. Sadly, we cannot type in `channels:list` in R and expect
it to work. With the thousands of APIs out there, there is no way R can
support all of them. Instead, we will use something called HTTP requests
to communicate our request to the Slack API. HTTP requests are the
cornerstone of the web in that they are used to communicate between
computers and servers (and more. again, I’m no expert). For instance,
when you clicked on the link to this post, you sent a GET request to the
server where our homepage is stored on and asked for the content of this
article. The server then sent you back the requested content. Something
similar happens everytime you click around on the Internet.

In R you can send those requests using a package called `httr`. So we
send our request - “formatted” according to the requirements outlined in
the Slack API - and get back our requested content: the data.



<div id="postprocess-and-clean-the-data." class="section level4">

#### 3. Postprocess and clean the data.

“Yeah!!”, you might think. But no. Data from APIs are usually sent to
you not in the form of nice little tables but instead as JSON. JSON is a
document format that is very common for so-called unstructured data.
Unstructured data is everything that you can’t neatly put in a table
which applies to a lot of social media data. Extracting those kind of
data can be really painful and indeed this was the most difficult step.

Breaking that down for the beginner reader would take some more words
and I feel this post has gotten too long already. So I’ll just leave the
package names here - just in case you have to work with complicated JSON
data or lists, the R equivalent of JSON: I used `jsonlite`, `tidyr` but
most importantly `purrr` which I admit is a bit hard to wrap your head
around so I struggled a lot with it. But in the end I came to the data
frame that basically looked exactly like the data in the first table. I
loaded the data in an R Markdown and used the before-mentioned \`emo\`
package to convert the names to the actual visual representations. This
is possible because R Markdown is a special type of R document that lets
you write normal text (like all the blabla here) but also allows to
insert R code, for example to generate the tables above or to make the
emoji\_name -&gt; emoji converion. Pretty cool, huh?

<f0><U+009F><U+008E><U+0089>.

Ps: Please excuse the abrupt ending of this post - I ran out of space
but more importantly time. If you want to know more about it, please
look at the [GitHub
repository](https://github.com/friep/correlaid-slack-analysis) or send
me a message (details down below). I’m all about sharing knowledge!





------------------------------------------------------------------------


