import numpy as np


def main():
    arr = np.array([1, 2, 3, 4, 5])
    print("Array created: {}".format(arr))
    print("Mean: {}, Std: {}, Sum: {}".format(arr.mean(), arr.std(), arr.sum()))
    
    matrix = np.random.rand(3, 3)
    print("\nRandom 3x3 matrix:")
    print(matrix)


if __name__ == "__main__":
    main()
