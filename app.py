from pprint import pprint
from typing import DefaultDict


def run() -> None:
    with open("f8ab32f7-44c7-43ca-98bf-c1b444724598.csv", "r") as f:
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
