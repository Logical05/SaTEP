[![Window11](https://img.shields.io/badge/Windows-blue?style=flat&logo=windows11)]()
[![Apache-2.0 license](https://img.shields.io/badge/license-Apache%202.0-%23D22128?style=flat&logo=apache
)](https://github.com/Logical05/SaTEP/blob/master/LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join-blue?logo=discord&logoColor=white)](https://discord.gg/Gtn9DN5UF5)

----
# SaTEP

Semi-automatic Teacher Evaluation Program for CKK.

## Installation

สามารถทําตามขั้นตอนด้านล่างเพื่อดาวน์โหลดตัวติดตั้งสําหรับโปรแกรมนี้

1. ดาวน์โหลด SaTEP_setup.exe ล่าสุดได้ที่ [releases](https://github.com/Logical05/SaTEP/releases)

2. เปิด SaTEP_setup.exe และทําตามขั้นตอนจนกว่าจะเสร็จสิ้น

3. เรียบร้อย ขอให้สนุกกับการประเมินครู 😁️

## How-To-Use

1. ให้ Login เข้าสู่ระบบด้วย Username กับ Password ของตนเอง (โปรแกรมไม่มีการเก็บ Password หรือ Username ใดๆทั้งนั้น)
![Screenshot 2024-02-19 021646](https://github.com/Logical05/SaTEP/assets/85784528/fef79720-8694-44e6-996e-a166faf5942d)


2. ให้เลือกว่าจะประเมินอะไร ตอนนี้มีประเมินครู หรือ ประเมินตนเอง (ถ้าเลือกประเมินตนเองให้เลื่อนลงไปตรงที่ เพิ่มเติม)
![Screenshot 2024-02-19 021738](https://github.com/Logical05/SaTEP/assets/85784528/791cc196-0b09-46d5-8fe9-ea4a6e9dfe82)


3. ถ้าเลือกประเมินครูให้เลือกตรง เทอม/ปี เพื่อเปลี่ยนเป็น เทอม/ปี ก่อนหน้าเพื่อที่จะทำการ Copy การตอบมาตอบปีนี้
![Screenshot 2024-02-19 021904](https://github.com/Logical05/SaTEP/assets/85784528/840ec861-49a7-4f5d-88b0-5214fe34b44e)


5. เลือกวิชาที่ต้องการจะ Copy แล้วเปิดหน้าโปรแกรมมาแล้วคลิก Copy
![Screenshot 2024-02-19 022107](https://github.com/Logical05/SaTEP/assets/85784528/e4e0db1b-2040-40a5-a377-dd4751c8fe3b)

6. ย้อนกลับมาที่ เทอม/ปี ปัจจุบันแล้วทำการคลิก Start หริอ Random เพื่อมั่วการประเมินก็ได้ (คำเตือน ถ้ามั่วเยอะระวังโดนครูเล่นนะ)
![Screenshot 2024-02-19 022129](https://github.com/Logical05/SaTEP/assets/85784528/319e39e3-2adf-4477-a1c5-4b5403769e51)

7. เลื่อนลงไปล่างสุดเพื่อทำการบันทึกผลการประเมินตามปกติได้เลย

### เพิ่มเติม

- ประเมินตนเองภาคปฏิบัติให้ทำตามวิธีการประเมินครูได้เลย
![Screenshot 2024-02-19 021925](https://github.com/Logical05/SaTEP/assets/85784528/26666298-95bd-496e-a1f2-06b053aebaf7)
![Screenshot 2024-02-19 023638](https://github.com/Logical05/SaTEP/assets/85784528/aab45954-a9c0-4b8d-9662-a266295ab18d)

- ประเมินตนเองภาคความรู้สึก ให้เลือกช่อง URL ด้านบนแล้วพิมพ์ต่อด้านหลังข้อความด้วย `&ChTerm=T&ChYear=Y`  T คือเทอมที่ต้องการจะ Copy และ Y คือปีที่ต้องการจะ Copy แล้วก็ Enter เสร็จแล้วก็ทำการคลิก Copy ในโปรแกรมแล้วก็ทำเหมือนวิธีการประเมินครูได้เลย
![Screenshot 2024-02-19 022007](https://github.com/Logical05/SaTEP/assets/85784528/6d5e2134-9f52-456e-87b6-c38a7c22ba7b)
![Screenshot 2024-02-19 023600](https://github.com/Logical05/SaTEP/assets/85784528/bd3dbc1f-56bf-4942-8969-4b3a2a315e79)
![Screenshot 2024-02-19 023653](https://github.com/Logical05/SaTEP/assets/85784528/83fbac43-d9fd-44c8-b725-a052d2c210b7)

## Python Library

- [pybrowsers](https://pypi.org/project/pybrowsers/)
- [numpy](https://pypi.org/project/numpy/)
- [selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)
- [py2exe](https://pypi.org/project/py2exe/)

## Copyright & License

อนุญาตให้แก้ไขและแจกจ่ายซ้ําได้ภายใต้เงื่อนไขของใบอนุญาต Apache 2.0
ดู [LICENSE](https://github.com/Logical05/SaTEP/blob/master/LICENSE) file สําหรับใบอนุญาตแบบเต็ม
