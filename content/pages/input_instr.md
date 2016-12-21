Title: Input Instructions

How can inputs be provided for Push programs?

When Push was first being developed, the idea was that you would preload inputs onto stacks, then run your program, and then find outputs on stacks after the program terminates. This was modeled roughly on how we thought of push-down automata being used in formal language theory.

However, Hampshire student Alan Robinson soon discovered, and documented in his [Division III](http://faculty.hampshire.edu/lspector/robinson-div3.pdf) thesis, the fact that it can be more helpful to define instructions that can be called to re-push inputs on demand, possibly multiple times during the execution of a program. This seems obvious in retrospect, since the original scheme provided only one copy of each input and required a program to duplicate it and keep track of copies on stacks if the inputs would be needed in multiple parts of a program.

It then became common practice to define input instructions for each problem, and each implementation of Push provided some way to do this, although the details for implementing these varied from implementation to implementation and had to be revisited for each new problem.

#### The Input "Stack"

The most common way to implement input instructions is by adding an additional stack to the push state, called the input stack. This stack does not behave like a stack, because values are never popped off of it. Instead, it acts as a list which stores all input values, of all types.

Using this stack, we can define instructions that get (copy) values from a particular index of the input stack. This gives our push programs access to all input values.

#### Example

Suppose we would like to create a classifier for the famous [iris dataset](https://archive.ics.uci.edu/ml/datasets/Iris). We typically think of the iris dataset as having the following 4 predictors:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

If we use a PushGP framework to create our classifier, we will be attempting to evolve a *program* that takes the 4 predictors as inputs and outputs the class value.

To give our programs access to the 4 input vales, we first load the input values onto the input stack. 

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Input   | `Sepal_Length Sepal_Width Petal_Length Petal_Width`                       |
| Exec    |                                                                           |
| Float   |                                                                           |

Note that we are using the predictor names in this demonstration, but in practice the input stacks would the actual measurements of the iris being classified. Now let's consider the following program:

`(input_2 integer_from_float integer_dec)`

The initial state of the stacks would be:

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Input   | `Sepal_Length Sepal_Width Petal_Length Petal_Width`                       |
| Exec    | `(input_2 integer_from_float integer_dec)`                                |
| Float   |                                                                           |

The first instruction of the program is `input_2`, which will copy the value at index 2 on the input stack and place it on top of the exec stack.

In this case, the `input_2` instruction will place the `Petal_Length` value on top of the exec stack.

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Input   | `Sepal_Length Sepal_Width Petal_Length Petal_Width`                       |
| Exec    | `Petal_Length integer_from_float integer_dec`                             |
| Float   |                                                                           |

We can see that the next value to be processed is now `Petal_Length`, which will be a floating point literal. The push interpreter will recognize the type of `Petal_Length` and push it to the float stack. 

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Input   | `Sepal_Length Sepal_Width Petal_Length Petal_Width`                       |
| Exec    | `integer_from_float integer_dec`                                          |
| Float   | `Petal_Length`                                                            |

We can now see that we can provide and arbitrary number of inputs to our programs through this input stack. These inputs can be of any type that the push interpreter can handle. 





