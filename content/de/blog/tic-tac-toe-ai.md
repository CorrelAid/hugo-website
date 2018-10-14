---
 title: "Developing an AI for Tic-Tac-Toe in R "
 date: NA
 image: /images/blog/tictactoe.JPG
 summary: "How Can We Model the Game?"
 author: "Johannes"
---


A couple of weeks ago I watched a documentary
(https://www.alphagomovie.com/) on the team of DeepMind. They developed
an Artificial Intelligence (AI) called AlphaGo which was later capable
of beating the best player in the Game Go - an ancient Chinese board
game considered one of the most difficult games in the world.

As always, the best way to really understand what's going on and how you
can train an AI to play a game is coding it yourself. To start slowly, I
decided to build an AI that can play the game Tic Tac Toe (TTT). Tic Tac
Toe is a simple game where both players have perfect information (like
in Chess or Go), but the number of possible games is limited. While
there are 10\^120 different games in chess and 10\^360 possible games in
Go, there are only 360.000 possible games in Tic Tac Toe.

Tic Tac Toe has, in addition, very simple rules. The goal of an AI model
for the game would be to implement some kind of evaluation function that
can determine whether or not a move is good given the situation on the
board. As the possibilities of different games are so limited it is
actually possible to solve TTT with a brute-force minimax algorithm
(https://www.r-bloggers.com/tic-tac-toe-part-3-the-minimax-algorithm/).
But where is the fun in that? I want the model to figure out good moves
itself. So: what do we need to write an AI that can play the game?

1.  Build the game mechanics
2.  Generate a dataset to train the AI
3.  Build a deep neural network that can evaluate a board position
4.  Implement a function that chooses the best next move

### 1. Build the game mechanics

There are some blog posts where people built the mechanics for TTT in R
(https://www.r-bloggers.com/tic-tac-toe-simulation-random-moves/ or
https://cran.r-project.org/web/packages/tictactoe/README.html). However,
I wanted to figure out the game mechanics myself, so I decided to build
it from scratch. The full version of the code can be found here:
https://github.com/JohMueller/tic\_tac\_toe\_AI.

Basically, the TTT board represents an array with 9 elements
representing the individual cells, which can be either 0 (not played
yet), 1 (player 1), or 2 (player 2).

![](/images/blog/vector.JPG){.img-responsive
.no-border}
From there on we have to write some help functions: 1. determine all
possible moves; 2. make a move; 3. evaluate the board if anyone has won.
Then we can set up the game. In this first instance we will have two
players playing each other with random moves. The function
random\_move() first determines the possible moves and then returns a
random possible move.



    game 

So far so good, we can now let two random players play the game. You can
also actively play the game by adding some print() functions after each
move and the line

`next_move  `
### 2. Build a training data set

To train our AI we have to give it some idea of what a "good move" is.
Ideally, we would have records of games where humans played against one
another. However, as there is no such dataset, we need another solution.
I simulate the game between two random players 5000 times (using a
slightly modified version of the code above) and keep a record of all
the different boards that were played and to which outcome they lead:
(0) TIE, (1) Victory Player 1, (2) Victory Player 2.



    boards_df 

This provides us with a dataset with 37.961 different board settings and
their respective outcomes. Using this dataset we can now train a neural
network to predict which outcome is most likely given a board position.

### 3. Build a Neural Net

Before setting up our model we first have to pre-process the data a
little bit. I mentioned above that a board situation can be represented
as a simple vector. So far, there are 3 possible values for each element
in the board-vector: (0, 1, 2). Using one hot encoding I create 18
features that represent the state for every field for each player. I
also split the dataset in a training and a validation dataset (20
percent). Now, we can start building a simple feedforward neural network
using the Keras API to Tensorflow. Neural networks are perfect for a job
like this as we need a highly flexible non-linear function that maps the
features to the outcome. It roughly looks as follows (Source Pic:
https://www.researchgate.net/figure/The-topology-of-a-typical-multiple-layer-neural-network-consisting-of-one-input-layer\_fig2\_228589481):

![](/images/blog/topology.png){.img-responsive
.no-border}
The neural net has 4 layers: An input layer with 18 input nodes, two
hidden layers with 9 nodes each, and an output layer with 3 nodes which
represent the three outcomes (Tie, Win Player 1, Win Player 2). For the
hidden layers I use the relu activation function and for the outcome
layer softmax activation for multiclass classification.



    #Initialize model
    model %
      layer_dense(units = 9,
                  kernel_initializer = "uniform",
                  activation = 'relu',
                  input_shape = c(18)) %>%
      layer_dense(units = 9,
                  kernel_initializer = "uniform",
                  activation = 'relu') %>%
      layer_dense(units = 3, activation = 'softmax')

    # Compile Model
    model %>% compile(loss = 'categorical_crossentropy',
                      optimizer = optimizer_rmsprop(),
                      metrics = c('accuracy'))

    # Train Model
    history % fit(
      x_train, y_train,
      epochs = 20, batch_size = 100,
      validation_split = 0.2
    )

    model %>% evaluate(x_test, y_test)

The accuracy of predictions is at around 64 % which doesn't sound like a
good value but keep in mind that there are some very early game
positions in the dataset where only one or two moves have been played.

![](/images/blog/training.JPG){.img-responsive
.no-border}
### 4. Implement a function that chooses the best next move

Now that we have a model that can predict what the probability for each
outcome given a certain board position is, we can use the model to make
more informed moves. There is a lot going on here so let me walk you
through the steps:

-   Get all possible moves using possible\_moves()
-   Iterate through all possible moves, feed the resulting boards to the
    model and evaluate the outcome probabilities using
    evaluate\_board\_position()
-   Find the move which has the highest probability of resulting in a
    win
-   Return that move

I decided to code two versions of the AI player: One plays aggressively
meaning that it optimises for the win probability. The other one plays
defensively meaning that it optimises for the probability of "not
losing". The style of the AI is passed to the function as an argument.



    AI_move 1){

        move_probas 

This function can then simply be added to the code above by replacing
the line for *next\_move*:

`next_move . `
### 5. Results

And *et voilà*: There you have an AI model playing TTT. Now the question
is how well it works. One of the things I was most curious about was
whether the model figures out what the best opening move is. Anyone who
has played TTT knows that you should always start with the field in the
middle. And indeed, the model also calculates the highest win percentage
for this move out of all possible opening moves:

![](/images/blog/opening_move.JPG){.img-responsive
.no-border}
Now lets see if the AI beats the random player. Therefore, I simulated
200 games each of "random vs. random", "aggressive AI vs. random", and
"defensive AI vs. random". And indeed, the aggressive AI wins 85 % of
the time, losing only 8 % of the games. The player who makes the first
move has a distinct advantage in the game of TTT so the expectation for
win and losses at baseline is not equal. A random player 1 wins about 65
% of the time against another random player. Surprisingly, the defensive
AI fairs even worse winning only 47 % of the time with the opponent
winning just as many games.

There are several ways in which we could improve the AI. Feel free to
fork the version on GitHub and play around with it
(https://github.com/JohMueller/tic\_tac\_toe\_AI). We could for example
build a new simulation dataset with games where the AI plays itself and
then train the neural net again. This would go in the direction of
reinforcement learning. Or we could add some kind of tree-search
simulation where we not only evaluate the board after the next move but
look two or three moves ahead. In this case we could discard the neural
net all along and just implement a minimax solution. A very cool
solution was implemented by Daniel Slater. He took all the different
components that DeepMind used for Alpha Go and applied them on this
smaller scale for TTT
(https://www.youtube.com/watch?v=Meb5hApAnj4&t=216s) which is a
brilliant way to understand the core concepts behind one of the most
advanced AI projects out there.

------------------------------------------------------------------------


