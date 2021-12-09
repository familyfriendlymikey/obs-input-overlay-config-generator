import sys
from keycodes import keycodes
from config import width, height, gap, keys, key_order

def get_left_mapping(key):
    return 1 + ((width + 3) * key_order.index(key))

def main():
    max_width = len(max(keys, key=len))
    max_height = len(keys)

    data = {}
    data["overlay_width"] = ((width + gap) * (max_width - 1)) + width
    data["overlay_height"] = ((height + gap) * (max_height - 1)) + height

    top = 1
    left = 1
    xpos = 0
    ypos = 0

    elements = []

    for row in keys:
        xpos = 0
        for key in row:
            if key != "":

                for i, item in enumerate(keycodes):
                    if item["key"] == key:
                        break
                else:
                    continue

                obj = dict()

                obj["mapping"] = [get_left_mapping(key), top, width, height]
                obj["pos"] = [xpos, ypos]
                obj["id"] = key
                obj["type"] = keycodes[i]["type"]
                obj["code"] = keycodes[i]["code"]

                elements.append(obj)

            left += width + 3
            xpos += width + gap
        ypos += height + gap

    data["elements"] = elements

    from datetime import datetime
    dt = datetime.now().strftime("%m-%d-%y_%H-%M-%S")
    with open("input_overlay_config_" + dt + ".json", "w") as outfile:
        import json
        json.dump(data, outfile, indent=4, sort_keys=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].strip() == "-p":
            print("WIDTH:", (width + 3) * len(key_order) -1)
            print("HEIGHT:", (height * 2) + 5)
    else:
        main()
