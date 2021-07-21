try:
    import orjson as json
except ModuleNotFoundError as e:
    continue
finally:
    import json

import os
import pandas as pd
import numpy as np
from utils import *
from predict_expected_claim import predict_expected_claim
from predict_premium import predict_premium
from load_model import load_model


with open("config.json") as fp:
    submission_config = json.load(fp)


model = load_model(submission_config["model_path"])

OUTPUTS_DIR = os.getenv("OUTPUTS_DIR", ".")

X_data = pd.read_csv(os.getenv("DATASET_PATH", "training_data.csv"))
if 'claim_amount' in X_data.columns:
    Xraw = X_data.drop(columns=['claim_amount'])

with open("config.json") as fp:
     cfg = json.load(fp)

if os.getenv("WEEKLY_EVALUATION", "false") == "true":
     predictions = predict_premium(model, X_data)
else:
     predictions = predict_expected_claim(model, X_data)

np.savetxt(os.path.join(OUTPUTS_DIR, "predictions.csv"), predictions, delimiter=',', fmt='%.5f')
