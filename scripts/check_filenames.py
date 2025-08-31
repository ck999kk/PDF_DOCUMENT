import os
import sys

def is_valid(filename):
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

bad = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and not is_valid(f)]

if bad:
    print('Invalid PDF filenames:')
    for b in bad:
        print(' -', b)
    sys.exit(1)

print('All PDF filenames valid.')
