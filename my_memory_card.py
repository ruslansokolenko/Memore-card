#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memore card")
question = QLabel('какой национальности не существует?')
main_win.resize(600, 400)
btn_Ok = QPushButton("ответить")


#создание виджетов главного окна
RadioGroupBox = QGroupBox("варианты ответов")



layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

que = []
que.append(['какой национальности не существует?','Энцы', 'Смурфы', 'Чулымцы', 'Алеуты'])

def ask(question, right_answer, wrong1, wrong2, wrong3):
    rbtn_1 = QRadioButton(right_answer)
    rbtn_2 = QRadioButton(wrong1)
    rbtn_3 = QRadioButton(wrong2)
    rbtn_4 = QRadioButton(wrong3)
    
    pass
          
    
def check_answer():
    if answer[0].isChecked9():
        slow_correct("Правильно!")



ask('какой национальности не существует?','Энцы','Смурфы','Чулымцы','Алеуты')
btn_Ok.clicked.connect(check_answer)




RadioGroupBox.setLayout(layout_ans1)

#расположение виджетов по лэйаутам
layout_main = QVBoxLayout()
layoutH1 = QVBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question)
layoutH2.addWidget(RadioGroupBox)
layoutH3.addWidget(btn_Ok)

#создание второго GroupBox
RadioGroupBox2 = QGroupBox("результат тест")
layout_main = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()

#правильный ответ




layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)
#обработка нажатий на переключатели
#отображение окна приложения 
layoutH1.addWidget(question, alignment=Qt.AlignHCenter)
layoutH2.addWidget(RadioGroupBox)
layoutH3.addWidget(btn_Ok)

main_win.setLayout(layout_main)


main_win.show()
app.exec_()