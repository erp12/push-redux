Title: Names and Tags

"Tags," in genetic programming and particularly in the context of Push/PushGP, are identifiers that can be used to name, store, and retrieve code and data as a program runs. The distinctive property of Tags relative to the "Names" used in Push1-Push3 is that Tags can match inexactly. This feature is hypothesized to be helpful for the evolution of reference, and hence for the evolution of complex and modular systems.

####History and Motivation

Tags were developed as a successor/replacement for Push "Names," which were included in the language (in a couple of different experimental forms) through Push3 ([GECCO paper2](http://faculty.hampshire.edu/lspector/pubs/push3-gecco2005.pdf), [language specification3](http://faculty.hampshire.edu/lspector/push3-description.html)). While Names performed as expected in hand-written Push programs, they were rarely (if ever) used in evolved programs. One reason probably stems from the number of Names in circulation during evolution: If there are too few then evolving systems will not be able to scale, while if there are too many then it will be rare for storage/retrieval operations will refer to the same names by chance, and therefore unlikely that name usage will evolve.

The conceptual difference between Tags and Names is that Tags can match inexactly: If one tries to retrieve something with a particular Tag, but that exact tag has not previously been used to tag (store) anything, then the retrieval operation will return the item that has been tagged with the closest matching tag. This concept of tags, with inexact matching, stems from the work of John Holland (perhaps discussed most fully in his book *Hidden Order: How Adaptation Builds Complexity*).

With Tags, as long as at least one thing has been tagged, all tag references will refer to something. The motivation for providing Tags in an evolutionary computation system is the hypothesis that this feature - that references may be produced easily by chance and change incrementally over evolutionary time - may be enough to get the ball rolling on the use of storage/reference in an evolving system.

In principle, tags and tag-based reference mechanisms could be added to many different kinds of evolutionary computation systems, including many different kinds of genetic programming systems. However, attempts to provide tagging mechanisms in tree-based genetic programming [have had limited success](http://faculty.hampshire.edu/lspector/pubs/p815.pdf).

A related concept of tags, also deriving from Holland's work and the notion of inexact matching, but different in details from the concept described here for evolutionary computation, has been used in game-theoretic studies of the evolution of altruism (e.g. [this](https://www.nature.com/articles/35106555), which started it all, and [this](http://faculty.hampshire.edu/lspector/pubs/spector-tags-alife.pdf), and [this](http://faculty.hampshire.edu/lspector/pubs/multitags-GPTP06.pdf) from members of the Push community).

####Tags in Clojush

In Clojush tags are integers that are "baked in" to tagging and tag-based retrieval instructions. For example, the instruction `tag_exec_123` will tag the top item on the `exec` stack with the tag 123, and the instruction `tagged_456` will push whatever has been tagged with the tag that most closely matches 456 onto the `exec` stack. "Closeness" is implemented in a one-directional way, with wraparound: if nothing has been tagged with 456 then 457 is the closest, followed by 458, 459, etc., and if no higher-numbered tags were used then the closest is 0, then 1, etc.

The full set of tag-related instructions can be found in [clojush.instructions.tag](https://github.com/lspector/Clojush/blob/master/src/clojush/instructions/tag.clj).

Tagging is generally enabled by including tag-related "erc" (ephemeral random constant) functions in the atom-generators of a PushGP run. These functions are defined in [clojush.instructions.tag](https://github.com/lspector/Clojush/blob/master/src/clojush/instructions/tag.clj) and demonstrated in problems such as [clojush.problems.demos.tagged-regression](https://github.com/lspector/Clojush/blob/master/src/clojush/problems/demos/tagged_regression.clj).

Early experiments with tags in Clojush are described [here](http://faculty.hampshire.edu/lspector/pubs/spector-gptp11-preprint.pdf) and [here](http://faculty.hampshire.edu/lspector/pubs/spector-gptp11-preprint.pdf).

####Be Careful!
Tags, in their current incarnation, have not been found to provide useful functionality beyond a small set of problems with very particular characteristics, namely the lawnmower and DSOAR (dirt-sensing object-avoiding robot) problems. In these problems, the increases in performance can be attributed to the fact that tags were primarily used to implement looping constructs. Additionally, these problems work by side-effect, meaning an infinite loop to "mow the whole lawn" is sufficient, as the program does not need to return a correct functional value.

Tags do not provide any utility on numerous other problems, including symbolic regression and classification problems for which modularity would be very natural to use for a human programmer. On none of these problems did the presence of tags increase performance. And in fact, in many cases, tags may make the things even worse. Introducing the functionality of tags adds a lot of tag based instructions in the program, many of which might not be useful at all. In this way, any improvement in the performance that tags introduce might not be able to compensate for this unnecessary overhead.

To learn more about names and tags, see [this thread](https://push-language.hampshire.edu/t/tags-and-what-happened-to-names) on the Push-language Discourse.