import os
import urllib.request
from datetime import datetime

import numpy as np
import pandas as pd


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


def generate_report(file_path: str, column_name: str) -> None:
    print(f"Loading source data {file_path}")
    df = pd.read_csv(file_path)

    print("Transforming data")
    column_name_year = "Year"
    df[column_name_year] = df.apply(
        lambda row: str(datetime.fromisoformat(row.ValidDate).year),
        axis=1,
    )
    license_type = df[[column_name, column_name_year]]
    license_type_counts = license_type.pivot_table(
        index=[column_name_year],
        columns=[column_name],
        aggfunc=np.count_nonzero,
        fill_value=0,
    )
    axis = license_type_counts.plot()

    report_path = f"{column_name}Plot.png"
    print(f"Saving {column_name} report to {report_path}")
    axis.figure.savefig(report_path)


def run() -> None:
    file_path = "dog_license_data.csv"
    download_data(file_path)

    generate_report(file_path, "LicenseType")


if __name__ == "__main__":
    run()
