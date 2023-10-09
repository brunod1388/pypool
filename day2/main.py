import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = pd.read_csv("life_expectancy_years.csv", index_col='country')
    print("the shape of data is:", data.shape)
    print(data.T["France"])
    plt.plot(data.T["France"])
    plt.show()