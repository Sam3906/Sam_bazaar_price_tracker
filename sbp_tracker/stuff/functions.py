import subprocess
import json

def importdata(i, lang):
    p1 = lang["mpli"]
    try:
        outpt = eval(subprocess.check_output(f"curl https://sky.coflnet.com/api/bazaar/{i}/snapshot", shell=True))
    except:
        error_handler(0, lang)
    else:
        mpli = int(input(f"{p1}:\n"))
        if not type(mpli) is int or mpli <= 0:
            error_handler(1)
        else:
            obj = [i, outpt["buyPrice"], outpt["sellPrice"], mpli]
    return obj

def outputf(inpt, lang):
    p1 = lang["s_name"]
    p2 = lang["s_pri"]
    p3 = lang["s_sell"]
    p4 = lang["s_del"]
    p5 = lang["mpli"]

    i = 0
    for x in inpt:
        list = inpt[i]
        d = abs(list[1] - list[2])
        mprice = list[1] * list[3]
        msell = list[2] * list[3]
        print(f"{p1}: {list[0]}; {p2}: {list[1]}; {p3}: {list[2]}; {p4}: {d}; {p5}: {list[3]}x; {p2} x{list[3]}: {mprice}; {p3} x{list[3]}: {msell}\n")
        i = i + 1
    return 0

def langsel(lang):
    with open("stuff/Options.json", "r") as opt:
        data_opt = json.load(opt)
    i = input(lang["language_sel"])
    if i == "-it":
        with open("stuff/languages/it_IT.json") as it_IT:
            data = json.load(it_IT)
            data_opt["Language"] = "it_IT"
    elif i == "-en":
        with open("stuff/languages/en_EN.json") as en_EN:
            data = json.load(en_EN)
            data_opt["Language"] = "en_EN"
    with open("stuff/Options.json", "w") as opt:
        json.dump(data_opt, opt, indent=4)
    return data


def error_handler(i, lang):
    if i == 0:
        print(lang["err_1"])
    elif i == 1:
        print(lang["err_2"])
    elif i == 2:
        print(lang["err_3"])
    elif i == 3:
        print(lang["err_4"])
    return 0