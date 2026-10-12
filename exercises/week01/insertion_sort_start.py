"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""


def insertion_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van insertion sort.

    Parameters:
        sequence (list): De lijst om te sorteren.

    Returns:
        list: De gesorteerde lijst.
    """
    if len(sequence) < 2:
        return sequence
    index = 1
    while index < len(sequence):
        temp_index = index
        while temp_index > 0 and sequence[temp_index] < sequence[temp_index - 1]:
            memory = sequence[temp_index -1]
            sequence[temp_index - 1] = sequence[temp_index]
            sequence[temp_index] = memory
            temp_index -= 1
        index += 1
    return sequence

if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:
    # import random
    # import time
    # ...