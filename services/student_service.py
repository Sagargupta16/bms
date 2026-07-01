from fastapi import Depends
from pymongo import MongoClient
from bson import ObjectId

from config.secrets_parser import get_db, get_student_collection
from models.student_model import StudentModel, StudentModelUpdate, StudentModelUpdatePassword, StudentModelUpdateSocials, StudentModelUpdateCoding, StudentModelSignIn, StudentModelSignUp
from bson.json_util import dumps

class StudentService:
    def __init__(self, db: MongoClient = Depends(get_db)):
        self.db = db
        self.student_collection = get_student_collection()

    def get_all_students(self):
        return dumps(list(self.student_collection.find({})))

    def get_student_by_id(self, student_id: str):
        return self.student_collection.find_one({"_id": ObjectId(student_id)})

    def get_student_by_email(self, email: str):
        return self.student_collection.find_one({"email": email})

    def sign_up_student(self, student: StudentModelSignUp):
        result = self.student_collection.insert_one(student.model_dump())
        inserted_id = result.inserted_id
        return {"message": "Student registered successfully", "student_id": str(inserted_id)}

    def sign_in_student(self, student: StudentModelSignIn):
        return self.student_collection.find_one({"email": student.email, "password": student.password})

    def update_student(self, student_id: str, student: StudentModelUpdate):
        changes = student.model_dump(exclude_unset=True)
        if changes:
            self.student_collection.update_one({"_id": ObjectId(student_id)}, {"$set": changes})
        return self.student_collection.find_one({"_id": ObjectId(student_id)})

    def update_student_password(self, student_id: str, student: StudentModelUpdatePassword):
        self.student_collection.update_one({"_id": ObjectId(student_id)}, {"$set": student.model_dump()})
        return {"message": "Password updated successfully"}

    def update_student_socials(self, student_id: str, student: StudentModelUpdateSocials):
        self.student_collection.update_one({"_id": ObjectId(student_id)}, {"$set": student.model_dump()})
        return {"message": "Socials updated successfully"}

    def update_student_coding(self, student_id: str, student: StudentModelUpdateCoding):
        self.student_collection.update_one({"_id": ObjectId(student_id)}, {"$set": student.model_dump()})
        return {"message": "Coding details updated successfully"}

    def delete_student(self, student_id: str):
        self.student_collection.delete_one({"_id": ObjectId(student_id)})
        return {"message": "Student deleted successfully"}

    def delete_all_students(self):
        self.student_collection.delete_many({})
        return {"message": "All students deleted successfully"}
