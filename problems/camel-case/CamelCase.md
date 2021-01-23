# CamelCase

There is a sequence of words in [CamelCase] as a string of letters, `s`, having the following properties:

- It is a concatenation of one or more words consisting of English letters.
- All letters in the first word are lowercase.
- For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given `s`, determine the number of `s`:

*Example*

```text
s = oneTwoThree
```

There are 3 words in the string: "one", "Two", "Three".

*Function parameters*

- `string s`: the string to analyze

*Function return*

- `int`: the number of words in `s`

*Constraints*

- Length of `s` should be in the range `[1, 100000]`

*Sample input*

```text
saveChangesInTheEditor
```

*Sample output*

```text
5
```

[CamelCase]: https://en.wikipedia.org/wiki/CamelCase