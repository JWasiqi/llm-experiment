# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 17:40:29 2025

@author: Wasuji
"""

with open("The_Verdict.txt", "r", encoding="utf-8") as f:raw_text = f.read()
print("Total number of characters:", len(raw_text))

import re

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)

vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
    