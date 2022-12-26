##############################
# Advent of Code 2022
# Day 25, part a and b of puzzle
# Matthias, 2022-12-26
# Balanced quinary numeral system
# https://en.wikipedia.org/wiki/Balanced_ternary
# https://www.youtube.com/watch?v=DLfO_6sTvjo
##############################

def parse():
    with open("input.txt") as f:
        contents = f.read()
    contents.strip()
    return contents.split("\n")

snafu_dict = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-"}
snafu_dict_reverse = {"0": 0, "1": 1, "2": 2, "=": -2, "-": -1}

def snafu_2_dect(snafu):
    value = 0
    result = 0
    for s in snafu[::-1]:
        number = snafu_dict_reverse[s]
        result += number * 5**value
        value+=1
    return result

def dec_2_snafu(dec):
    snafu = ""
    while(dec > 0):
        remainder = dec % 5
        if remainder >2:
            dec += 5 - remainder
        snafu = snafu_dict[remainder]  + snafu
        dec = dec // 5
    return snafu

sum = 0
snafus = parse()
for snafu in snafus:
    sum += snafu_2_dect(snafu.strip())

print(dec_2_snafu(sum))