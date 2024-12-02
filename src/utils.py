from pathlib import Path

def read_input(day: int) -> list[str]:
    day_folder = Path(__file__).parent / f"day{day}"
    return (day_folder / "input.txt").read_text().strip().split("\n") 

def read_test_input(day: int) -> list[str]:
    day_folder = Path(__file__).parent / f"day{day}"
    return (day_folder / "test.txt").read_text().strip().split("\n") 