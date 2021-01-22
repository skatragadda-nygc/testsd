from datetime import datetime
import os
from pprint import pprint
from typing import DefaultDict
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime


def download_data(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"Found data file {file_path}")
    else:
        print(f"Data file not found. Downloading...")
        urllib.request.urlretrieve(
            "https://data.wprdc.org/dataset/ad5bd3d6-1b53-4ed0-8cd9-157a985bd0bd/resource/f8ab32f7-44c7-43ca-98bf-c1b444724598/download/2099.csv",
            file_path,
        )
        print(f"Downloaded data file {file_path}")


def run() -> None:
    file_path = "dog_license_data.csv"
    download_data(file_path)

    dog_data = pd.read_csv(file_path)
    column_name_year = "Year"
    column_name_license = "LicenseType"
    dog_data[column_name_year] = dog_data.apply(
        lambda row: str(datetime.fromisoformat(row.ValidDate).year),
        axis=1,
    )
    license_type = dog_data[[column_name_license, column_name_year]]
    license_type_counts = license_type.pivot_table(
        index=[column_name_year],
        columns=[column_name_license],
        aggfunc=np.count_nonzero,
        fill_value=0,
    )
    axis = license_type_counts.plot()
    axis.figure.savefig("license_type_plot.png")


if __name__ == "__main__":
    run()
