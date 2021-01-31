import json

ROLL_NUMBER = 0
NOTE = 1
PUPILS = 2
TEACHING = 3
SUPPORT = 4
LEADERSHIP = 5
SCHOOL = 6

def fill_data_field(info, d):
    if info[PUPILS]:
        d["data"]["pupils"] = info[PUPILS]
    if info[TEACHING]:
        d["data"]["teaching"] = info[TEACHING]
    if info[SUPPORT]:
        d["data"]["support"] = info[SUPPORT]
    if info[LEADERSHIP]:
        d["data"]["leadership"] = info[LEADERSHIP]
    if info[SCHOOL]:
        d["data"]["school"] = info[SCHOOL]
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