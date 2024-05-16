def switch_door(door_no: int, doors: list) -> bool:
    return True if doors[door_no] == False else False
def switch_door_condition(factor: int, doors: list) -> "list[bool]":
    for door_no in range(1, len(doors)+1, factor):
        doors[door_no] = switch_door
    return doors
def open_doors(limit: int) -> list:
    doors = [True] * limit
    for i in range(1, limit+1):
        doors = switch_door_condition(i, doors)
    return [door_no for door_no in range(1, limit+1) if doors[door_no] == True]

print(open_doors(100))