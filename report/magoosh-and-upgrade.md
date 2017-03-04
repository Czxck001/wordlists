## Reports
Structured wordlists allow us to directly handle the words to learn and review them in an easier way. I've made some statistics on them and poked around finding some relations between them.

I devide the words into three categories of length: short words for length less than 7 charactors; intermediate words for length not less than 7 but less than 10 charactors; long words for longer than or equal to 10.

This devision is based on the following observations: Short words often doesn't consist of root. Mid words often consists of a root with a simple suffix. And long words are usually composed by a root with prefix, root and one or more than one suffixs. These different modes on word building *require* different ways to memorize them.

Another thing I found useful is to explore the relationship between the wordlists. It is supposed that if a word is found in more than one wordlist, it should be more important. Similarities and differencies of wordlists also suggest the quality of them.


### Magoosh GRE Flashcards wordlist (1000 words)
```
Short words (len < 7): 217 (21.70%)
Mid words (7 <= len < 10): 492 (49.20%)
Long words (10 < len): 291 (29.10%)
```

### GRE Vocabulary Upgrade (1080 words)
```
Short words (len < 7): 252 (23.38%)
Mid words (7 <= len < 10): 534 (49.54%)
Long words (10 < len): 292 (27.09%)
```

### Comparison between wordlists of Magoosh GRE flashcards and GRE Vocabulary Upgrade
They shared 672 words, which is supposed to be the most important words.

I dumped the list into `conj/magoosh-upgrade.json` and conducted the word-length statistics again:
```
Short words (len < 7): 149 (22.17%)
Mid words (7 <= len < 10): 335 (49.85%)
Long words (10 < len): 118 (27.98%)
```
