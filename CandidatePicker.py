from typing import List

import Candidate


class CandidatePicker:

    __m: int

    def __init__(self, m: int):
        self.__m = m

    def pick(self, candidates: List[Candidate.Candidate]) -> Candidate:
        if self.__m >= len(candidates):
            raise ValueError("There must be more candidates than the value of m")

        current_best = -1

        for i in range(self.__m):
            current_candidate_score = candidates[i].get_score()

            if current_candidate_score > current_best:
                current_best = current_candidate_score

        for i in range(self.__m, len(candidates)):
            current_candidate = candidates[i]

            if current_candidate.get_score() > current_best:
                return current_candidate

        return Candidate.null_candidate
