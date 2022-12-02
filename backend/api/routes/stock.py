"""Stock blueprint"""

from flask import Blueprint, jsonify

stock_bp = Blueprint("stock_bp", __name__)


@stock_bp.route("/stock")
def stock():
    
    return jsonify("Hello")
