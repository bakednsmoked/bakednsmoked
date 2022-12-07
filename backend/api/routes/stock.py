"""Stock blueprint"""

import threading
from flask import Blueprint, jsonify, request
from ..websock import start_ws
stock_bp = Blueprint("stock_bp", __name__)

th = threading.Thread(target=start_ws)
th.start()

@stock_bp.route("/stock", methods=["GET", "POST"])
def stock():
    """Stock endpoint"""

    if request.method == "GET":
        return jsonify("Hello")
    else:
        return jsonify("Invalid request")
