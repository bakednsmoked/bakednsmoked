"""Stock blueprint"""

from flask import Blueprint, jsonify, request

stock_bp = Blueprint("stock_bp", __name__)


@stock_bp.route("/stock", methods=["GET", "POST"])
def stock():
    """Stock endpoint"""

    if request.method == "GET":
        return jsonify("Hello")
    else:
        return jsonify("Invalid request")
