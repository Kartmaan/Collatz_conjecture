# Collatz_conjecture

## What's Collatz conjecture ?
The Collatz conjecture is defined as follows:
- The starting value n is a positive integer
- If the previous term x is even, the next term = x/2
- If the previous term x is odd, the next term = x*3 + 1
The conjecture is that whatever the value of n, the sequence will always reach 1 before oscillating indefinitely on the values 4,2,1,4,2,1,4,2,1, .... (in this program, the sequence generation process stops as soon as it encounters a 1)

## What does the program do?
The program designed with PyQt5 generate sequences from the Collatz conjecture. The program allows to:
- Visualize graphically a sequence from a single input value
- Compare the sequences of two input values in the form of two superimposed graphs
- Display more detailed statistics (flight time, max altitude, number of even / odd values, etc.)
- Save graphics in .png format
- Copy the lists of numbers generated to the clipboard
- Randomly generate numbers
