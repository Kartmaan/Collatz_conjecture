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
- Display more detailed statistics (flight time, time on altitude >n, max altitude, average altitude, number of even/odd values)
- Save graphics in .png format
- Copy the sequence(s) generated to the clipboard
- Randomly generate Collatz sequences

## Screenshots
### Interface
![collatz](https://user-images.githubusercontent.com/11463619/96777644-df9fd100-13ea-11eb-8404-d04e714da630.png)
### Sequences pasted from clipboard
![paste](https://user-images.githubusercontent.com/11463619/96784908-5d191080-13ee-11eb-9933-d3088b0c9c99.png)
### Graph saved as .png image
![97-649](https://user-images.githubusercontent.com/11463619/96784880-54283f00-13ee-11eb-8851-f90d954f31a4.png)
