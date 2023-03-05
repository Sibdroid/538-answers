from decimal import Decimal as dec
def find_solutions(points: int) -> int:
    count = 0
    for x in range(1, points//2+1):
        x = dec(x)
        y = (dec(points)/dec(3)-dec(2)/dec(3)*x)
        if float(y).is_integer() and y != 0:
            count += 1
    return count
def main() -> None:
    print(find_solutions(61))
if __name__ == "__main__":
    main()

