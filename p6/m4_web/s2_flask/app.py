"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

Flask - A minimal RESTful web server
Run it as normal Python script: python <script>.py
 or on Flask CLI: flask --app <script> run
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

coders = {
    1: {"id": 1, "name": "Pete", "lang": "Python"},
    2: {"id": 2, "name": "Chip", "lang": "C++"},
}


@app.route("/")
def home():
    """Fake home page"""
    app.logger.debug("home()")

    return "<p>Welcome!</p>"


@app.route("/coders", methods=["GET"])
def read_coders():
    """Get all (non deleted) coders"""
    app.logger.debug("read_coders()")
    # returns only the active (non-None) coders
    return jsonify([v for v in coders.values() if v is not None])


@app.route("/coders/<int:id>", methods=["GET"])
def read_coder(id):
    """Get the coder with the specified id, or 404"""
    app.logger.debug("read_coder() on %d", id)

    if id in coders and coders[id] != None:
        return jsonify(coders[id])
    else:
        return jsonify({"error": f"Coder {id} not found"}), 404


@app.route("/coders", methods=["POST"])
def create_coder():
    """Create a coder from the passed JSON"""
    app.logger.debug("create_coder() on %s", request.json)

    id = len(coders) + 1
    # TODO: robustness, check what the user pass as a coder
    coder = request.json
    coder["id"] = id
    coders[id] = coder
    return jsonify(coder), 201


@app.route("/coders/<int:id>", methods=["PUT", "PATCH"])
def update_coder(id):
    """Manage both PUT and PATCH - just to show that it is possible"""
    app.logger.debug("update_coder() on %s", request.json)

    # no fallback to post in this implementation
    if id not in coders or coders[id] == None:
        return jsonify({"error": f"Coder {id} not found"}), 404

    coder = request.json
    # PUT requires all fields, PATCH here is OK even if nothing is passed in
    if request.method == "PUT":
        if not coder:
            return {"error": "No coder passed in"}, 400
        elif "name" not in coder or "lang" not in coder:
            return {"error": "Missing at least a required field"}, 400

    # TODO: robustness, check what the user pass
    coders[id].update(coder)

    return {"message": "Coder updated successfully", "coder": coders[id]}, 200


@app.route("/coders/<int:id>", methods=["DELETE"])
def delete_coder(id):
    """Delete the code with the passed id, if it still exists"""
    app.logger.debug("delete_coder() on %d", id)
    if id not in coders or coders[id] == None:
        return {"error": "Coder not found"}, 404

    coders[id] = None
    return {"message": "Coder deleted successfully"}, 200


if __name__ == "__main__":
    app.run(debug=True)
