[![Window11](https://img.shields.io/badge/Windows-blue?style=flat&logo=windows11)]()
[![Apache-2.0 license](https://img.shields.io/badge/license-Apache%202.0-%23D22128?style=flat&logo=apache
)](https://github.com/Logical05/SaTEP/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join-blue?logo=discord&logoColor=white)](https://discord.gg/Gtn9DN5UF5)

----
# SaTEP (Windows Only)

Semi-automatic Teacher Evaluation Program for CKK. (ขอตั้งชื่อไว้แบบเดิมแต่ทำได้หมด)

## Installation

สามารถทําตามขั้นตอนด้านล่างเพื่อดาวน์โหลดตัวติดตั้งสําหรับโปรแกรมนี้ (ถ้ามี version เก่าอยู่ให้ลบก่อน)

1. ดาวน์โหลด SaTEP_setup.exe ล่าสุดได้ที่ [releases](https://github.com/Logical05/SaTEP/releases)

2. เปิด SaTEP_setup.exe และทําตามขั้นตอนจนกว่าจะเสร็จสิ้น

3. เรียบร้อย ขอให้สนุกกับการประเมินใน CKK-MIS 😁️

## How-To-Use

1. ให้ Login เข้าสู่ระบบด้วย Username กับ Password ของตนเอง (โปรแกรมไม่มีการเก็บ Password หรือ Username ใดๆทั้งนั้น)
![Screenshot 2024-02-19 021646](https://github.com/Logical05/SaTEP/assets/85784528/fef79720-8694-44e6-996e-a166faf5942d)

2. ให้เลือกว่าจะประเมินอะไร ตอนนี้โปรแกรมสามารถประเมินได้ทุกอัน (ถ้าจะเลือกประเมินอย่างอื่นที่ไม่ใช่ประเมินครูให้เลื่อนลงไปตรงที่ เพิ่มเติม)
![Screenshot 2024-02-19 021738](https://github.com/Logical05/SaTEP/assets/85784528/791cc196-0b09-46d5-8fe9-ea4a6e9dfe82)

3. ถ้าเลือกประเมินครูให้เลือกตรง เทอม/ปี เพื่อเปลี่ยนเป็น เทอม/ปี ก่อนหน้าเพื่อที่จะทำการ Copy การตอบมาตอบปีนี้
![Screenshot 2024-02-19 021904](https://github.com/Logical05/SaTEP/assets/85784528/840ec861-49a7-4f5d-88b0-5214fe34b44e)


5. เลือกวิชาที่ต้องการจะ Copy แล้วเปิดหน้าโปรแกรมมาแล้วคลิก Copy
![Screenshot 2024-02-19 022107](https://github.com/Logical05/SaTEP/assets/85784528/e4e0db1b-2040-40a5-a377-dd4751c8fe3b)

6. ย้อนกลับมาที่ เทอม/ปี ปัจจุบันแล้วทำการคลิก Start หริอ Random เพื่อมั่วการประเมินก็ได้ (คำเตือน ถ้ามั่วเยอะระวังโดนครูเล่นนะ)  
![Screenshot 2024-02-19 022129](https://github.com/Logical05/SaTEP/assets/85784528/319e39e3-2adf-4477-a1c5-4b5403769e51)

7. เลื่อนลงไปล่างสุดเพื่อทำการบันทึกผลการประเมินตามปกติได้เลย

### เพิ่มเติม

- ในการประเมินอย่างอื่นยกเว้นประเมินครูให้กรอกปีที่ต้องการจะ Copy เพื่อนำคำตอบอันเก่ามาตอบใหม่ในปีนี้โดยที่เราไม่ต้องมานั่งคลิกประเมินเอง (แต่ถ้าใครอยากคลิกเองก็ไม่ว่านะ) หลังจากกรอกปีที่ต้องการจะ Copy เสร็จแล้วก็ให้เปิดเว็ปหน้าแบบประเมินที่ต้องการจะกรอกแล้วคลิกชื่อแบบประเมินในโปรแกรมได้เลย แล้วตัวโปรแกรมจะทำการกรอกแบบประเมินให้เองโดยที่เราไม่ต้องทำอะไรเลย หลังจากโปรแกรมกรอกเสร็จก็กดบันทึกได้เลย

  ![Screenshot 2024-02-20 102710](https://github.com/Logical05/SaTEP/assets/85784528/3999d3cb-bc1e-4f1e-bacb-34827e18e310)

## Python Library (Python 3.11)

- [pybrowsers](https://pypi.org/project/pybrowsers/)
- [numpy](https://pypi.org/project/numpy/)
- [selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)
- [pyinstaller](https://pypi.org/project/pyinstaller/)
- [pillow](https://pypi.org/project/pillow/)

## Copyright & License

อนุญาตให้แก้ไขและแจกจ่ายซ้ําได้ภายใต้เงื่อนไขของใบอนุญาต Apache 2.0
ดู [LICENSE](https://github.com/Logical05/SaTEP/blob/master/LICENSE) file สําหรับใบอนุญาตแบบเต็ม
