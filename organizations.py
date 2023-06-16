from flask import Flask, request, jsonify
import marshmallow as ma
from users import OrganizationSchema
from organizations import Organizations, Organizations_Schema, Organization_Schema
# import uuid
# from sqlalchemy.dialects.postgresql import UUID

from db import db #this is the database name = Alchemy

class Organizations(db.Model):
    __tablename__ = "Organizations"

    org_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False, unique=True)
    city = db.Column(db.String())
    state = db.Column(db.String())
    phone = db.Column(db.String())
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, name, city, state, phone, active):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.active = active


users = db.relationship("Users", backref="organization",lazy=True)


@app.route("/orgs/get", methods=['GET'])
def get_all_orgs():
    orgs = db.session.query(OrganizationsSchema).all()
    if not orgs:
        return jsonify("There are no Orgs"), 404
    else:
        return jsonify(organizations_schema.dump(orgs)), 200


@app.route("/orgs/get/<id>", methods=['GET'])
def get_all_orgs_by_id():
    orgs = db.session.query(OrganizationsSchema).all()
    if not orgs:
        return jsonify("There are no Orgs"), 404
    else:
        return jsonify(organizations_schema.dump(orgs)), 200   


class OrganizationsSchema(ma.Schema):
    class Meta:
        fields = ['org_id', 'name', 'phone', 'city', 'state', 'active']
        users = ma.fields.Nested(UsersSchema())
 
organization_schema = OrganizationSchema()
organizations_schema = OrganizationsSchema(many=True) 

    # org_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Organizations.org_id"), nullable= False)

    

    