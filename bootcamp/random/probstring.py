import random

def gen_string(length: int, prob_data: dict):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    weighted_chars = ""
    for char in characters:
        weighted_chars += char * 100 * prob_data[char]
    generated_string = ""
    for i in range(5):
        generated_string += random.choice(weighted_chars)
    return generated_string

print(gen_string(100, data_dict))


    

