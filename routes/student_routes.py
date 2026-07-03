from fastapi import APIRouter, HTTPException

from services.student_service import StudentService
from models.student_model import StudentModelUpdate, StudentModelUpdatePassword, StudentModelUpdateSocials, StudentModelUpdateCoding , StudentModelSignIn , StudentModelSignUp

router = APIRouter( prefix="/students", tags=["students"], responses={404: {"description": "Not found"}})

student_service = StudentService()

@router.get("/")
async def get_all_students():
    return student_service.get_all_students()

@router.get("/{student_id}")
async def get_student_by_id(student_id: str):
    student = student_service.get_student_by_id(student_id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.post("/sign-up")
async def sign_up_student(student: StudentModelSignUp):
    student = student_service.sign_up_student(student)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.post("/sign-in")
async def sign_in_student(student: StudentModelSignIn):
    student = student_service.sign_in_student(student)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.put("/{student_id}")
async def update_student(student_id: str, student: StudentModelUpdate):
    student = student_service.update_student(student_id, student)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.put("/{student_id}/password")
async def update_student_password(student_id: str, student: StudentModelUpdatePassword):
    student = student_service.update_student_password(student_id, student)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.put("/{student_id}/socials")
async def update_student_socials(student_id: str, student: StudentModelUpdateSocials):
    student = student_service.update_student_socials(student_id, student)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.put("/{student_id}/coding")
async def update_student_coding(student_id: str, student: StudentModelUpdateCoding):
    student = student_service.update_student_coding(student_id, student)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{student_id}")
async def delete_student(student_id: str):
    student = student_service.delete_student(student_id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")
