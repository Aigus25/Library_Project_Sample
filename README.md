# 🎓 Course Registration System (CLI) - Starter Template จัดทำโดย: Thitiwat Thaicharoen (AIGUS__)

ระบบจัดการข้อมูลรายวิชาและการลงทะเบียนเรียนแบบ Command Line Interface (CLI) พัฒนาด้วยภาษา Python เพื่อเป็นตัวอย่างศึกษาการจัดการข้อมูลไบนารีไฟล์ชนิด Fixed-length Record ด้วยโมดูล `struct`

---

## 📌 Data Dictionary (โครงสร้างข้อมูลไบนารี)

การจัดเก็บข้อมูลในไฟล์ `courses.dat` จะใช้โครงสร้างแบบ **Fixed-length Record** ขนาดรวม **105 Bytes** ต่อ 1 รายการ โดยใช้วิธีการจัดเก็บแบบ Little-Endian (`<`)

| ฟิลด์ข้อมูล (Field) | ชนิดข้อมูล (Data Type) | ขนาด (Size) | คำอธิบาย (Description) | ตัวอย่างข้อมูล |
| :--- | :--- | :--- | :--- | :--- |
| **course_id** | `int` (`I`) | 4 Bytes | รหัสไอดีรายวิชา (Unsigned Int) | `1001` |
| **code** | `str` (`15s`) | 15 Bytes | รหัสวิชา (UTF-8, Padding `\x00`) | `CS101` |
| **title** | `str` (`50s`) | 50 Bytes | ชื่อรายวิชา (UTF-8, Padding `\x00`) | `Computer Programming` |
| **category** | `str` (`20s`) | 20 Bytes | หมวดหมู่รายวิชา (เช่น Core, GenEd) | `Core` |
| **credits** | `int` (`I`) | 4 Bytes | จำนวนหน่วยกิต | `3` |
| **fee** | `float` (`f`) | 4 Bytes | ค่าธรรมเนียมรายวิชา (Single Precision) | `1500.00` |
| **status** | `int` (`I`) | 4 Bytes | สถานะรายการ (`1` = Active, `0` = Deleted) | `1` |
| **enrolled** | `int` (`I`) | 4 Bytes | สถานะลงทะเบียน (`0` = Available, `1` = Full) | `0` |

> **Format String สำหรับ `struct`:** `"<I 15s 50s 20s I f I I"`  
> **ขนาดรวมต่อ Record:** `struct.calcsize(FORMAT)` = **105 Bytes**

---

## 🏗️ โครงสร้างฟังก์ชันแนวทาง (Skeleton Code)

ไฟล์ตัวอย่างโค้ด `main_starter.py` สำหรับนำไปศึกษาและพัฒนาระบบต่อ:

```python
import struct
import os

FORMAT = "<I """1) """2) """3) """4) """5) # ## 'ab' 'r+b' 'rb' (Sample) (Soft (THB) (THB, (fixed-length) (records) (report.txt) (เฉพาะสถานะ * **ทดสอบระบบไฟล์ไบนารี:** **ศึกษา **เขียน - --- ------------------------------------------------------------------------------------- 0 1""" 1. 1.0 1000.00 1001 1002 105 11:15:00 1250.00 1500.00 15s 2 2. 2026-09-09 20s 3 3. 50s : Active Active) App At Available Avg CS101 Category Category""" Code Computer Core Course CourseID Courses Credits Currently Data Delete)""" Deleted Dictionary:** Encoding Endianness English Enrolled Enrolled/Full FILENAME="courses.dat" Fee GEN111 GenEd Generated I I" ID Little-Endian Logic Max Min Min/Max/Avg No Now Padding Prog RECORD_SIZE Registration Report Statistics Status Summary System TODO: Title Total UTF-8 Version `.ljust(N, ``` ```text `main_starter.py` `read(RECORD_SIZE)` `seek()` `struct` add_course(): append b'\x00')` bytes decode('utf-8') def delete_course(): encode f file flag generate_report(): null-byte offset="index" only) pack padding pass pointer read(RECORD_SIZE) report.txt seek() status="=" struct.pack() text unpack update_course(): view_all_courses(): | คำนวณ คำนวณค่า ค้นหา ดูรายวิชาทั้งหมด: ด้วย ตรวจสอบการย้าย ตัวอย่างรูปแบบรายงานสรุป ที่ นำ ประมวลผลสถิติ ปรับค่า รับค่า รับค่าจากผู้ใช้ ลงไฟล์""" ลบรายวิชา: วนลูป วนลูปอ่านทีละ วิธีนำไปศึกษาและต่อยอด สตริง สรุปรายงาน: หา อ่านข้อมูลทั้งหมด อ่านเฉพาะรายการที่ เขียนทับ""" เขียนทับตำแหน่งเดิม เขียนทับในโหมด เขียนแบบ เข้าใจชนิดข้อมูล เติม เปิดไฟล์โหมด เป็น เพิ่มรายวิชาใหม่: เมื่อพัฒนาระบบเสร็จสมบูรณ์ แก้ไขข้อมูล: และการสแกน และการใช้ และแยกตาม และใช้ แล้ว แล้วปรับ แล้วเขียนลงไฟล์ แล้วใช้ โปรแกรมจะสามารถสร้างรายงานสรุปในรูปแบบ ในฟังก์ชัน:** ได้ดังนี้: ไบต์ ไปเติมการคำนวณและคำสั่งของโมดูล 📄 🛠️>

---

## 🔒 Intellectual Property & License
- **Original Author:** Thitiwat Thaicharoen (AIGUS__)
- **Project:** Course Registration System (COMPRO Project)
- **Usage Notice:** โค้ดนี้เป็นเพียง **Starter Template (ตัวอย่างโครงสร้าง)** สำหรับการศึกษาเท่านั้น ห้ามนำไปคัดลอกเพื่อส่งซ้ำโดยไม่ได้รับการอนุญาต
