import sys, time
from pypandas.datasets import *
from pypandas.scale import *
from pypandas.preprocess import *

columns = ["Job #", "Doc #", "Bin #", "Initial Cost", "Total Est Fee", "Existing Zoning Sqft", "Proposed Zoning Sqft", "Enlargement SQ Footage", "Street Frontage", "ExistingNo of Stories", "Proposed No of Stories", "Existing Height", "Proposed Height"]

def drop_na(df, cols):
    for col in cols:
        df = drop_null(df, col)
    return df

def test_standard_scale():
    starttime = time.time()
    df = load_data_job("aws")
    df = drop_na(df, columns)
    df = standard_scale(df, columns)
    df.count()
    print("The standard_scale() takes: " + str(time.time() - starttime) + " sec.")

def test_min_max_scale():
    starttime = time.time()
    df = load_data_job("aws")
    df = drop_na(df, columns)
    df = min_max_scale(df, columns)
    df.count()
    print("The min_max_scale() takes: " + str(time.time() - starttime) + " sec.")

def test_max_abs_scale():
    starttime = time.time()
    df = load_data_job("aws")
    df = drop_na(df, columns)
    df = max_abs_scale(df, columns)
    df.count()
    print("The max_abs_scale() takes: " + str(time.time() - starttime) + " sec.")

def test_normalize():
    starttime = time.time()
    df = load_data_job("aws")
    df = drop_na(df, columns)
    df = normalize(df, columns)
    df.count()
    print("The normalize() takes: " + str(time.time() - starttime) + " sec.")


def main():
    func = sys.argv[1]
    if func == "standard_scale":
        test_standard_scale()
    elif func == "min_max_scale":
        test_min_max_scale()
    elif func == "max_abs_scale":
        test_max_abs_scale()
    elif func == "normalize":
        test_normalize()
    else:
        raise ValueError("Invalid argument.")

if __name__ == "__main__":
    main()
