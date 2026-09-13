"""
===============================================================================
  PROJECT   : Library Borrowing System (CLI Binary I/O - Starter Template)
  AUTHOR    : Thitiwat Thaicharoen (AIGUS__)
  RIGHTS    : Educational Starter Code - All Rights Reserved
  REPO      : https://github.com/Aigus25/Library_Project_Sample
===============================================================================
"""

import struct
import os
import datetime

# โครงสร้าง 105 Bytes (Fixed-length Record)
# I   = Book ID (4 bytes)
# 15s = ISBN (15 bytes)
# 50s = Title (50 bytes)
# 20s = Category (20 bytes)
# I   = Publish Year (4 bytes)
# f   = Rental Price per Day (4 bytes)
# I   = Status (4 bytes: 1=Active, 0=Deleted)
# I   = Borrowed Status (4 bytes: 1=Borrowed/Unavailable, 0=Available)
FORMAT = "<I 15s 50s 20s I f I I"
RECORD_SIZE = struct.calcsize(FORMAT)
FILENAME = "books.dat"

def show_banner():
    print("=====================================================================")
    print(" 📚 ระบบยืม-คืนหนังสือในห้องสมุด (Library Borrowing System - CLI) ")
    print(" 👤 Developed by: Thitiwat Thaicharoen (AIGUS__)")
    print("=====================================================================")

def add_book():
    """1) เพิ่มหนังสือใหม่เข้าระบบ (Starter Template)"""
    print("\n--- ➕ [EXAMPLE] เพิ่มหนังสือใหม่ ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. รับค่า book_id, isbn, title, category, year, price จากผู้ใช้")
    print("2. แปลงข้อความสตริงเป็น UTF-8 bytes และเติม Padding b'\\x00' ด้วย .ljust()")
    print("3. ใช้ struct.pack(FORMAT, ...) เพื่อแปลงเป็นไบนารีข้อมูลขนาด 105 ไบต์")
    print("4. เขียนข้อมูลลงไฟล์ด้วยโหมด 'ab'\n")
    
    # TODO: ผู้ศึกษานำไปเขียน Logic struct.pack() บันทึกลงไฟล์ books.dat ด้วยตนเอง
    pass

def update_book():
    """2) แก้ไขข้อมูลหนังสือ (In-Place Update Template)"""
    print("\n--- ✏️ [EXAMPLE] แก้ไขข้อมูลหนังสือ ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปิดไฟล์ด้วยโหมด 'r+b'")
    print("2. วนลูปอ่านข้อมูลทีละ RECORD_SIZE (105 Bytes)")
    print("3. ใช้ struct.unpack() เพื่ออ่านค่า ID และเช็ก status == 1")
    print("4. เมื่อเจอตำแหน่งที่ต้องการ ให้ใช้ file.seek(offset) เพื่อถอยตัวชี้ไปเริ่มต้น Record")
    print("5. เขียนข้อมูลใหม่ทับตำแหน่งเดิมทันทีด้วย file.write(packed_new)\n")
    
    # TODO: ผู้ศึกษานำไปเขียน Logic การค้นหาและ seek() เขียนทับด้วยตนเอง
    pass

def delete_book():
    """3) ลบหนังสือ (Soft Delete Template)"""
    print("\n--- 🗑️ [EXAMPLE] ลบหนังสือ (Soft Delete) ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. ใช้หลักการ Soft Delete โดยไม่ลบข้อมูลออกจากไฟล์ไบนารีจริง")
    print("2. ปรับค่าฟิลด์ status จาก 1 (Active) ให้กลายเป็น 0 (Deleted)")
    print("3. ใช้ file.seek(offset) แล้วเขียนข้อมูลที่แก้ status แล้วกลับลงไปที่เดิม\n")
    
    # TODO: ผู้ศึกษานำไปเขียน Logic Soft Delete ด้วยตนเอง
    pass

def view_all_books():
    """4) ดูรายชื่อหนังสือทั้งหมด"""
    print("\n--- 📖 [EXAMPLE] รายชื่อหนังสือทั้งหมด ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. เปิดไฟล์ด้วยโหมด 'rb'")
    print("2. อ่านทีละ RECORD_SIZE จนกว่าจะหมดไฟล์ (not data_read)")
    print("3. แสดงเฉพาะรายการที่ status == 1\n")
    
    # TODO: ผู้ศึกษานำไปเขียน Logic การอ่านและ decode('utf-8') ด้วยตนเอง
    pass

def generate_report():
    """5) สร้างไฟล์รายงาน report.txt (Report Generator Template)"""
    print("\n--- 📄 [EXAMPLE] สร้างไฟล์รายงาน report.txt ---")
    print("📌 คำอธิบายสำหรับผู้ศึกษา:")
    print("1. อ่านหนังสือทั้งหมดจาก books.dat เข้ามาประมวลผล")
    print("2. คำนวณ Statistics (Min, Max, Avg ของราคาเช่าต่อวัน)")
    print("3. จัดกลุ่มนับจำนวนหนังสือแยกตามหมวดหมู่ (Category)")
    print("4. เขียนข้อมูลลงไฟล์ report.txt พร้อมสลัก Header เครดิตผู้พัฒนา\n")
    
    # TODO: ผู้ศึกษานำไปเขียน Logic การสร้างรายงานด้วยตนเอง
    pass

def main_menu():
    while True:
        show_banner()
        print("1) เพิ่มหนังสือใหม่ (Add Book)")
        print("2) แก้ไขข้อมูลหนังสือ (Update Book)")
        print("3) ลบหนังสือ (Delete Book)")
        print("4) ดูหนังสือทั้งหมด (View All Books)")
        print("5) สร้างรายงานสรุป (Generate Report)")
        print("0) ออกจากโปรแกรม (Exit)")
        choice = input("เลือกเมนู (0-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            view_all_books()
        elif choice == "5":
            generate_report()
        elif choice == "0":
            print("\nขอบคุณที่ใช้งานโปรแกรมตัวอย่างจัดทำโดย Thitiwat Thaicharoen (AIGUS__) 👋\n")
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง ลองใหม่อีกครั้ง\n")

if __name__ == "__main__":
    main_menu()