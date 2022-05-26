# Picks a petr and plenty of modular functionality
# because I can

from random import choices
import csv

def read_petrs(petr_file) -> dict:

    with open(petr_file, "r") as pfile:
        petr_reader = csv.reader(pfile)
        dict_petrs = {row[0]:float(row[1]) for row in petr_reader}

    return dict_petrs

def pick_a_petr(petr_dict:dict) -> str:

    return choices(list(petr_dict.keys()), 
                   list(petr_dict.values()))[0]

def read_n_pick_petr(petr_csv = "petrs.csv") -> str:

    return pick_a_petr(read_petrs(petr_csv))

def build_and_grab(path = "./") -> str:
# Can alternatively rebuild but where's the fun in that?
# Also if this blossoms, I/O may be faster ;)
    from build_petrs import determine_weights, grab_petrs

    part_1 = determine_weights(grab_petrs(path))
    return pick_a_petr(part_1)

if __name__ == "__main__":

    print("Testing `pick_a_petr` and `read_petrs`...") 
    print(read_n_pick_petr())
    print()
    print("Testing `build_and_grab`...")
    print(build_and_grab())
