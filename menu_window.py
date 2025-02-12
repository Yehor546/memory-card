from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout, QLineEdit
)

from main_window import lb_question

menu_win = QWidget()

lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть правильну відповідь:')
lb_wrong_ans1 = QLabel('Введіть хибну відповідь:')
lb_wrong_ans2 = QLabel('Введіть хибну відповідь:')
lb_wrong_ans3 = QLabel('Введіть хибну відповідь:')

le_quest = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

btn_add = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
btn_back = QPushButton('Назад')
lb_start_header = QLabel('Статистика')
lb_statistics = QLabel()
vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_quest)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

hl_questions = QHBoxLayout()
hl_questions.addLayout(vl_labels)
hl_questions.addLayout(vl_lineEdits)

lb_stat_header = QLabel('Статистика')
lb_statistic = QLabel()

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add)
hl_buttons.addWidget(btn_clear)

v1_main = QVBoxLayout()
v1_main.addLayout(hl_questions)
v1_main.addLayout(hl_buttons)
v1_main.addWidget(lb_start_header)
v1_main.addWidget(lb_statistic)
v1_main.addWidget(btn_back)
menu_win.setLayout(v1_main)
menu_win.resize(400,300)
menu_win.setWindowTitle('Меню')

