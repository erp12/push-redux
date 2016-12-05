Title: Introduction To Push
Summary: Introduction to the Push language and Push Genetic Programming.

<a name="push_lang"></a> 
#### The Push Language
 
The following paragraph has been taken from the Push language [homepage](<http://faculty.hampshire.edu/lspector/push.html>):

>Push is a programming language designed for evolutionary computation, to be used as the programming language within which evolving programs are expressed. Push features a stack-based execution architecture in which there is a separate stack for each data type. In Push, "code" itself is a data type, allowing programs to manipulate their own code as they run and thereby to implement arbitrary and potentially novel control structures. This expressiveness is combined with syntactic minimality: the only syntax rule is that parentheses must be balanced. It is therefore trivial to generate and transform syntactically valid Push programs.

To demonstrate how Push works, and some of its benefits, we will step through the execution of a simple Push program.

Consider the following program:

`(5 "10" string_from_integer exec_dup (string_concat integer_from_string))`

The first step to executing a push program is to push the whole program (as a list) onto the exec stack. Below is the state of the Push stacks.

| Stack   | Contents                                                                    |
|---------|-----------------------------------------------------------------------------|
| Exec    | `(5 "10" string_from_integer exec_dup (string_concat integer_from_string))` |
| Integer |                                                                             |
| String  |                                                                             |

Generally, Push language implementations contain more stacks than the 3 listed above, but this example only requires the 3 thus they are the only stacks shown.

Each step of Push program execution involves 1) popping the top item off the exec stack. 2) Processing the item in the interpreter 3) Pushing results onto the appropriate stacks, when applicable.

For the first step of execution, the only item on the exec stack is a list containing the entire program. When the push interpreter encounters a list, it simply pushes the contents of the list onto the exec stack in reverse order (which preserves the execution order). The resulting state of the stacks is as follows:

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `5 "10" string_from_integer exec_dup (string_concat integer_from_string)` |
| Integer |                                                                           |
| String  |                                                                           |

At this stage in our example, the item on top of the exec stack is a 5, which is a literal value (as opposed to an instruction, which we will see later). When a literal value is processed by the interpreter, it is simply placed on the stack corresponding to its type. Thus, the new state is as follows:

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `"10" string_from_integer exec_dup (string_concat integer_from_string)`   |
| Integer | 5                                                                         |
| String  |                                                                           |

For the next step in the program execution, the item that is now on top of the exec stack is another literal. This time it is a string. 

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `string_from_integer exec_dup (string_concat integer_from_string)`        |
| Integer | 5                                                                         |
| String  | "10"                                                                      |

Now the top item on the exec stack is an instruction. An instruction is a function that has access to the items on the stacks, and can push its results onto any of the stacks. Push language implementations must include a fairly comprehensive instruction set. For more information on Push instructions, see the [Instructions Page](../instructions/index.html).

The `string_from_integer` instruction is the instruction that will pop the top integer, cast it to a string, and then push the resulting string onto the string stack. Thus, the resulting state of the stacks is as follows:

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `exec_dup (string_concat integer_from_string)`                            |
| Integer |                                                                           |
| String  | "5" 10"                                                                   |

The next item on the exec stack is the ``exec_dup`` instruction. This instruction demonstrates the expressiveness of the Push language. Push programs continue to run until the exec stack is empty. Push instructions have the ability to modify the stacks, including the exec stack. This makes it trivial to create instructions that implement various forms of conditionals, modularity, and code reuse. The ``exec_dup`` instruction is one of the simplest forms of code reuse. It pushes a copy of the next item on the exec stack to the exec stack. 

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `(string_concat integer_from_string) (string_concat integer_from_string)` |
| Integer |                                                                           |
| String  | "5" 10"                                                                   |

In this case, the duplicated item was a list of instructions. We can see now that this has the potential to reuse large sections of code easily.

The top item on the exec stack is now a list. As mentioned above, the contents will be pushed onto the exec stack in reverse order.

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `string_concat integer_from_string (string_concat integer_from_string)`   |
| Integer |                                                                           |
| String  | "5" 10"                                                                   |

Now the top item of the exec stack is the `string_concat` instruction. This instruction will concatenate the top two strings and push the result back onto the string stack.

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `integer_from_string (string_concat integer_from_string)`                 |
| Integer |                                                                           |
| String  | "105"                                                                     |

The `integer_from_string` instruction parses the top string to an integer and pushes the result to the integer stack.

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `(string_concat integer_from_string)`                                     |
| Integer | 105                                                                       |
| String  |                                                                           |

The next item on the exec stack is a list, so it will be unpacked.

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `string_concat integer_from_string`                                       |
| Integer | 105                                                                       |
| String  |                                                                           |

Next, the interpreter will encounter another `string_concat` instruction, but there are no items on the string stack. Push was designed so that any nested structure of literals and instructions is a valid program (assuming balanced parentheses). One important behavior of Push interpreters that helps achieve this design is how instructions are handled when the required arguments aren't present. In cases like this, the instruction is skipped over. In other words, no values are popped from the stacks except the instruction on the exec stack.

This behavior is extremely important when using the Push language in Genetic Programming frameworks because randomly generated programs often contain many instructions that do not have the required instructions when executed.

The resulting state of the stack will simply be as follows:

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    | `integer_from_string`                                                     |
| Integer | 105                                                                       |
| String  |                                                                           |

The `integer_from_string` instruction is also lacking arguments, and will be ignored.

| Stack   | Contents                                                                  |
|---------|---------------------------------------------------------------------------|
| Exec    |                                                                           |
| Integer | 105                                                                       |
| String  |                                                                           |

The above state is the output of the push program. The remaining items on the stacks can be utilized as needed.


<a name="push_gp"></a> 
#### Push Genetic Programming

The following paragraph has been taken from the Push language [homepage](http://faculty.hampshire.edu/lspector/push.html).

>PushGP is a genetic programming system that evolves programs in the Push programming language. Features include:
>
>   - Multiple data types without constraints on code generation or manipulation.
>   - Arbitrary control structures without constraints on code generation or manipulation.
>   - Arbitrary modularity without constraints on code generation or manipulation.
>   - Automatic program simplification.

##### Generating Random Programs

Most modern Push implementations can generate random Plush genomes, rather than Push programs. The difference between Plush Genomes and Push Programs is explained in detail on the [Programs and Genomes page](../programs_and_genomes/). Plush genomes can easily be translated into Push programs and executed.

When generating random genomes, PushGP relies on **atom generators** and **epigenetic markers**.

An "atom" refers to either an instruction or a literal. **Atom generators** are things that produce an "atom". For example, an anonymous function that returns a random floating point value between 0 and 1 could be an **atom generator**. At the time of random program generation (but NOT program execution) this anonymous function could be used to generate a literal in the program. An instruction can also be considered an **atom generator** that adds itself to the random program.

When generating a random genome, PushGP selects **atom generators** at random. If the atom generator is a constant, it is added to the genome. If the atom generator is an anonymous function, it is called and its response if added to the genome. If the atom generator is an instruction, it is added to the genome.

**Epigenetic Markers** are how the nested structure of a push program is captured in the linear genome. They are extra values associated with each gene that denotes if the gene places an parenthesis in the program, and/or if the gene is silent. **Epigenetic Markers** are discussed more in depth on the [Programs and Genomes page](../programs_and_genomes/index.html). 

When generating random individuals during PushGP, random Plush genomes are generated and translated into programs. The individuals in the evolutionary population store both their genomes and their programs. Programs are executed during the individuals fitness evaluations, while genomes are manipulated by the genetic operators. When new genomes are needed (aka offspring) a new individual is created with the new genome, and the program for the new individual is produced by translating the new genome.


##### Evaluating Programs

Every Genetic Programming problem requires an error function, sometimes called a fitness function. This function takes a program produced by evolution, executes it, and evaluates how well it solved the problem.

In most Push GP systems, error functions return a vector of numbers representing the program's error on each test case. The total error of the program is the sum of the error vector. During evolution, some selection methods select parents based on a program's total error, while other utilize the dis-aggregated error vector.

A program whose total error is equal to, or below, the stopping threshold parameter (default to 0) is considered a solution.

>Currently most PushGP implementations only support using evolution to minimize a programs *errors*. It is also common to evaluate programs based on a *fitness* value that evolution attempts to maximize, but this is less common.

##### Selection and Variation

Selection events pick a single individual from the population to perform a variation operation on.

The Push language's permissive syntax was designed to allow programs themselves to be treated as genomes, for which random variation is safe. In much of the past work, Push programs themselves did serve as genomes, which would be randomly varied and recombined.

More recently, a linearized representation of Push programs, called Plush, has been developed. Read more about Plush on [this post](https://push-language.hampshire.edu/t/plush-genomes/279) found on the Push Discourse.

Most modern PushGP implementations contain variation operators (mutations and recombination) that manipulate Plush genomes. To read more about common genetic operators found in PushGP implementations, see the [Genetic Operators page](../genetic_operators/index.html).