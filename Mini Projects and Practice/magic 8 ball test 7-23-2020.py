#Magic 8 Ball Test

import random

answers = [
    "Absolutely",
    "Definitely not",
    "Maybe",
    "Ask again later",
    "Probably",
    "Yes",
    "No"
    ]

question = input("Ask me a question: \n>")

#note: len(answers)-1 is used to account for index values starting at 0
print(answers[random.randint(0,len(answers) - 1)])

#note: tuples are indicated like lists but using parentheses instead of square brackets

