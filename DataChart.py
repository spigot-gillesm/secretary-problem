from typing import Dict, List
import matplotlib.pyplot as plt


class DataChart:
    # Links the alpha value to the proportion of best result found for that m
    __data_pairs: Dict[str, float] = {}

    __n: int

    __attempts: int

    __output: str

    def __init__(self, n: int, attempts: int, output: str):
        self.__n = n
        self.__attempts = attempts
        self.__output = output

    def add_data(self, alpha: str, success_rate: float):
        self.__data_pairs[alpha] = success_rate

    def plot(self):
        # Get the alpha values used. Used to form the x-axis
        alpha_values = list(self.__data_pairs.keys())
        # Get the success rates. Used to form the y-axis
        success_rates = list(self.__data_pairs.values())
        figure, subplots = plt.subplots(figsize=(10, 7))

        # creating the bar plot
        bar_container = subplots.bar(alpha_values, success_rates, color='red',
                                     width=0.3)

        subplots.set_ylabel("Success Rate")
        subplots.set_xlabel("Alpha Value")
        subplots.set_title("Success rate of the algorithm for a given alpha on {} attempts on {} candidates each"
                           .format(self.__attempts, self.__n))

        for i, bar in enumerate(bar_container):
            height = bar.get_height()
            subplots.text(x=bar.get_x(), y=(height + 0.01), s=str(success_rates[i]))

        figure.savefig(self.__output)
        plt.close(figure)
