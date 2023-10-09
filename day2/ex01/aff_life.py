import matplotlib.pyplot as plt
import load_csv


def callback_left_button(event):
    ''' this function gets called if we hit the left button'''
    print('Left button pressed')


def callback_right_button(event):
    ''' this function gets called if we hit the left button'''
    print('Right button pressed')


def plot_country(country, dataset):
    '''
    this function plots the life expectancy of a country
    '''
    dataset = dataset.T
    plt.style.use('ggplot')
    dataset[country].plot()
    # plt.plot(dataset.index, dataset[country])
    plt.title(country + " Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life  expectancy (years)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    dataset = load_csv.load("../life_expectancy_years.csv", "country")
    if dataset is None:
        exit(1)
    plot_country("France", dataset)
