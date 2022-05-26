# For rebuilding the petrs.csv file in case new petrs are added
import os
import numpy as np
import csv

def grab_petrs(path = "./") -> list:
    allowed = ["png", "jpeg", "jpg", "gif", "pdf"]
    petr_list = [i for i in os.listdir(path) 
                 if i.split('.')[-1].lower() in allowed]

    return petr_list

def determine_weights(petr_list:list) -> dict:
    # For rare petrs... no this doesn't pass stylecheck but ¯\_(ツ)_/¯
    basic = 1
    normal = 1/5
    rare = 1/20
    pretty_rare = 1/50
    very_rare = 1/100
    once_in_a_petr = 1/1000

    weighted_dict = {p:normal for p in petr_list}
    # Put custom weights here
    weighted_dict["friends_with_benefetr.jpeg"] = once_in_a_petr
    weighted_dict["friend_of_peter.jpeg"] = very_rare
    weighted_dict["pEt3RRRRr.jpeg"] = very_rare
    weighted_dict["know_your_petr.jpeg"] = very_rare
    weighted_dict["high_quality_petr.png"] = pretty_rare
    weighted_dict["my_neighbor_petr-o.png"] = rare
    weighted_dict["piano_petr.jpeg"] = rare
    weighted_dict["ghostd_petr.png"] = rare
    weighted_dict["petr.png"] = basic

    # I can't believe I have to do this... numpy!!!
    weights = np.array(list(weighted_dict.values()))
    normalized = weights/np.linalg.norm(weights)

    weighted_dict = {p:nv for p,nv in zip(weighted_dict.keys(), normalized)}
    
    return weighted_dict

if __name__ == "__main__":

    with open("petrs.csv", "w") as petr_file:
        petr_writer = csv.writer(petr_file)

        for p,w in determine_weights(grab_petrs()).items():
#            petr_writer.writerow(["petr","weight(lbs)"])
            petr_writer.writerow([p, w])

