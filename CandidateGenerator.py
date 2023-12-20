import random
from typing import List
from Candidate import Candidate


class CandidateGenerator:

    def generate(self, n: int) -> List[Candidate]:
        candidates = []
        unordered_candidates = []

        for i in range(n):
            candidates.append(Candidate(i))

        for i in range(n):
            # n - i - 1 = the max index of the candidates list
            random_index = random.randint(0, n - i - 1)
            unordered_candidates.append(candidates.pop(random_index))

        return unordered_candidates
