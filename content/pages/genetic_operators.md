Title: Evolutionary Operators
Summary: A description of slection, mutation, and recombination operators typically used in PushGP systems.



>To learn more about Selection, Mutation, and Recombination algorithms, I would highly recommend the "Field Guide To Genetic Programming" book, which is freely shared online [here](http://dces.essex.ac.uk/staff/rpoli/gp-field-guide/A_Field_Guide_to_Genetic_Programming.pdf). The content is not exactly the same as this page because the book is not specific to PushGP.

<a name="selection"></a> 
#### Selection

A selection event refers to the points during evolution where an individual is probabilistically chosen based on fitness. Individuals with better fitness (ie. lower error) are more likely to be chosen. The chosen individuals are typically used as "parents" in Mutation or Recombination.

##### Lexicase Selection

Lexicase selection selects and individual from the Pareto front, and tends to select individuals which have specialized at solving some test cases.

>"Unlike most traditional parent selection techniques, lexicase selection does not base selection on a fitness value that is aggregated over all test cases; rather, it considers test cases one at a time in random order" 
>-- T. Helmuth, L. Spector

Lexicase selection follows the following procedure at *each* selection event:

```
1. Set CANDIDATES to be the entire population.
2. Set CASES to be a list of all of the test CASES in random order.
3. Loop:
    a. Set CANDIDATES to be the subset of the current CANDIDATES that have exactly the best performance of any individual currently in CANDIDATES for the first case in CASES
    b. If CANDIDATES contains just a single individual then return it.
    c. If CASES contains just a single test case then return a randomly selected individual from CANDIDATES
    d. Otherwise remove the first case from CASES and go to Loop.
```
[reference](http://faculty.hampshire.edu/lspector/pubs/lexicase-IEEE-TEC.pdf)

For more information about Lexicase selection, and its benefits, see the following publications:

- [Solving Uncompromising Problems with Lexicase Selection](http://faculty.hampshire.edu/lspector/pubs/lexicase-IEEE-TEC.pdf)
- [Lexicase selection for program synthesis: a diversity analysis](http://cs.wlu.edu/~helmuth/Pubs/2015-GPTP-lexicase-diversity-analysis.pdf)
- [The Impact of Hyperselection on Lexicase Selection](http://cs.wlu.edu/~helmuth/Pubs/2016-GECCO-hyperselection.pdf)


##### Epsilon Lexicase Selection

Lexicase selection generally performs poorly on problems that use continuous output values, such as most regression problems. Epsilon Lexicase Selection is a form of lexicase selection that allows candidates to pass a test case as long as their error is within *epsilon* ( $\epsilon$ ) of the error of the best candidate on the test case. This change dramatically increases the performance of lexicase selection on problems with continuous output values.

For more information about Epsilon Lexicase selection, and its benefits, see the following publication:

- [Epsilon-lexicase selection for regression](http://www.williamlacava.com/pubs/GECCO_lex_reg_preprint.pdf)

##### Tournament Selection

Tournament selection involves selecting the individual with the lowest total error from a small, random subset of the population. This subset is called the tournament. Each time a selection event occurs, a new random subset of the population is placed into the tournament.

<a name="mutation"></a> 
#### Mutation

Mutation operators randomly modify a single parent to create new individuals. These modifications usually involve inserting random code, or removing random parts of the parent. 

##### Uniform Mutation

Uniformly mutates individual. For each token in genome, there is `uniform_mutation_rate` probability of being mutated. If a token is to be mutated, it has a `uniform_mutation_constant_tweak_rate` probability of being mutated using a constant mutator (which varies depending on the type of the token), and otherwise is replaced with a random instruction.

##### Uniform Close Mutation

Uniformly mutates the `close` markers in the individual's plush genes. Each `close` will have a `uniform_close_mutation_rate` probability of being changed, and those that are changed have a `close_increment_rate` chance of being incremented, and are otherwise decremented.

<a name="recombination"></a> 
#### Recombination

Recombination operators typically use 2 or more parents. Unlike mutation, the resulting individual is composed entirely of parts of the parents.

##### Alternation

Uniformly alternates between taking genes from either of the two parent plush genomes. 

Alternation traverses the parent genomes to build the child genome out of tokens taken from the parents. Traversal begins with a “read head” on the first token of the the first parent, and the copying of that token to the child. 

After this and each subsequent step there is a fixed probability of alternating between parents. In other words: moving the read head to approximately the same location in the other parent genome. The probability of alternating at any given step is specified as the `alternation rate.`

When alternating between parents, the position of the read head is subjected to Gaussian noise and may change to a higher or lower index; the standard deviation of the noise is given by the `alignment deviation` parameter. Note that alignment deviation may cause some elements of parent programs to be skipped or to be repeated in the child program.

##### Point Crossover

Point Crossover (sometimes called "subtree crossover") splits each parent genome into a head and tail at a randomly selected crossover point. The new child genome is created by combining the head of one parent and the tail of the other parent. This is called "One Point Crossover."

"Two Point Crossover" refers to the same processes described above with 2 two crossover points.

When performing evolution on linear program representations, it is possible for **Alternation** to perform operations synonymous with $n$-point crossover, as well as other recombinations. This is why Alternation is the most commonly used method of recombination.

#### Gone But Not Forgotten

##### Uniform Linear Transformation with Repair and Alternation in Genetic Programming (ULTRA)

[PAPER](http://faculty.hampshire.edu/lspector/pubs/spector-gptp-2013-preprint.pdf)