from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_name, best_score = "", 0
    for score in scores:
        name, score = score[0], score[1]
        if score > best_score:
            best_name, best_score = name, score
    
    return best_name

        


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
