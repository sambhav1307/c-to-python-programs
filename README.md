# C to Python Programs

Three classic C programs (factorial, Fibonacci and struct-based student records) converted to Python using AI assistance.

## Programs

| File | Description |
|------|-------------|
| `factorial.py` | Reads a number and prints its factorial |
| `fibonacci.py` | Prints the first N terms of the Fibonacci series |
| `student_records.py` | Reads 3 students (roll, name, marks) and prints them as a table |

## Requirements

Python 3.7 or newer. No external packages needed.

## How to Run

```bash
git clone https://github.com/sambhav1307/c-to-python-programs.git
cd c-to-python-programs
python3 factorial.py
python3 fibonacci.py
python3 student_records.py
```

## Sample Output

**factorial.py**
```
Enter a number: 5
Factorial of 5 = 120
```

**fibonacci.py**
```
Enter number of terms: 7
0 1 1 2 3 5 8
```

**student_records.py**
```
Enter roll, name and marks: 1 Aman 87.5
Enter roll, name and marks: 2 Priya 92
Enter roll, name and marks: 3 Rohit 78.25

Roll	Name	Marks
1	Aman	87.50
2	Priya	92.00
3	Rohit	78.25
```

## C vs Python Note

- No type declarations: Python infers types.
- Integers have no size limit, so `25!` is correct (C's `long long` overflows after `20!`).
- `for` loops use `range()`; swapping uses `a, b = b, a + b`.
- `struct` becomes a `@dataclass`, and fixed arrays become lists.

## Author

Sambhav Jain
