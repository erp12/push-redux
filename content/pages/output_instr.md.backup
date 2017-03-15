Title: Output Instructions
Nav: instructions

How can outputs be retrieved after executing Push programs?

After the execution of a push program, the result is the state of all of the stacks. Often, the values that are considered the output of the program are taken from the top of these stacks.

#### Output Instructions

Depending on the problem, other forms of output might be required. For example, printing a particular string. Various special instructions have been written to add this functionality.

##### Printing Instructions

PushGP has been known to perform well on General Software Synthesis tasks compared to most other forms of GP. Many problems in this domain require that a solution return an output value, but also print various other values while the program is being executed.

In most programming languages, this would be accomplished by built in functions that write to standard out. The Push language simulates this in a way that can be captured by fitness functions during evolution through the use of the `output` stack.

The `output` stack initializes with only 1 element: an empty string. The Push instruction set contains `print` instructions that take items from other stacks, casts them to a string, and concatenates them to the empty string on top of the `output` stack. There is an additional `print` instruction that appends a newline character to the `output` stack string.

After a Push program has been finished being executed by the push interpreter, the string on top of the `output` stack is considered the printed output of the program, as it is equal to what would have been written to standard out in conventional programming languages.

##### Class Voting Instructions

When using PushGP on classification problems, the goal is to evolve a program that produces a class label, `l`, such that `0 < l <= c` where `c` is the number of classes in the classification problem. A common way of achieving this is by using class voting instructions. 

As mentioned in the previous section, the bottom element of the `output` stack is a string reserved for use by the printing instructions. Elements 1 to `c` of the `output` stack each hold numeric values corresponding to the amount of "votes" given to each class. 

For example, if a push program is executed and the resulting `output` stack looks as follows:

```
["", 4.12, 0.12, -5.3, 10.77, 1.1]
```

The class with the most votes would be class 4. This is because the most votes is 10.77, which appear at index 4 of the `output` stack.

These class votes get added to the output stack through "voting instructions" which pull numeric values off of either the `integer` or `float` stacks and add them to a particular index of the `output` stack.

Note that this system allows for real-valued votes and negative votes.