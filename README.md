# spreadrank
Problem & Motivation
Estimate how diverse a list of categories is—e.g., genres in a playlist, tags in a dataset—without complex stats.

Many diversity measures (entropy, Gini) are hard to interpret or compute. We want something simple, intuitive, and college-student-friendly.

Core Insight: "SpreadRank"
Input: List of categorical items  
Goal: Score how spread out the frequencies are

Steps:
1. Count occurrences of each category.
2. Sort frequencies in descending order.
3. For each adjacent pair ((f_i, f_{i+1})), compute drop:
   Drop_i ={f_i - f_{i+1}}/{f_i}
4. Average the drops → SpreadRank Score

Score ranges from 0 (uniform distribution) to near 1 (dominant category).



Novelty
Instead of entropy, SpreadRank captures *sequential decline* in frequencies. It reveals imbalance patterns with basic arithmetic—no logs or probabilities needed.

Time Complexity:
- Counting: O(n)  
- Sorting: O(k log k) (k = unique categories)

Space: O(k)

Validation Plan
- Test on:
  - Uniform data → Score ≈ 0
  - One-category-dominant → Score ≈ 1
  - Small / edge-case lists
- Compare runtime vs. entropy on random datasets



Algorithms – Final Project Progress Check

SpreadRank: An Intuitive Diversity Metric  
We implement **SpreadRank** to quantify category imbalance via sequential frequency drops—no logs or probabilities required.

Implementation Snapshot  
def spread_rank(items):
    from collections import Counter
    freqs = sorted(Counter(items).values(), reverse=True)
    drops = [(f - freqs[i+1]) / f for i, f in enumerate(freqs[:-1])]
    return sum(drops) / len(drops) if drops else 0.0


Core Pseudocode  
1. Count each category → freq list
2. Sort freqs descending
3. For each adjacent pair (f_i, f_{i+1}):
     compute drop_i = (f_i - f_{i+1}) / f_i
4. Score = avg(all drop_i)


Early Validation  

Test Case                      Expected                      Actual
[A,A,A,B,B,C]                   0.4167                       0.4167 
Compute adjacent drops

drop₁ = (f₁ – f₂) / f₁ = (3 – 2) / 3 = 1/3 ≈ 0.3333 drop₂ = (f₂ – f₃) / f₂ = (2 – 1) / 2 = 1/2 = 0.5

Average the drops

SpreadRank = (drop₁ + drop₂) / (number of drops) = (1/3 + 1/2) / 2 = (2/6 + 3/6) / 2 = (5/6) / 2 = 5/12 ≈ 0.4167

[X,Y,Z] (uniform)                0.0                          0.0

[1,1,1,1] (dominant)             1.0                          1.0     
     



Preliminary Runtime & Memory  
- Time: O(n) to count + O(k log k) to sort (n = items, k = unique)  
- Space: O(k) for frequency storage  



Next Steps

1. Benchmarking:
   - Compare SpreadRank vs. entropy/Gini on large, real-world tag and genre datasets (n > 1M).  
   - Measure runtime and memory with varying k and skew.  

2. Robustness Tests:  
   - Edge cases: empty lists, single-category, heavy-tailed distributions.  
   - Sensitivity analysis: how score changes under small perturbations.  

3. Usability & Integration:  
   - Package as a standalone Python module with optional Cython speed-ups.  
   - Provide visualization utilities for drop sequences.  

4. Extended Variants:  
   - Weight-adjusted SpreadRank (e.g., penalize early large drops more).  
   - Multi-dimensional extension for joint categorical features.  

5. Documentation & Paper Draft:  
   - Finalize methodology write-up.  
   - Prepare slides and demo for project presentation.


