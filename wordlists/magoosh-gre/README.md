## Magoosh GRE Flashcards wordlist (1000 words)

### magoosh-gre-1000-words_oct01.txt
Text file extracted from Magoosh official wordlist [magoosh-gre-1000-words_oct01.pdf](https://s3.amazonaws.com/magoosh.resources/magoosh-gre-1000-words_oct01.pdf), using [pdfminer.six](https://github.com/pdfminer/pdfminer.six).


### magoosh-gre.py
Script to wash the magoosh GRE 1000 flashcards raw text into a structured JSON.

### magoosh-gre.json
Structured object washed from the wordlist. Basically is a map of each word in wordlist to its definition, part of speech, and example in sentences, as well as it's level and other extra informations. e.g.
```json
{
  "aberrant": {
      "level": "Common (High-frequency) Words",
      "definition": "markedly different from an accepted norm",
      "part": "adjective",
      "example": "When the financial director started screaming and throwing food at his co-workers, the police had to come in to deal with his aberrant behavior."
  }
}
```
