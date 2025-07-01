# spreadrank
# SpreadRank

Compute a SpreadRank score for a list of categorical items.  
Score ∈ [0, 1):  
- 0 means perfectly uniform distribution  
- Values approach 1 as one category dominates  

---

## Prerequisites

- Python 3.6 or higher  

---

## Installation

Clone the repository and (optionally) set up a virtual environment:


git clone https://github.com/yourusername/spreadrank.git
cd spreadrank

# optional: create venv
python3 -m venv venv
source venv/bin/activate

# no external dependencies required


---

## Usage

Run `main.py` in one of four modes:

1. **List mode**  
   Pass items directly as space-separated arguments:  
   
   python main.py --list a a b b c
 

2. **File mode**  
   Read one item per line from a text file:  
   
   python main.py --file items.txt
   

3. **STDIN mode**  
   Pipe items (one per line) via standard input:  
   
   cat items.txt | python main.py --stdin


4. **Interactive mode**  
   Run without flags and enter items when prompted:  
   
   python main.py
   # Enter items separated by spaces: a a b c
   

---

## Command-Line Arguments

- `-l, --list`  
  Items specified inline, e.g. `-l red red blue green red`  

- `-f, --file`  
  Path to a text file with one item per line  

- `-s, --stdin`  
  Read items from standard input (one per line)  

---

## Examples


# 1) Inline list
python main.py --list apple apple banana cherry

# 2) From file
python main.py --file items.txt

# 3) Via STDIN
cat items.txt | python main.py --stdin

# 4) Interactive prompt
python main.py
Enter items separated by spaces: x x y z z z


Each command prints:


SpreadRank score: 0.XXXXXX


---

## Project Structure

- src/       – Contains `spread_rank`, argument parsing, and interactive fallback  
- README.md     – This documentation  

