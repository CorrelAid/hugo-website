---
title: Happy Bi/R/thday
date: '2018-07-01T00:00:00+02:00'
image: 509-music-with-r.jpg
summary: Learn How to Make R Play Music
draft: no
categories:
- R
- Crazy R
- DIY
- Programming
author:
  name: Jochen
  image: jochen.jpg
  description: Nach einem Bachelor in Politik- und Verwaltungswissenschaft studiert
    Jochen nun Data Science an der Universität Mannheim. Ausgerüstet mit ThinkPad,
    R und Python arbeitet er im dortigen Local Chapter mit und berät außerdem freiberuflich
    Medienunternehmen zu den Themen Datenjournalismus und digitale Inhalte.
  twitter: https://twitter.com/@Joschkon
  facebook: ''
  github: ''
  email: ''
  website: ''
meta:
  title: CorrelAid - Happy Bi/R/thday
  description: R is, and I cannot state this enough, an incredibly versatile tool.
    Back at the University of Konstanz, where my experience with R took root, one
    of my professors once coined the phrase 'Using R, it is never a question if you
    can do something. The only question is how.'
  image: 509-music-with-r.jpg
  keywords: CorrelAid, Data4Good, R, Crazy R, Happy Birthday, Composing
slug: music-with-r
---

*The programming language R is widely used in the academic world, and,
increasingly, in data journalism, too. People run analyses, plot their
data and calculate predictions of real world phenomena. But R can do
more than that – things that many people don’t even know about: making
presentations, writing books, and so on. We start a new, loose series
about the crazy stuff you can do in R apart from science. Today, Jochen
of the Mannheim local chapter starts with explaining you how to make R
play music.*

R is, and I cannot state this enough, an incredibly versatile tool. Back
at the University of Konstanz, where my experience with R took root, one
of my professors once coined the phrase "Using R, it is never a question
if you can do something. The only question is how."

Now, roughly 3 years later on a rainy afternoon in Mannheim, this pretty
accurate description of R's power came back to my mind: It was the
birthday of a good friend of mine and I had been recking my brain all
day long over the question how to congratulate him in a way more
imaginative than the ususal text messages. With him being a Statistician
and me being a wannabe Data Scientist, I thought: "Why not write an
R-Script that plays Happy Birthday?". Armed with a copy of RStudio and
supported by the tremendous swarm intelligence of the internet, the only
question remaining was: How?

After some research and even more trial-and-error-programming, I did
eventually come up with a solution, using the R-Packages *dplyr*,
*sound* and *htmltab*:

The first thing we are going to need is the music itself. By just
entering the name of your favourite song into a search engine of your
choice, you will get plenty of results for sheet music. So, for a start,
we will just create a vector of characters in R, in which we are going
to insert the notes. In case of happy birthday, our R code would look
like this:

```r
pitch <- c('D4', 'D4', 'E4', 'D4',
           'G4', 'F#4', 'D4', 'D4', 
           'E4', 'D4', 'A4', 'G4', 
           'D4', 'D4', 'D5', 'B4', 
           'G4', 'F#4', 'E4', 'C5', 
           'C5', 'B4', 'G4', 'A4', 'G4')
```

Make sure to use the english notation, this will make things easier
later on.

The next thing we need are the note values. These will be specified as
decimal numeric values, so that whole notes are represented by 1, half
notes by 0.5, quarter notes by 0.25 and so on. It is best to store these
values in a vector of type "numeric". Because the first six notes are
repeated once in Happy Birthday, we can shorten things a bit by using
the *rep()* function.

```r
value <- c(rep(c(0.75, 0.25, 1, 1, 1, 2), 2),
              0.75, 0.25, 1, 1, 1, 1, 1, 0.75, 0.25, 1, 1, 1, 2)
```

If everything went well so far, we should now have two vectors of the
same size in our workspace. As pitch and duration of course belong
together, we are now going to join them in a data frame named bday by
using *cbind*:

```r
bday <- cbind.data.frame(pitch, value)
```


This gives us a data frame containing pitch and values of the notes we
want to play – So far for the easy part. Now, we have to determine the
frequencies of the audio waves associated with our notes. Of course,
there would be a simple way to compute them mathematically, but being a
complete musical illiterate, who happens to have some experience in web
mining, I suggest another approach: Wikipedia provides us with a really
nicely formatted table of tones and their frequencies, so all we have to
do is to import this table in R and sanitize the data a bit. For this
purpose, we will use the *htmltab()* function from the htmltab package,
which comes with some very handy webscraping features. Gsub is used for
exchanging the comma with a point as the decimal separator and
*substr()* will remove unneccessary contents, such as links and
annotations.

```r
wikitab <- htmltab("https://de.wikipedia.org/wiki/Frequenzen_der_gleichstufigen_Stimmung",
                   1, 
                   colNames = c("note","eng","ger","freq"))
wikitab$freq <- as.numeric(gsub(",", ".", wikitab$freq))
wikitab$eng <- substr(wikitab$eng,0,3)
```

After having successfully mined the frequencies from the web, it is time
to combine our new knowledge with the data in our bday-dataframe. We can
do this using lapply, which will apply a function that assigns the
correct frequency to every row of our database.

```r
bday$freq <- lapply(bday$pitch, function(x) wikitab[wikitab$eng==x,4])
```


Now, we're almost done. All we have to do now is to create the actual
audio file: Technically speaking, audio files usually are digital
representations of sound waves, which have been captured by a
microphone. However, since we want to create our music entirely in R, we
cannot rely on any recordings, but have to create an "artificial" sound
wave on our own. This is what the *Sine()* funtion from R's "sound"
package is for. Provided with a frequency, a duration and a sampling
rate, it will conveniently create a sine wave of said frequency. In this
case, the sampling rate defines how many individual data points will be
used to describe our sine wave and is therefore a measure of sound
quality. We will go for a sampling rate of 44100 Hz, which is the
standard of modern-day Audio-CDs and should be more than sufficient for
our purpose. One last thing to define would be the length of our sound
in seconds. This can easily be calculated by dividing the value of the
individual notes by the tempo (we will try 110 BPM). With all that
sorted out, its time to create the wave:

```r
wave <-mapply(Sine, bday$freq, (bday$value/110)*60, rate=44100, channels=1 ) %>%
  do.call("c", .)
wave <- as.Sample(wave)
```

Allthough this piece of code looks a bit odd, we need to do it that way
to get a continuous wave: Mapply splits the bday-dataframe into
individual entries and applies *Sine()* to every one of them. These
intermediate results are then passed to *do.call("c", .)* via a pipe
operator, which will combine them into one large object. *as.Sample()*
then tells R to treat wave as a Sound Sample, so all that's left to do
is to

```r
play(wave)
```

relax and enjoy your first, self-made biRthday song.

*The code in this post was inspired by [a posting on
stackoverflow](https://stackoverflow.com/questions/31782580/how-can-i-play-birthday-music-using-r#%0D%0A).
You can copy the whole piece of code in the following:*

```r
if(!require(sound)){install.packages("sound")}
if(!require(dplyr)){install.packages("dplyr")}
if(!require(htmltab)){install.packages("htmltab")}

pitch <- c('D4', 'D4', 'E4', 'D4', 'G4', 'F#4', 'D4', 'D4', 'E4', 'D4', 'A4', 'G4', 'D4', 'D4', 'D5', 'B4', 'G4', 'F#4', 'E4', 'C5', 'C5', 'B4', 'G4', 'A4', 'G4')
value <- c(rep(c(0.75, 0.25, 1, 1, 1, 2), 2),
              0.75, 0.25, 1, 1, 1, 1, 1, 0.75, 0.25, 1, 1, 1, 2)
bday <- cbind.data.frame(pitch, value)

wikitab <- htmltab("https://de.wikipedia.org/wiki/Frequenzen_der_gleichstufigen_Stimmung",1, colNames = c("note","eng","ger","freq"))
wikitab$freq <- as.numeric(gsub(",", ".", wikitab$freq))
wikitab$eng <- substr(wikitab$eng,0,3)

bday$freq <- lapply(bday$pitch, function(x) wikitab[wikitab$eng==x,4])

wave <-mapply(Sine, bday$freq, (bday$value/110)*60, rate=44100, channels=1 ) %>%
  do.call("c", .)

wave <- as.Sample(wave)

play(wave)
```

*The title picture of this post is licensed under Public Domain Mark 1.0 (no Copyright).*

