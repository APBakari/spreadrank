from collections import Counter
from typing import List, Hashable

def spread_rank(items: List[Hashable]) -> float:
    """
    Compute the SpreadRank score for a list of categorical items.
    Score ∈ [0, 1):  0 == perfectly uniform, →1 as one category dominates.
    """
    n = len(items)
    if n == 0:
        return 0.0

    freqs = list(Counter(items).values())
    k = len(freqs)
    # If there's only one (or zero) unique category, no drop
    if k <= 1:
        return 0.0

    # sort frequencies desc
    freqs.sort(reverse=True)

    # compute relative drops between adjacent frequencies
    drops = [
        (f_i - f_j) / f_i
        for f_i, f_j in zip(freqs[:-1], freqs[1:])
        if f_i > 0
    ]

    # average drop
    return sum(drops) / len(drops)


if __name__ == "__main__":
    # quick sanity checks
    tests = [
        ([], 0.0, "empty list"),
        (["a"], 0.0, "single category"),
        (["a","b","c","d"], 0.0, "uniform four"),
        # only one adjacent drop: (3-1)/3 == 0.6667
        (["a","a","a","b"], (3-1)/3, "3:1 split"),
        (["x"]*100 + ["y"]*1, (100-1)/100, "extreme dominance"),
    ]

    for data, expected, desc in tests:
        score = spread_rank(data)
        print(f"{desc:15} → score={score:.4f}  (expected≈{expected:.4f})")
