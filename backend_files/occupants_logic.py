from data import rooms

# Here is a method signature to get you started.


def check_occupants(room_number, date):
    if rooms.get(room_number):
        room = rooms[room_number]
        for occupant in room["occupants"]:
            if occupant["check_in"] <= date and occupant["check_out"] >= date:
                return room
    else:
        return []
