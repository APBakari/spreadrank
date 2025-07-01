from collections import Counter       # import Counter to count occurrences of each item
from typing import List, Hashable    # import type hints for function signatures
import argparse                       # import argparse for command-line argument parsing
import sys                            # import sys for stdin reading and exiting

def spread_rank(items: List[Hashable]) -> float:  # define function taking a list of hashable items
    """
    Compute the SpreadRank score for a list of categorical items.
    Score ∈ [0, 1): 0 == perfectly uniform, →1 as one category dominates.
    """
    n = len(items)                   # total number of input items
    if n == 0:                       # handle empty list
        return 0.0                   # no items → score 0.0

    freqs = list(Counter(items).values())  # get list of counts per unique category
    k = len(freqs)                   # number of unique categories
    if k <= 1:                       # if only one (or zero) category
        return 0.0                   # perfectly uniform or no diversity

    freqs.sort(reverse=True)         # sort frequencies in descending order
    drops = [                         # compute relative drops between adjacent frequencies
        (f_i - f_j) / f_i            # drop fraction from f_i down to f_j
        for f_i, f_j in zip(freqs[:-1], freqs[1:])  # pair up adjacent counts
        if f_i > 0                   # guard against division by zero (f_i always > 0 here)
    ]
    return sum(drops) / len(drops)   # return the average drop

def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute SpreadRank for a list of categorical items."
    )
    group = parser.add_mutually_exclusive_group(required=False)  # allow only one input mode
    group.add_argument(
        "-l", "--list",
        nargs="+",                   # one or more items
        help="Items as space-separated list, e.g. -l a a b b c"
    )
    group.add_argument(
        "-f", "--file",
        type=argparse.FileType("r"), # file handle for reading
        help="Path to a text file (one item per line)"
    )
    group.add_argument(
        "-s", "--stdin",
        action="store_true",         # boolean flag for STDIN mode
        help="Read items (one per line) from STDIN"
    )
    return parser.parse_args()      # parse and return the arguments

def main():
    args = parse_args()             # get CLI arguments

    if args.list:                   # if list mode selected
        items = args.list           # use provided list of items
    elif args.file:                 # if file mode selected
        items = [
            line.strip()            # strip newline/whitespace
            for line in args.file
            if line.strip()         # skip empty lines
        ]
    elif args.stdin:                # if STDIN mode selected
        items = [
            line.strip()            # strip newline/whitespace
            for line in sys.stdin
            if line.strip()         # skip empty lines
        ]
    else:                           # fallback interactive prompt
        raw = input("Enter items separated by spaces: ").strip()  # prompt user
        if not raw:                 # no input given
            print("No items provided. Exiting.")
            sys.exit(1)             # exit with error code
        items = raw.split()         # split input into list

    score = spread_rank(items)      # compute the SpreadRank score
    print(f"SpreadRank score: {score:.6f}")  # display score with 6 decimal places

if __name__ == "__main__":        # if script is run directly
    main()                         # invoke main function
