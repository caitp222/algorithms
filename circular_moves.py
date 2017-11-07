# http://www.techiedelight.com/check-given-set-moves-circular-not/
# check if a given set of moves is circular or not

def is_circular(str):
    possible_directions = ["north", "east", "south", "west"]
    current_direction = "north"
    co_ords = { "x": 0, "y": 0 }
    for char in str:
        if char == "M":
            if current_direction == "north":
                co_ords["y"] += 1
            elif current_direction == "east":
                co_ords["x"] += 1
            elif current_direction == "south":
                co_ords["y"] -= 1
            elif current_direction == "west":
                co_ords["x"] -= 1
        elif char == "R":
            current_direction = possible_directions[possible_directions.index(current_direction) + 1]
        elif char == "L":
            current_direction = possible_directions[possible_directions.index(current_direction) - 1]
    return co_ords == { "x": 0, "y": 0 }


# both should return true:
print is_circular("MRMRMRM")
print is_circular("MRMLMRMRMMRMM")
