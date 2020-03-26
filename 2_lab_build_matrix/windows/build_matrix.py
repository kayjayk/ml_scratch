import numpy as np
import pandas as pd
import os


def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    source = np.array(list(enumerate(sorted(df["source"].unique()))))[:, 1].tolist()
    target = np.array(list(enumerate(sorted(df["target"].unique()))))[:, 1].tolist()
    df_rating = pd.DataFrame(np.zeros(len(source) * len(target)).reshape(len(source), len(target)),
                             columns=target, index=source)

    number = list(range(len(df)))
    df.index = number
    df["index"] = number

    def f(x):
        df_rating.loc[df.loc[x]["source"]][df.loc[x]["target"]] = df.loc[x]["rating"]

    df["index"].map(f)
    return df_rating.values


def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    source = np.array(list(enumerate(sorted(df["source"].unique()))))[:, 1].tolist()
    target = np.array(list(enumerate(sorted(df["target"].unique()))))[:, 1].tolist()
    df_freq = pd.DataFrame(np.zeros(len(source) * len(target)).reshape(len(source), len(target)),
                           columns=target, index=source)

    number = list(range(len(df)))
    df.index = number
    df["index"] = number

    def f(x):
        df_freq.loc[df.loc[x]["source"]][df.loc[x]["target"]] += 1

    df["index"].map(f)
    return df_freq.values