#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Python-Quiz (https://github.com/KafetzisThomas/Quiz-Games)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

from Question import Question

question_prompts = [
    "\nWhich one is NOT a legal variable name?\n\n(a) my_var\n(b) my-var\n(c) _myvar\n(d) Myvar\n\n",
    "\nWhat is a correct syntax to return the first character in a string?\n\n(a) x = sub(\"Hello, 0,1\")\n(b) x = \"Hello\".sub(0, 1)\n(c) x = \"Hello\"[0]\n\n",
    "\nWhich method can be used to remove any whitespace from both the beginning and the end of a string?\n\n(a) ptrim()\n(b) strip()\n(c) len()\n(d) trim()\n\n",
    "\nWhich collection does not allow duplicate members?\n\n(a) TUPLE\n(b) SET\n(c) LIST\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b")
]

def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)}")

run(questions)