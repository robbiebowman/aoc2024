from pathlib import Path

def read_input(day: int) -> list[str]:
    """
    Read the input.txt file for the specified day and return its contents split by lines.
    
    Args:
        day (int): The day number (1-25)
        
    Returns:
        list[str]: The contents of the input file split by lines
    """
    day_folder = Path(__file__).parent / f"day{day}"
    return (day_folder / "input.txt").read_text().strip().split("\n") 

def read_test_input(day: int) -> list[str]:
    """
    Read the test.txt file for the specified day and return its contents split by lines.
    
    Args:
        day (int): The day number (1-25)
        
    Returns:
        list[str]: The contents of the input file split by lines
    """
    day_folder = Path(__file__).parent / f"day{day}"
    return (day_folder / "test.txt").read_text().strip().split("\n") 