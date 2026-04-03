#!/usr/bin/env python3

"""
Player Score Analytics
Processes game scores from the command line and prints basic statistics.
"""

import sys


print("=== Player Score Analytics ===")

scores = []

for value in sys.argv[1:]:
    try:
        scores = scores + [int(value)]
    except ValueError:
        print(f"Invalid parameter: '{value}'")

if len(scores) == 0:
    print("No scores provided. Usage: "
          "python3 ft_score_analytics.py <score1> <score2> ...")
else:
    total_score = sum(scores)
    average_score = total_score / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", total_score)
    print("Average score:", average_score)
    print("High score:", high_score)
    print("Low score:", low_score)
    print("Score range:", score_range)
