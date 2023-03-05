from typing import List
from itertools import combinations
from math import prod


def check_pair(date1: List[int], date2: List[int]) -> bool:
    conditions = [sum(date1) in date2 and prod(date1) in date2,
                  sum(date2) in date1 and prod(date2) in date1]
    return any(conditions)


def main() -> None:
    day_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = [[[month+1, day+1] for day in range(day_length)] for
             month, day_length in enumerate(day_lengths)]
    dates = [date for month in dates for date in month]
    print(sum([check_pair(*pair) for pair in
               combinations(dates, 2)]))

    
if __name__ == "__main__":
    main()
