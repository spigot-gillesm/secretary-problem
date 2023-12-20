class Candidate:

    __score: int

    def __init__(self, score: int):
        self.__score = score

    def get_score(self) -> int:
        return self.__score

    def __str__(self):
        return str(self.__score)
    
    
null_candidate = Candidate(-1)
