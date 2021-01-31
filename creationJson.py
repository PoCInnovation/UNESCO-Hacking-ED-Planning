import json

ROLL_NUMBER = 0
NOTE = 1
HYGIEN = 2
FOUR = 3
FIVE = 4
SIX = 5
SEVEN = 6

def fill_data_field(info, d):
    if info[HYGIEN]:
        d["data"]["hygien"] = info[HYGIEN]
    if info[FOUR]:
        d["data"]["four"] = info[FOUR]
    if info[FIVE]:
        d["data"]["five"] = info[FIVE]
    if info[SIX]:
        d["data"]["six"] = info[SIX]
    if info[SEVEN]:
        d["data"]["seven"] = info[SEVEN]
    return (d)

def remove_last_coma(f):
    f.seek(0, 2)
    f.seek(f.tell() - 2, 0)
    f.truncate()

def createJson(infos):
    f = open("data.json", "w")
    f.write("[")
    for info in infos:
        d = {
            "Roll_No": info[ROLL_NUMBER],
            "note": info[NOTE],
            "data":{},
        }
        d = fill_data_field(info, d)
        json.dump(d, f, indent=4)
        f.write(",\n")
    
    remove_last_coma(f)
    f.write("]")

if __name__ == '__main__':
    test = [[12, 12, 0, 0, 0, 0, 0],
            [5, 6, 0, 0, 0, 70, 0],
            [19, 5, 0, 2, 50, 0, 0]
            ]
    createJson(test)