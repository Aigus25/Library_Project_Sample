"""
===============================================================================
  PROJECT    : Course Registration System (CLI Binary I/O - Starter Template)
  AUTHOR     : Thitiwat Thaicharoen (AIGUS__)
  RIGHTS     : Educational Starter Code - All Rights Reserved
  REPO       : https://github.com/Aigus25/Library_Project_Sample
===============================================================================
"""

import struct
import os
import datetime

# ============================================================
# 1. การกำหนดค่าคงที่และขนาด Struct (โครงสร้าง 3 ไฟล์)
# ============================================================
STUDENT_FILE = "students.dat"
COURSE_FILE = "courses.dat"
ENROLL_FILE = "enrollments.dat"
LOG_FILE = "operations.log"
REPORT_FILE = "report.txt"

# Q = Unsigned Long Long (8 Bytes) รองรับรหัสนักศึกษา 13 หลัก
# ลำดับ: student_id (Q), student_code (15s), name (50s), major (20s), year (I), status (I)
STUDENT_FORMAT = "<Q 15s 50s 20s I I"

# ลำดับ: course_id (I), course_code (15s), title (50s), category (20s), credits (I), fee (f), status (I), is_full (I)
COURSE_FORMAT = "<I 15s 50s 20s I f I I"

# ลำดับ: enroll_id (I), student_id (Q), course_id (I), enroll_date (20s), status (I)
ENROLL_FORMAT = "<I Q I 20s I"

STUDENT_SIZE = struct.calcsize(STUDENT_FORMAT)
COURSE_SIZE = struct.calcsize(COURSE_FORMAT)
ENROLL_SIZE = struct.calcsize(ENROLL_FORMAT)


def show_banner():
    print("=====================================================================")
    print(" 🎓 ระบบลงทะเบียนเรียน (Course Registration System - CLI) ")
    print(" 👤 Developed by: Thitiwat Thaicharoen (AIGUS__)")
    print("=====================================================================")


# Helper function guidance
def encode_fixed(s: str, size: int) -> bytes:
    """แปลงข้อความสตริงเป็น UTF-8 bytes และเติม Padding b'\\x00' ให้ครบขนาด"""
    # TODO: ผู้ศึกษานำไปเขียน Logic การตัดคำและการเติม null-byte (.ljust) ด้วยตนเอง
    pass


def decode_fixed(b: bytes) -> str:
    """แปลง Bytes กลับเป็นข้อความสตริง ตัด Padding b'\\x00' ทิ้ง"""
    # TODO: ผู้ศึกษานำไปเขียน Logic การ split(b'\\x00') และ decode ด้วยตนเอง
    pass


def view_all_courses():
    """1.1) ดูรายวิชาทั้งหมด"""
    print("\n--- 📖 [EXAMPLE] รายวิชาทั้งหมด (Courses) ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปิดไฟล์ courses.dat ด้วยโหมด 'rb'")
    print("2. วนลูปอ่านข้อมูลทีละ COURSE_SIZE")
    print("3. struct.unpack(COURSE_FORMAT, ...) แล้ว decode ข้อความ")
    print("4. แสดงเฉพาะรายการที่ status == 1\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic การอ่านไฟล์รายวิชาด้วยตนเอง
    pass


def view_all_students():
    """1.2) ดูรายชื่อนักศึกษาทั้งหมด"""
    print("\n--- 👨‍🎓 [EXAMPLE] รายชื่อนักศึกษาทั้งหมด (Students) ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปิดไฟล์ students.dat ด้วยโหมด 'rb'")
    print("2. วนลูปอ่านข้อมูลทีละ STUDENT_SIZE (รองรับ Q=8 Bytes)")
    print("3. struct.unpack(STUDENT_FORMAT, ...) แล้ว decode ข้อความ")
    print("4. แสดงเฉพาะรายการที่ status == 1\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic การอ่านไฟล์นักศึกษาด้วยตนเอง
    pass


def view_all_enrollments():
    """1.3) ดูประวัติการลงทะเบียนทั้งหมด"""
    print("\n--- 📝 [EXAMPLE] ประวัติการลงทะเบียน (Enrollments) ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปิดไฟล์ enrollments.dat ด้วยโหมด 'rb'")
    print("2. อ่านทีละ ENROLL_SIZE เพื่อเชื่อมโยง student_id และ course_id\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic การแสดงประวัติการลงทะเบียนด้วยตนเอง
    pass


def view_sub_menu():
    """เมนูย่อยสำหรับการแสดงผลข้อมูล (View Sub-menu)"""
    while True:
        print("\n--- 🔍 เมนูแสดงผลข้อมูล (View Data Menu) ---")
        print("1) ดูรายชื่อวิชาทั้งหมด (View All Courses)")
        print("2) ดูรายชื่อนักศึกษาทั้งหมด (View All Students)")
        print("3) ดูรายการลงทะเบียนทั้งหมด (View All Enrollments)")
        print("0) ย้อนกลับ (Back to Main Menu)")
        choice = input("เลือกเมนู (0-3): ").strip()

        if choice == "1":
            view_all_courses()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            view_all_enrollments()
        elif choice == "0":
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง ลองใหม่อีกครั้ง")


def add_record():
    """2) เพิ่มข้อมูลใหม่ (Add Record Template)"""
    print("\n--- ➕ [EXAMPLE] เพิ่มข้อมูลใหม่ ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เลือกประเภทข้อมูลที่ต้องการเพิ่ม (Student / Course / Enrollment)")
    print("2. เติม null-byte padding (b'\\x00') ด้วย encode_fixed()")
    print("3. แปลงเป็นข้อมูลไบนารีด้วย struct.pack()")
    print("4. บันทึกลงไฟล์ด้วยโหมด 'ab'\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic การรับค่าและ struct.pack() ด้วยตนเอง
    pass


def update_record():
    """3) แก้ไขข้อมูล (In-Place Update Template)"""
    print("\n--- ✏️ [EXAMPLE] แก้ไขข้อมูล ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปิดไฟล์โหมด 'r+b'")
    print("2. ค้นหารายการตาม ID โดยใช้ struct.unpack()")
    print("3. เมื่อเจอ ให้ใช้ file.seek(offset) ถอยตัวชี้ไปต้น Record")
    print("4. เขียนข้อมูลใหม่ทับลงไปทันทีด้วย file.write(packed_new)\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic seek() และเขียนทับด้วยตนเอง
    pass


def delete_record():
    """4) ลบข้อมูล (Soft Delete Template)"""
    print("\n--- 🗑️ [EXAMPLE] ลบข้อมูล (Soft Delete) ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปลี่ยนสถานะ status จาก 1 (Active) เป็น 0 (Deleted)")
    print("2. ใช้ file.seek(offset) แล้วเขียนทับตำแหน่งเดิม\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic Soft Delete ด้วยตนเอง
    pass


def generate_report():
    """5) สร้างไฟล์รายงานสรุป report.txt (Report Generator Template)"""
    print("\n--- 📄 [EXAMPLE] สร้างไฟล์รายงาน report.txt ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. อ่านข้อมูลจากทั้ง 3 ไฟล์ไบนารี")
    print("2. จัดฟอร์แมตตารางด้วย String Formatting")
    print("3. เขียนลงไฟล์ report.txt ในโหมด 'w' (UTF-8)\n")

    # TODO: ผู้ศึกษานำไปเขียน Logic การสร้างไฟล์รายงานสรุปด้วยตนเอง
    pass


def main_menu():
    while True:
        show_banner()
        print("1) แสดงข้อมูลในระบบ (View Data Sub-menu)")
        print("2) เพิ่มข้อมูลใหม่ (Add Record)")
        print("3) แก้ไขข้อมูล (Update Record)")
        print("4) ลบข้อมูล (Delete Record / Soft Delete)")
        print("5) สร้างรายงานสรุป (Generate Report)")
        print("0) ออกจากโปรแกรม (Exit)")
        choice = input("เลือกเมนู (0-5): ").strip()

        if choice == "1":
            view_sub_menu()
        elif choice == "2":
            add_record()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            generate_report()
        elif choice == "0":
            print("\nขอบคุณที่ใช้งานโปรแกรมจัดทำโดย Thitiwat Thaicharoen (AIGUS__) 👋\n")
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง ลองใหม่อีกครั้ง\n")


if __name__ == "__main__":
    main_menu()
