from fastapi import Depends
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

from config.secrets_parser import get_db, get_student_collection
from models.student_model import StudentModelUpdate, StudentModelUpdatePassword, StudentModelUpdateSocials, StudentModelUpdateCoding, StudentModelSignIn, StudentModelSignUp
from bson.json_util import dumps


def parse_student_object_id(student_id: str):
    try:
        return ObjectId(student_id)
    except InvalidId:
        return None


class StudentService:
    def __init__(self, db: MongoClient = Depends(get_db)):
        self.db = db
        self.student_collection = get_student_collection()

    def get_all_students(self):
        return dumps(list(self.student_collection.find({}, {"password": 0})))

    def get_student_by_id(self, student_id: str):
        object_id = parse_student_object_id(student_id)
        if object_id is None:
            return None
        return self.student_collection.find_one({"_id": object_id}, {"password": 0})

    def get_student_by_email(self, email: str):
        return self.student_collection.find_one({"email": email})

    def sign_up_student(self, student: StudentModelSignUp):
        result = self.student_collection.insert_one(student.model_dump())
        inserted_id = result.inserted_id
        return {"message": "Student registered successfully", "student_id": str(inserted_id)}

    def sign_in_student(self, student: StudentModelSignIn):
        return self.student_collection.find_one({"email": student.email, "password": student.password}, {"password": 0})

    def update_student(self, student_id: str, student: StudentModelUpdate):
        object_id = parse_student_object_id(student_id)
        if object_id is None:
            return None
        changes = student.model_dump(exclude_unset=True)
        if changes:
            self.student_collection.update_one({"_id": object_id}, {"$set": changes})
        return self.student_collection.find_one({"_id": object_id}, {"password": 0})

    def update_student_password(self, student_id: str, student: StudentModelUpdatePassword):
        object_id = parse_student_object_id(student_id)
        if object_id is None:
            return None
        result = self.student_collection.update_one({"_id": object_id}, {"$set": student.model_dump()})
        if result.matched_count == 0:
            return None
        return {"message": "Password updated successfully"}

    def update_student_socials(self, student_id: str, student: StudentModelUpdateSocials):
        object_id = parse_student_object_id(student_id)
        if object_id is None:
            return None
        result = self.student_collection.update_one({"_id": object_id}, {"$set": student.model_dump()})
        if result.matched_count == 0:
            return None
        return {"message": "Socials updated successfully"}

    def update_student_coding(self, student_id: str, student: StudentModelUpdateCoding):
        object_id = parse_student_object_id(student_id)
        if object_id is None:
            return None
        result = self.student_collection.update_one({"_id": object_id}, {"$set": student.model_dump()})
        if result.matched_count == 0:
            return None
        return {"message": "Coding details updated successfully"}

    def delete_student(self, student_id: str):
        object_id = parse_student_object_id(student_id)
        if object_id is None:
            return None
        result = self.student_collection.delete_one({"_id": object_id})
        if result.deleted_count == 0:
            return None
        return {"message": "Student deleted successfully"}

    def delete_all_students(self):
        self.student_collection.delete_many({})
        return {"message": "All students deleted successfully"}
