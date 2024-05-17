def split_filename(filenames: list):
    prefix = ''.join([char for char in filenames[0] if not char.isdigit()])
    suffix_list = []
    for filename in filenames:
        suffix_list.append(int(''.join([digit for digit in filename if digit.isdigit()])))
    return prefix, sorted(suffix_list)
print(split_filename(["day1","day11", "day2"]))

def sorted_filenames(filenames: list):
    prefix, suffix_list = split_filename(filenames)
    return [prefix + str(suffix) for suffix in suffix_list]

print(sorted_filenames(["day1","day11", "day44", "day6", "day101", "day2"]))         