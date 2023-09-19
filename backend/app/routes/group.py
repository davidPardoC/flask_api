from flask import Blueprint, jsonify
from app.models.group import Group, GroupSchema
from app.database import db
from sqlalchemy import select


groups_bp = Blueprint("groups", __name__, url_prefix="/groups")
group_schema = GroupSchema()


@groups_bp.route("", methods=["GET"])
def get_all_groups():
    groups = db.session.scalars(select(Group)).all()
    return jsonify(group_schema.dump(groups, many=True))
