from collections import defaultdict as ddict
def extract_data(data_file) -> str:
    with open(data_file) as f:
        data = f.read()
        return data

def generate_frequency(data: str) -> dict:
    no_of_occurance = {}
    for char in data:
        if char in no_of_occurance:
            no_of_occurance[char] += 1
        else:
            no_of_occurance[char] = 1
    return no_of_occurance

def percentage_data(data: str) -> dict:
    freq_data = generate_frequency(data)
    percentage_dat = {}
    for key in freq_data:
        percentage_dat[key] = freq_data[key] * len(data) / 100
    return percentage_dat

def display_freq():
    freq_analysis1 = percentage_data(extract_data("mono_ciph013.txt"))
    freq_analysis2 = percentage_data(extract_data("mono_ciph033.txt"))
    freq_analysis3 = percentage_data(extract_data("mono_ciph053.txt"))
    print("Character\tOccurance in file1\tOccurance in file2\tOccurance in file2")
    for key in freq_analysis1:
        print(key, "\t", freq_analysis1[key], "\t", freq_analysis2[key], "\t", freq_analysis3[key] )
  
display_freq()
    

