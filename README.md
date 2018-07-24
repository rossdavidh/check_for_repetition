# check_for_repetition
utility to check my own writing for repetitive use of words (other than stopwords such as a,and,the,etc.)

Usage:
In the same directory as "my_awesome_file.txt", type this at the command line:
python check_for_repetition.py my_awesome_file.txt

You will get terminal output of sentences that appear to have repetition, such as:
We decided to think it over, and walked outside to think it over. [('think', 2)]

Note that here only the word "think" is flagged, for 2 usages, and neither "it" nor "over" are flagged.

Of course, in many cases repetition is just fine, and you won't want to change anything.  This just helps you to spot
unwanted repetition in your own writing.
