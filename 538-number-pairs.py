import typing as t
from collections import Counter
def get_sequence(length: int, n: int=1) -> t.Generator[int, None, None]:
    """Yields numbers from (n, n+2, n+5, n+9...) sequence.

    Args:
        length (int): the length of the sequence.
        n (int): the starting value, defaults to 1.

    Yields:
        Consecutive numbers of the sequence.
    """
    yield n
    for i in range(2, length+1):
        n += i
        yield n

        
def find_most_common_pairs(length: int) -> t.Generator[int, None, None]:
    """Yields most common end pairs of numbers in (1, 3, 6, 10, 15) sequence.

    Args:
        length (int): the length of the sequence.

    Yields:
        Most common end pairs of numbers in the sequence.
    """
    pairs = []
    for number in get_sequence(length):
        number = str(number)
        if len(number) > 1:
            pairs += [number[-2:]]
    occurences = Counter(pairs)
    max_occurrence = max(occurences.values())
    for i, j in occurences.items():
        if j == max_occurrence:
            yield int(i)

            
def main() -> None:
    for i in find_most_common_pairs(100000):
        print(i)


if __name__ == "__main__":
    main()
                                
    
