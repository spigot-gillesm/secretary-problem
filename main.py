import argparse
import math
from typing import List

from CandidateGenerator import CandidateGenerator
from CandidatePicker import CandidatePicker
from DataChart import DataChart


def main(n: int, attempts: int, alphas: List[float], output: str):
    generator = CandidateGenerator()
    chart = DataChart(n, attempts, output)

    for alpha in alphas:
        print("Alpha = " + str(alpha) + "...")
        m = int(n * alpha)
        candidate_picker = CandidatePicker(m)

        counter = attempts
        best_found = 0

        while counter > 0:
            candidates = generator.generate(n)
            best_candidate = candidate_picker.pick(candidates)

            if best_candidate.get_score() >= n-1:
                best_found += 1

            counter -= 1

            if counter % (attempts/20) == 0:
                print(str((attempts - counter) / attempts * 100) + "%")

        print("Algorithm found the best candidates in " + str(best_found) + " out of the " + str(attempts) + " attempts")
        chart.add_data(alpha=str(alpha), success_rate=(best_found / attempts))

    # Once all values were tested, save the chart
    print("Saving results to {}.".format(output))
    chart.plot()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Secretary Problem')
    parser.add_argument("-n", "--candidates", type=int, help="The number n of candidates.", default=1000)
    parser.add_argument("-a", "--alpha", nargs="+", type=str, help="The list of alpha values."
                                                                   " Must be a float or '1/e'"
                        , required=True)
    parser.add_argument("-o", "--output", type=str, default="output.png",
                        help="The destination file for the chart. Must have a valid image extension."
                             " Default to 'chart.png'")
    parser.add_argument("--attempts", type=int,
                        help="How many rounds the algorithm will be executed on each set of n candidates for each alpha."
                             " Increasing this value allows for more accurate results but increase the computation time.",
                        default=10_000)

    values = vars(parser.parse_args())
    alphas = []

    if len(values) == 0:
        print("Some arguments are mandatory. Use the -h or --help to get help.")
        exit(0)

    for value in values["alpha"]:
        if value == "1/e":
            alphas.append(1/math.e)
        else:
            alphas.append(float(value))

    main(values["candidates"], values["attempts"], alphas, values["output"])
