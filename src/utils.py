import os
import pickle
import yaml

def load_config(config_path):

    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config