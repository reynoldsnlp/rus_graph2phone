# Rob Reynolds final project - Ling 361

## Enhancing lexicon with mal-rules for language learners

* Language learners (and other populations) are less well understood by ASR
* Spoken learner data is difficult to find/generate
* I want to identify factors of native speaker models that can be tweaked to improve L2 usability
    * ...beginning with the dictionary!
* My approach: add non-standard pronunciations to dictionary
	* UDAR (UDAR Does Accented Russian)
	* Mal-rules to produce learner-like surface forms
	* ORCA grant for student to make Russian graph2phone 
* My question: could this graph2phone engine have application in ASR?

## Methods

* I could not find anyone doing similar work
* [West Point Russian Speech corpus](https://catalog.ldc.upenn.edu/LDC2003S05)
	* 4,181 speech files  (118 of which were deemed unusable)
		* 2,290 Native Russian  (29 speakers)
		* 1,891 Non-native  (22 speakers, L1s: English, German, French, Czech, Hausa, Hebrew, Ukrainian)
	* 96 sentences (528 tokens, 351 types)
* Train model on native Russian speaker data, test on L2 Russian data
* Kaldi monophone model
	* I tried first triphone pass (TRI1), but results were worse)

### Mal-rules

* I do not have Russian graph2phone yet, so I made a few simple additions to dictionary
* I focused on Russian phonemes that are inherently difficult for foreigners
	* soft l -> hard l
	* hard t -> soft t
	* soft d -> hard d
	* hard sh -> soft sh
	* y -> i
* One entry in dictionary is standard, and a second entry has learner pronunciation

## Results

* Modest improvements, probably not significant

PLAIN

|         |   WER     |  SER |
| ------- | --------- | ------- |
|   count |  99.000000 |  99.000000 |
|    mean |  8.390606  | 22.249091 |
|    std  |  3.416785  |  7.254705 |
|    min  |  4.260000  | 11.390000 |
|    25%  |  5.915000  | 17.330000 |
|    50%  |  7.360000  | 20.250000 |
|    75%  | 10.030000  | 26.235000 |
|    max  | 20.300000  | 49.370000 |

ENHANCED

|          |  WER      | SER |
| -------- | --------- | ---------- |
|    count | 99.000000 |  99.000000 |
|    mean  | 7.955960  | 21.797273 |
|    std   | 2.907436  |  6.777031 |
|    min   | 3.760000  | 10.130000 |
|    25%   | 6.020000  | 16.935000 |
|    50%   | 7.060000  | 20.900000 |
|    75%   | 9.530000  | 26.095000 |
|    max  | 19.300000  | 44.300000 |

* Somewhat promising; I might try a more robust experiment with graph2phone mal-rules


