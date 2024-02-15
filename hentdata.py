import requests
import os
import gzip
import shutil
import pandas as pd

data = [
    "StormEvents_details-ftp_v1.0_d1950_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1951_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1952_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1953_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1954_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1955_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1956_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1957_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1958_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1959_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1960_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1961_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1962_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1963_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1964_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1965_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1966_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1967_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1968_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1969_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1970_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1971_c20210803.csv.gz",
    "StormEvents_details-ftp_v1.0_d1972_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1973_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1974_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1975_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1976_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1977_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1978_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1979_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1980_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1981_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1982_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1983_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1984_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1985_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1986_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1987_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1988_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1989_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1990_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1991_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1992_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1993_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1994_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1995_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1996_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1997_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1998_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d1999_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2000_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2001_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2002_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2003_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2004_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2005_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2006_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2007_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2008_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2009_c20231116.csv.gz",
    "StormEvents_details-ftp_v1.0_d2010_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2011_c20230417.csv.gz",
    "StormEvents_details-ftp_v1.0_d2012_c20221216.csv.gz",
    "StormEvents_details-ftp_v1.0_d2013_c20230118.csv.gz",
    "StormEvents_details-ftp_v1.0_d2014_c20231116.csv.gz",
    "StormEvents_details-ftp_v1.0_d2015_c20220425.csv.gz",
    "StormEvents_details-ftp_v1.0_d2016_c20220719.csv.gz",
    "StormEvents_details-ftp_v1.0_d2017_c20230317.csv.gz",
    "StormEvents_details-ftp_v1.0_d2018_c20230616.csv.gz",
    "StormEvents_details-ftp_v1.0_d2019_c20240117.csv.gz",
    "StormEvents_details-ftp_v1.0_d2020_c20231217.csv.gz",
    "StormEvents_details-ftp_v1.0_d2021_c20231217.csv.gz",
    "StormEvents_details-ftp_v1.0_d2022_c20231217.csv.gz",
    "StormEvents_details-ftp_v1.0_d2023_c20240117.csv.gz",
]


def hent():
    url = "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
    for i, filNavn in enumerate(data):
        a = requests.get(url + filNavn)
        with open(os.path.join("./ekstremvær", filNavn), "wb") as fil:
            fil.write(a.content)

        print(round((i / len(data)) * 100), a.status_code)


def pakkUt():
    filer = [os.path.join("./ekstremvær", a)
             for a in os.listdir("./ekstremvær")]
    for i, filNavn in enumerate(filer):
        with gzip.open(filNavn, "rb") as filInn:
            with open(filNavn.removesuffix(".gz"), "wb") as filUt:
                shutil.copyfileobj(filInn, filUt)

        print(round((i / len(filer)) * 100), filNavn)


def tilExcel():
    filer = [os.path.join("./ekstremvær", a)
             for a in os.listdir("./ekstremvær")]
    for i, filnavn in enumerate(filer):
        df = pd.read_csv(filnavn, low_memory=False)
        try:
            df.to_excel(filnavn.removesuffix(".csv")+".xlsx")
        except:
            print(f"hoppet over {filnavn}")

        print(round((i / len(filer)*100)))


if __name__ == "__main__":
    tilExcel()
