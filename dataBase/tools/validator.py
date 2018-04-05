import glob
import json

directory = "../SubDistricts/New"
toCheck = glob.glob1(directory, "*.json")

def json_check(myJSON):
    try:
        json_obj = json.loads(myJSON)
    except ValueError:
        return False
    return True

print()
for i in toCheck:
    print(i + " " + str(json_check(i)))
