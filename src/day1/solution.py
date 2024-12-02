from src.utils import read_input

def parse_input(puzzle_input):
    """Parse the puzzle input."""
    return puzzle_input

def part1(data):
    """Solve part 1 of the puzzle."""
    pass

def part2(data):
    """Solve part 2 of the puzzle."""
    pass

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    data = read_input(1)
    solutions = solve(data)
    print(f"Part 1: {solutions[0]}")
    print(f"Part 2: {solutions[1]}")