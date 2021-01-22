import os
from pprint import pprint
from typing import DefaultDict
import urllib.request

FILE_NAME = "dog_license_data.csv"

def download_data() -> None:
    if os.path.exists(FILE_NAME):
        print(f"Found data file {FILE_NAME}")
    else:
        print(f"Data file not found. Downloading...")
        urllib.request.urlretrieve(
            "https://data.wprdc.org/dataset/ad5bd3d6-1b53-4ed0-8cd9-157a985bd0bd/resource/f8ab32f7-44c7-43ca-98bf-c1b444724598/download/2099.csv",
            FILE_NAME,
        )
        print(f"Downloaded data file {FILE_NAME}")


def run() -> None:
    download_data()

    with open(FILE_NAME, "r") as f:
        headers = f.readline().split(",")
        print(headers)
        data = {header: DefaultDict(int) for header in headers}
        counter = 0
        while row:=f.readline():
            for i, value in enumerate(row.split(",")):
                column_name = headers[i]
                data[column_name][value] += 1
            counter += 1
            if counter % 1000 == 0:
                print(".", end="")
    pprint(sorted(data["LicenseType"].items(), key=lambda x: x[1], reverse=True))
    pprint(sorted(data["Breed"].items(), key=lambda x: x[1], reverse=True)[:10])

if __name__ == "__main__":
    run()
