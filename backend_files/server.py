from flask import Flask, request, jsonify
from flask_cors import CORS
from data import rooms
from booking_logic import book_room
from occupants_logic import check_occupants
from availability_logic import check_room_availability

app = Flask(__name__)

CORS(app)

# GET api/rooms
@app.route("/api/rooms", methods=["GET"])
def get_rooms():
    return jsonify(rooms)


# Get api/rooms/<int:room_number>
@app.route("/api/rooms/<int:room_number>", methods=["GET"])
def get_room(room_number):
    room = rooms.get(room_number)
    if room:
        return jsonify(room)
    else:
        return jsonify({"error": "Room not found"}), 404


# Below are the routes that you need to implement. You can use the existing routes as a reference.
# These will not work until you implement the corresponding logic in the respective files.


# POST /api/book-room
@app.route("/api/book-room", methods=["POST"])
def book_room_route():
    data = request.json
    room_number = data.get("room_number")
    name = data.get("name")
    check_in = data.get("check_in")
    check_out = data.get("check_out")
    email = data.get("email")
    phone = data.get("phone")
    special_requests = data.get("special_requests")

    result = book_room(
        room_number, name, check_in, check_out, email, phone, special_requests
    )
    return jsonify(result)


# GET /api/check-occupants
@app.route("/api/check-occupants", methods=["GET"])
def check_occupants_route():
    room_number = int(request.args.get("room_number"))
    date = request.args.get("date")

    result = check_occupants(room_number, date)
    return jsonify(result)


# GET /api/check-availability
@app.route("/api/check-availability", methods=["GET"])
def check_availability_route():
    room_number = int(request.args.get("room_number"))
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))

    result = check_room_availability(room_number, month, year)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
