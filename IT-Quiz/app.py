#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: IT-Quiz (https://github.com/KafetzisThomas/Quiz-Games)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

from Question import Question

question_prompts = [
    "\nWhat HTTP stands for?\n\n(a) Hypotext Transmission Protocol\n(b) Hyperlink Template Troubleshooting Processor\n(c) Hypertext Transfer Protocol\n(d) I don't know\n\n",
    "\nWhat is kernel in a computer?\n\n(a) The core that provides basic services for all other parts of the OS\n(b) The entire Os\n(c) A process\n(d) I don't know\n\n",
    "\nWhat is lambda in Python?\n\n(a) A function having no name\n(b) A typical function\n(c) A for loop\n(d) I don't know\n\n",
    "\nWhat is TLS?\n\n(a) Transfer Layer Security\n(b) Transport Layer Security\n(c) Traditional Layer Security\n(d) I don't know\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b")
]

def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"\nYou got {score}/{len(questions)}")

run(questions)