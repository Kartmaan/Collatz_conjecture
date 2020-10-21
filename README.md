# Collatz_conjecture

## What's Collatz conjecture ?
The Collatz conjecture is defined as follows:
- The starting value n is a positive integer
- If the previous term x is even, the next term = x/2
- If the previous term x is odd, the next term = x*3 + 1

The conjecture is that whatever the value of n, the sequence will always reach 1 before oscillating indefinitely on the values 4,2,1,4,2,1,4,2,1, .... (in this program, the sequence generation process stops as soon as it encounters a 1). The Collatz conjecture is still an unsolved problem in mathematics, it has not yet been shown that all sequences reach 1 for an integer and positive initial value.

## What does the program do?
The program designed with PyQt5 generate Collatz conjecture sequences. The program allows to:
- Visualize graphically a sequence from a single input value
- Compare the sequences of two input values in the form of two superimposed graphs
- Display more detailed statistics (flight time, max altitude, number of even / odd values, etc.)
- Save graphics in .png format
- Copy the sequence(s) generated to the clipboard
- Randomly generate numbers

![collatz](https://user-images.githubusercontent.com/11463619/96777644-df9fd100-13ea-11eb-8404-d04e714da630.png)
