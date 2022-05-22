import numpy as np
import pandas as pd

from tensorflow.keras.layers import Dense, Activation, Dropout, Input, LSTM, Reshape, Lambda, RepeatVector
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

alphaDS = open("datasets/a/dataset.txt", "r", encoding="utf-8").read().split("\n\n")
betaDS = open("datasets/b/dataset.txt", "r", encoding="utf-8").read().split("\n\n")
vocab = sorted(set(open("datasets/vocab.txt", "r", encoding="utf-8").read()))

print(f'{len(vocab)} unique characters')



