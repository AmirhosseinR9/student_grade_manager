
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    @property
    def average(self):
        return round(sum(self.scores) / len(self.scores), 2)

    def to_dict(self):
        return {
            "name": self.name,
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["scores"])
    
    def add_score(self, score: float):

        self.scores.append(score)

    def remove_score(self, index: int):
        
        self.scores.pop(index)

    def print_scores(self):

        if not self.scores:
            print("No scores available.")
            return
        
        for i, score in enumerate(self.scores, start=1):
            print(f"{i}) {score}")
