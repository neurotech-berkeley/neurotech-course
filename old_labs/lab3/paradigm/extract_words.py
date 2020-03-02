import pandas as pd
import numpy as np

def get_words():
    words = pd.read_csv("word_list.csv")
    n = len(words)

    words_big = np.random.choice(words["id"],size=60, replace=False)
    words_small = np.random.choice(words_big,size=30, replace=False)

    final = words[words["id"].isin(words_big)].copy()
    final["is_shown"] = 0

    ids = list(final["id"])
    is_shown = list(final["is_shown"])

    for x in range(0,len(ids)):
        if ids[x] in words_small:
            is_shown[x] = 1

    final["is_shown"] = is_shown


    ix = np.arange(final.shape[0])
    np.random.shuffle(ix)
    final = final.reset_index().ix[ix]
    final = final.reset_index()

    return final
