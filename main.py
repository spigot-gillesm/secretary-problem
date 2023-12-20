import math

from CandidateGenerator import CandidateGenerator
from CandidatePicker import CandidatePicker
from DataChart import DataChart


def main():
    values_of_alpha = [0.15, 0.25, 0.3, (1 / math.e), 0.4, 0.65]
    n = 1000
    attempts = 10_000
    generator = CandidateGenerator()
    chart = DataChart(n, attempts)

    for alpha in values_of_alpha:
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
    chart.plot()


if __name__ == "__main__":
    main()
