from PySide6.QtCore import QDate

now1 = QDate.currentDate()

print(now1.toString())
print(now1.toString('d.M.yy'))