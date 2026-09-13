# 🎓 Course Registration System (CLI) - Starter Template
**จัดทำโดย:** Thitiwat Thaicharoen (AIGUS__)

ระบบจัดการข้อมูลรายวิชาและการลงทะเบียนเรียนแบบ Command Line Interface (CLI) พัฒนาด้วยภาษา Python เพื่อเป็นโครงสร้างตัวอย่าง (Starter Template) สำหรับการศึกษาการจัดการข้อมูลไบนารีไฟล์ชนิด Fixed-length Record ด้วยโมดูล `struct`

---

## 📌 Data Dictionary (โครงสร้างข้อมูลไบนารีทั้ง 3 ไฟล์)

การจัดเก็บข้อมูลในระบบจะแบ่งออกเป็น 3 ไฟล์หลัก โดยใช้โครงสร้างแบบ **Fixed-length Record** จัดเก็บด้วยรูปแบบ Little-Endian (`<`)

### 1. ไฟล์ข้อมูลนักศึกษา (`students.dat`) - ขนาด 97 Bytes / Record
| ฟิลด์ข้อมูล (Field) | ชนิดข้อมูล | ขนาด (Size) | คำอธิบาย (Description) |
| :--- | :--- | :--- | :--- |
| **student_id** | `int` (`Q`) | 8 Bytes | รหัสนักศึกษา 13 หลัก (Unsigned Long Long) |
| **student_code** | `str` (`15s`) | 15 Bytes | รหัสย่อ (UTF-8, Padding `\x00`) |
| **name** | `str` (`50s`) | 50 Bytes | ชื่อ-นามสกุล |
| **major** | `str` (`20s`) | 20 Bytes | สาขาวิชา |
| **year** | `int` (`I`) | 4 Bytes | ชั้นปี (1-4) |
| **status** | `int` (`I`) | 4 Bytes | สถานะ (`1` = Active, `0` = Deleted) |

> **Format String:** `"<Q 15s 50s 20s I I"` | **RECORD_SIZE:** `97 Bytes`

---

### 2. ไฟล์ข้อมูลรายวิชา (`courses.dat`) - ขนาด 105 Bytes / Record
| ฟิลด์ข้อมูล (Field) | ชนิดข้อมูล | ขนาด (Size) | คำอธิบาย (Description) |
| :--- | :--- | :--- | :--- |
| **course_id** | `int` (`I`) | 4 Bytes | รหัสไอดีรายวิชา |
| **course_code** | `str` (`15s`) | 15 Bytes | รหัสวิชา (เช่น CS101) |
| **title** | `str` (`50s`) | 50 Bytes | ชื่อรายวิชา |
| **category** | `str` (`20s`) | 20 Bytes | หมวดหมู่รายวิชา |
| **credits** | `int` (`I`) | 4 Bytes | จำนวนหน่วยกิต |
| **fee** | `float` (`f`) | 4 Bytes | ค่าธรรมเนียมรายวิชา |
| **status** | `int` (`I`) | 4 Bytes | สถานะ (`1` = Active, `0` = Deleted) |
| **is_full** | `int` (`I`) | 4 Bytes | สถานะที่นั่ง (`0` = Available, `1` = Full) |

> **Format String:** `"<I 15s 50s 20s I f I I"` | **RECORD_SIZE:** `105 Bytes`

---

### 3. ไฟล์ข้อมูลการลงทะเบียน (`enrollments.dat`) - ขนาด 36 Bytes / Record
| ฟิลด์ข้อมูล (Field) | ชนิดข้อมูล | ขนาด (Size) | คำอธิบาย (Description) |
| :--- | :--- | :--- | :--- |
| **enroll_id** | `int` (`I`) | 4 Bytes | รหัสการลงทะเบียน |
| **student_id** | `int` (`Q`) | 8 Bytes | อ้างอิงรหัสนักศึกษา (13 หลัก) |
| **course_id** | `int` (`I`) | 4 Bytes | อ้างอิงรหัสรายวิชา |
| **enroll_date** | `str` (`20s`) | 20 Bytes | วันเวลาลงทะเบียน (`YYYY-MM-DD HH:MM:SS`) |
| **status** | `int` (`I`) | 4 Bytes | สถานะ (`1` = Active, `0` = Cancelled) |

> **Format String:** `"<I Q I 20s I"` | **RECORD_SIZE:** `36 Bytes`

---

## 🛠️ รายละเอียดเมนูการทำงาน (Application Design)

* **1) แสดงข้อมูลในระบบ (View Sub-menu):**
  * `1.1` ดูรายวิชาทั้งหมด (Courses)
  * `1.2` ดูรายชื่อนักศึกษาทั้งหมด (Students)
  * `1.3` ดูรายการลงทะเบียนทั้งหมด (Enrollments)
* **2) เพิ่มข้อมูลใหม่ (Add Record):** เพิ่มข้อมูลลงไฟล์ `.dat` ด้วย `struct.pack()`
* **3) แก้ไขข้อมูล (Update Record):** ค้นหาและเขียนทับตำแหน่งเดิมโดยใช้ `file.seek()` (In-Place Update)
* **4) ลบข้อมูล (Delete Record):** ปรับสถานะ `status` เป็น `0` (Soft Delete)
* **5) สร้างรายงานสรุป (Generate Report):** อ่านข้อมูลจากไฟล์ไบนารีมาประมวลผลแล้วบันทึกลง `report.txt`

---

## 📄 ตัวอย่างไฟล์รายงานสรุปที่ต้องสร้าง (`report.txt`)

```text
Course Registration System - Summary Report
Generated At : 2026-09-13 13:14:47
App Version  : 2.0
Endianness   : Little-Endian
Encoding     : UTF-8 (fixed-length)
Files        : students.dat, courses.dat, enrollments.dat

=== รายวิชา (Courses) ===
-------------------------------------------------------------------------------------
| ID     | Code     | Title                | Category     | Credits | Fee       | Status  | Full  |
-------------------------------------------------------------------------------------
| 1001   | CS001    | Cyber Programming    | General      | 4       | 0.00      | Active  | No    |
-------------------------------------------------------------------------------------

=== นักศึกษา (Students) ===
----------------------------------------------------------------------
| Student ID      | Code     | Name                      | Major             | Status  |
----------------------------------------------------------------------
| 6906022610001   | STD001   | กัญญารัตน์ สุขเจริญ          | Data Science      | Active  |
----------------------------------------------------------------------
