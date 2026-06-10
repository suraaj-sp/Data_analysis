import pandas as pd


def main():
    df = pd.read_csv("data/car-sales.csv")
    print("Dataset loaded: {} rows, {} columns".format(df.shape[0], df.shape[1]))
    print(df.head())


if __name__ == "__main__":
    main()
