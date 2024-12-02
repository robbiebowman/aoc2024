from src.utils import read_input


def part1(first_location_codes, second_location_codes):
    return sum(
        abs(x - y)
        for x, y in zip(sorted(first_location_codes), sorted(second_location_codes))
    )


def part2(first_location_codes, second_location_codes):
    sorted_first = sorted(first_location_codes)
    sorted_second = sorted(second_location_codes)
    return sum(sorted_second.count(value) * value for value in sorted_first)


def solve(first_location_codes, second_location_codes):
    return part1(first_location_codes, second_location_codes), part2(
        first_location_codes, second_location_codes
    )


if __name__ == "__main__":
    data = [line.split() for line in read_input(1)]
    first_location_codes = [int(x[0]) for x in data]
    second_location_codes = [int(x[1]) for x in data]
    solution1, solution2 = solve(first_location_codes, second_location_codes)
    print(f"Part 1: {solution1}") # 1110981
    print(f"Part 2: {solution2}") # 24869388
