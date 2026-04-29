"""
Filename: export_data.py
Purpose: Exports data of the simulation simulate.py to a .csv file with SCADA data tags.
Author: Cameron L. Nolen
Created: 2026-01-07
"""


import pandas as pd


def export_to_csv (time: float, tags: float, filename: str):
    data: dict(str, float) = {"time_s" : time}
    for (key, value) in tags.items():
        data[key] = value
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index = False)
