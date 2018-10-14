---
 title: "Coin Tosses, Markov Chains and an Existential Crisis"
 date: 2018-06-25T00:00:00+02:00
 image: münze.jpg
 summary: "Visualising Markov Chains Based On A Simple Statistical Experiment"
 author: "Johannes"
---


While procrastinating from writing my thesis, I came across an
interesting property of coin tosses (I realise how pathetic that sounds
while writing it). But bare with me, in the end it is about more than a
simple coin toss experiment but also about why this experiment
exemplifies a major flaw in the thinking of today's researchers. On top,
it is a little coding exercise on how to visualise simple markov chains
in R.

### Coin Tosses

**The story goes as follows: Bob and Alice are playing a game. Both have
a fair coin and flip it over and over again. Bob will end the game when
he gets two heads in a row. Alice will end the game when she gets heads
directly followed by tails. On average Bob needs six coin tosses to end
the game and Alice needs four coin tosses.**

Sounds counter-intuitive, right? If a coin is fair, a sequence should be
equally likely to end with **Head, Head**, or **Head, Tail**. So I used
the time in which I should actually write my thesis to find out what
this is about. Before I explain the experiment using markov chains,
let’s quickly simulate the experiment in R:

     
         
        # Write a function to simulate one coin toss 

        coin_toss  Bob: condition = c(1,1); Alice: condition = c(1,0) 
        
        simulate_game  

        

     
        # Mean and Distribution for Heads, Heads (Bob) to end the game 
        [1] 6.007 
        

\
\
![](hist_bob.JPG){.img-responsive
.no-border}\
\
     
        # Mean and Distribution for Heads, Tails (Alice) to end the game  
    [1] 3.961 
        
        

\
\
![](hist_alice.JPG){.img-responsive
.no-border}\
\
The intuitive explanation is as follows: Both Alice and Bob first need
to get *heads*. For Alice, if she gets *tails* for the next toss the
game is over. If she doesn't get *tails* but *heads* shows up again it
is not too bad either because with the next toss she has again the
chance to get *tails* and end the game. This is where the difference
between Alice's and Bob's winning conditions are: If Bob fails to get
*heads* after tossing *heads* the first time, his streak gets reset and
he needs at least two more tosses to win.

### Markov Chains

I found it helpful to visualise the problem with Markov Chains (after
getting the inspiration from Nassim Talbes' Twitter post: @nntaleb).
Markov chains are stochastic models which are useful when describing a
sequence of events. A transition plot helps to visualise how the
different states are connected stochastically.

For Bob there are the following three possible states: **H (Heads), T
(Tails), HH (Heads, Heads)** . For Alice there are the following three
possible states: **H (Heads), T (Tails), HT (Heads, Tails)**

     
         
        
        states_bob  
        

Then we first have to build the transition matrices for both Bob and
Alice. After that we create markov chain objects so that we can plot
them.

     
         
        
        library(markovchain) 
        
        #Transition matrix for Bob 
        tm_bob  
        

The expectation for Alice's markov chain (MC) to converge to the state
of "HT" are 4 iterations, and the expectation for Bob's MC to converge
to the state of "HH" are six iterations. You immediately see, why: Bob
has an additional arrow (from "H" to "T").

\
\
![](tp_bob.JPG){.img-responsive
.no-border}\
\
![](tp_alice.JPG){.img-responsive
.no-border}\
\
### Existential Crisis

I came across this problem first in a Tweet by David Robinson (@drob)
and two hours later I saw Nassim Nicholas Taleb tweeting about it (I
mean, at this point I just had to write a blog post about it).

The reason why people (especially people familiar with probability
theory) first think that it is counterintuitive is "because effects like
linearity of expected value spoil us in being able to treat events as
independent even if they aren't" (David Robinson). Nassim Taleb goes
even further and argues "It is ONLY counterintuitive then you are
trained/selected to think in Static terms".

In his new book "Skin in the Game - Hidden Asymmetries in Daily Life"
Taleb explains why the thinking in **static terms** is one of the core
problems of social scientists and economists today. He argues that most
social scientists are not able to think in dynamics; we are not able of
"thinking in second steps and unaware of the need for them \[...\] while
every car operator in real life knows that real life happens to have
second, third and n-th steps" (p. 9). In the book he explains why
"static thinking" is a major flaw in the work of accomplished
researchers like Thaler (Behavioural Economics), Piketty (Inequality),
and Krugman (Trade). Static thinking is an attribute of what he calls
the "Intellectuals Yet Idiots (IYI)".

Wow, a simple coin toss experiment turned into an existential academic
crisis really fast...

------------------------------------------------------------------------


