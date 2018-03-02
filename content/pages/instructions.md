Title: Push Instructions

#### What are Push Instructions?

An instruction is a function that has access to the items on the stacks, and can push its result on to any of the stacks.

Consider this python implementaion of the `integer_add` instruction.

```python
def integer_add(state):
    if len(integer stack of state) > 1:
        i = top integer + second integer.
        pop integer stack of state.
        pop integer stack of state.
        push i onto integer stack of stack.
```

Notice that nothing happens to the `state` if there are insufficient arguements to the instruction.

#### Typical Push Instruction Set
The following sections describe some of the commonly used Push instructions categorized according to the type of stacks they modify. The columns *Input* and *Output* specify the type of stacks to take input from or put the output onto.

##### Boolean
| Instruction | Operation  | Input | Output|
|-------------|------------|-------|-------|
| `boolean_and` | logical AND of top two items | `:boolean` | `:boolean`| 
| `boolean_or` | logical OR of top two items | `:boolean` | `:boolean`| 
| `boolean_not` | logical NOT of top item | `:boolean` | `:boolean`| 
| `boolean_xor` | logical XOR of top two items| `:boolean` | `:boolean`| 
| `boolean_invert_first_then_and` | logical AND of the second item with the logical NOT of the first item | `:boolean` | `:boolean`| 
| `boolean_invert_second_then_and` | logical AND of the first item with the logical NOT of the second item | `:boolean` | `:boolean`| 
| `boolean_frominteger` | Pushes FALSE if the top item is 0, or TRUE otherwise | `:integer` | `:boolean`| 
| `boolean_fromfloat` |Pushes FALSE if the top item is 0, or TRUE otherwise | `:float` | `:boolean`| 


##### Numbers 
Here, `:number` has been used as a general type for numbers : floats and integers.

| Instruction | Operation  | Input | Output|
|-------------|------------|-------|-------|
| `number_add` | sum of the top two items | `:number` | `:number` |
| `number_sub`| first item subtracted from second item   | `:number` | `:number` | 
| `number_mult` | product of the top two items |  `:number` | `:number` |
| `number_div` | second item divided by first item |  `:number` | `:number` |
| `number_mod` | modulus of the top two items   |  `:number` | `:number` |
| `number_fromboolean`| converts FALSE to 0 or 0.0, TRUE to 1 or 1.0  |  `:boolean` | `:number` |
| `number_fromstring` | string to number conversion   |  `:string` | `:number` |
| `number_inc` | increment the top item by 1  |  `:number` | `:number` |
| `number_dec` | decrement the top item by 1  |  `:number` | `:number` |

##### String 

| Instruction | Operation  | Input | Output|
|-------------|------------|-------|-------|
| `string_concat` | concatenate top two strings | `:string` | `:string` |
| `string_take` | take the first n chars in the top string, where n is the top integer |`:string`, `:integer` |`string`|
| `string_conjchar`| concatenate the top char onto the top string | `:string, `:char` | `:string`|
|`string_length` | length of the top string |`:string` |`:integer`
|`string_reverse` |reverse the string |`:string` |`:string`
|`string_parse_to_chars` |parse string to a set of strings which have only one char |`:string` |`:string`
|`string_contains` |check whether the top string is a substring of second string |`:string` |`:boolean`
|`string_replace` | In third string replaces all occurences of second string with first string |`:string` |`:string`|
|`string_setchar`| Returns a function that sets char at index in string | `:string`, `:char`, `"integer`| `:string`|

##### Code
Following are the instructions for `:code` and `:exec`.

| Instruction | Operation  | Input | Output|
|-------------|------------|-------|-------|
|`code_append` |concatenate the first 2 items |`:code` |`:code`|
|`code_atom` |if the first item is sequence, push FALSE, otherwise TRUE |`:code` |`:boolean`
|`code_car` | push the first element of the top sequence|`:code` |`:code`
|`code_cdr` | push the top sequence excluding the first element |`:code` |`:code`
|`code_cons` |Concatenate the second item of `:code` into the first one |`:code` |`:code`
|`code_do` |execute the top item (pop after execution)|`:code` |`:exec`
|`code_do*` |execute the top item (pop before execution)|`:code` |`:exec`
|`code_do*range` |while the counter moves from the second item of `:integer` to the first item of `:integer` by 1 (+ or -), keep executing the first item of `:code`|`:code` |`:exec`
|`exec_do*range` |similar to `code_do*range` but the source is from `:exec`|`:exec` |`:exec`
|`code_do*count` |Execute the first item of `:code` for (the first item of `:integer`) times|`:code` |`:exec`
|`exec_do*count` |similar to `code_do*count` but the source if from `:exec`|`:exec` |`:exec`
|`code_wrap` |Wrap up the first item of `:code` with `(list )` |`:code` |`:code`
|`code_list` |List the first two items of `:code` |`:code` |`:code`
|`code_length` |Get the length of the first item of `:code` |`:code` |`:code`
|`code_map` |Maps the first item of `:code` and the first item in `:exec` |`:code`, `:exec` |`:code`
|`code_member` |Whether the second item in `:code` belongs to the first item of `:code` or not |`:code` |`:boolean`
|`code_nth` |Get the nth (mod the length of code) from a piece of code |`:code`, `:integer` |`:code`
|`code_nthcdr` |Delete all instructions before the nth (mod the length of code) |`:code`, `:integer` |`:code`
|`code_null` |Determine whether the first item in `:code` is an empty sequence or not |`:code` |`:boolean`
|`code_extract` |Use `code-at-a-point` to return a subtree of the first item from `:code` |`:code`, `:integer` |`:code`
|`code_insert` |Insert a piece of code into another by `insert-code-at-a-point` |`:code`, `:integer` |`:code`
|`code_subst` |To name the first, second and third items from `:code` 1, 2 and 3. Replace all 3 in 1 with 2. |`:code` |`:code`
|`code_contains` |Exam whether the second code item contains the first one as its subtree or not |`:code` |`:boolean`
|`code_containing` |Returns the smallest subtree of the first item which contains the second item. |`:code` |`:code`
|`code_position` |Get the position in which the second code item appears in the first one. -1 if no appearance is found. |`:code` |`:integer`



This page introduces instructions for `:code` and `:exec`.

== `codemaker`
Codemaker pops an item from a specific stack and push it into the code stack. Codemaker is a high level function which is used to construct push instructions `code_fromboolean`, `code_fromfloat`, `code_frominteger` and `code-quote`, which moves an item from `:exec` to `:code`.

== Stack manipulations
[options="header"]
|====
|Instruction |Explanation |input |output
|`code_append` |Append the first 2 items in `:code` |`:code` |`:code`
|`code_atom` |If the first item in `:code` is a sequence -> false, otherwise true |`:code` |`:boolean`
|`code_car` |Perform `first` on the first item of `:code` |`:code` |`:code`
|`code_cdr` |Perform `rest` on the first item of `:code` |`:code` |`:code`
|`code_cons` |Concatenate the second item of `:code` into the first one |`:code` |`:code`
|`code_wrap` |Wrap up the first item of `:code` with `(list )` |`:code` |`:code`
|`code_list` |List the first two items of `:code` |`:code` |`:code`
|`code_length` |Get the length of the first item of `:code` |`:code` |`:code`
|`code_map` |Maps the first item of `:code` and the first item in `:exec` |`:code`, `:exec` |`:code`
|`code_member` |Whether the second item in `:code` belongs to the first item of `:code` or not |`:code` |`:boolean`
|`code_nth` |Get the nth (mod the length of code) from a piece of code |`:code`, `:integer` |`:code`
|`code_nthcdr` |Delete all instructions before the nth (mod the length of code) |`:code`, `:integer` |`:code`
|`code_null` |Determine whether the first item in `:code` is an empty sequence or not |`:code` |`:boolean`
|`code_extract` |Use `code-at-a-point` to return a subtree of the first item from `:code` |`:code`, `:integer` |`:code`
|`code_insert` |Insert a piece of code into another by `insert-code-at-a-point` |`:code`, `:integer` |`:code`
|`code_subst` |To name the first, second and third items from `:code` 1, 2 and 3. Replace all 3 in 1 with 2. |`:code` |`:code`
|`code_contains` |Exam whether the second code item contains the first one as its subtree or not |`:code` |`:boolean`
|`code_containing` |Returns the smallest subtree of the first item which contains the second item. |`:code` |`:code`
|`code_position` |Get the position in which the second code item appears in the first one. -1 if no appearance is found. |`:code` |`:integer`
|====

== Execute codes

[options="header"]
|====
|instruction |explanation
|`code_do` |execute the code (by pushing both it and code_popper to `:exec`)
|`code_do*` |execute the code (by popping it and pushing to `:exec`)
|`code_do*range` |While the counter moves from the second item of `:integer` to the first item of `:integer` by 1 (+ or -), keep executing the first item of `:code`
|`exec_do*range` |similar to `code_do*range` but the source is from `:exec`
|`code_do*count` |Execute the first item of `:code` for (the first item of `:integer`) times
|`exec_do*count` |similar to `code_do*count` but the source if from `:exec`
|`code_if` |If the first item in `:boolean` is true, run the second item of `:code`, otherwise run the first one
|`exec_if` |true  -> run the fist one from `:exec`, false -> run the second one
|`exec_when` |first item from `:boolean` is true -> pop `:boolean`, otherwise pop both `:boolean` and `:exec`. To understand: if true, it would be executed later at some point.
|====

