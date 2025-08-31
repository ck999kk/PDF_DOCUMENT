# This script validates PDF filenames to ensure they follow a specific naming convention.
# The expected format is YYYYMMDD-Title-###.pdf.
#
# Input: A directory path (optional, defaults to current directory).
# Output: Prints invalid filenames and exits with an error code if any are found.

import os
import sys


def is_valid(filename):
    """
    Checks if a filename follows the YYYYMMDD-Title-###.pdf format.

    Args:
        filename: The name of the file to check.

    Returns:
        True if the filename is valid, False otherwise.
    """
    # expected format YYYYMMDD-Title-###.pdf
    if not filename.lower().endswith('.pdf'):
        return True
    name = filename[:-4]
    parts = name.split('-')
    if len(parts) < 3:
        return False
    date_part = parts[0]
    seq_part = parts[-1]
    if len(date_part) != 8 or not date_part.isdigit() or not seq_part.isdigit():
        return False
    return True


if __name__ == "__main__":
    """
    Main script to validate PDF filenames in a given directory.
    """
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'

    try:
        all_files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: Directory not found at '{directory}'")
        sys.exit(1)

    bad = [f for f in all_files if f.lower().endswith('.pdf') and not is_valid(f)]

    if bad:
        print('Invalid PDF filenames:')
        for b in bad:
            print(' -', b)
        sys.exit(1)

    print('All PDF filenames valid.')