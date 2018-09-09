---
title: "Tic Tac Toe"
date: 2018-09-08T23:45:48+02:00
image: tic-tac-toe.jpg
summary: "Johannes provides an introduction to build an AI model which play Tic Tac Toe. In 4 simple steps you'll learn to beat any human player."
language: "en"
draft: true
---

A couple of weeks ago I watched a documentary (https://www.alphagomovie.com/) on the team of DeepMind. They developed an Artificial Intelligence (AI) called AlphaGo which was later capable of beating the best player in the Game Go - an ancient Chinese board game considered one of the most difficult games in the world.

As always, the best way to really understand what's going on and how you can train an AI to play a game is coding it yourself. To start slowly, I decided to build an AI that can play the game Tic Tac Toe (TTT). Tic Tac Toe is a simple game where both players have perfect information (like in Chess or Go), but the number of possible games is limited. While there are 10^120 different games in chess and 10^360 possible games in Go, there are only 360.000 possible games in Tic Tac Toe.

Tic Tac Toe has, in addition, very simple rules. The goal of an AI model for the game would be to implement some kind of evaluation function that can determine whether or not a move is good given the situation on the board. As the possibilities of different games are so limited it is actually possible to solve TTT with a brute-force minimax algorithm (https://www.r-bloggers.com/tic-tac-toe-part-3-the-minimax-algorithm/). But where is the fun in that? I want the model to figure out good moves itself. So: what do we need to write an AI that can play the game?

1. Build the game mechanics
2. Generate a dataset to train the AI
3. Build a deep neural network that can evaluate a board position
4. Implement a function that chooses the best next move
