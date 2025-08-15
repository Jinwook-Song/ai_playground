from crewai.tools import tool


@tool
def count_letters(sentence: str) -> int:
    """
    Count the number of letters in the sentence
    """
    return len(sentence)
