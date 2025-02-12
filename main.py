from PyQt6.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep
app = QApplication([])
from main_window import*
from menu_window import *


class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.count_asked = 0
        self.count_right = 0

    def got_right(self):
        print('Це правильна відповідь!')

    def got_wrong(self):
        print('Неправильна відповідь')


q1 = Question('Персик', 'peach', 'pear', 'paper','pad')
q2 = Question('Яблуко', 'apple', 'apply','application', 'pineapple')
q3 = Question('Мишка', 'mouse', 'mood', 'master', 'morty')
q4 = Question('Число', 'number', 'chislo', 'summa', 'amount')

cur_q = ''
question = [q1, q2, q3, q4]
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]


def new_question():
    global cur_q
    cur_q = choice (question)
    lb_question.setText(cur_q.answer)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.answer)
    radio_buttons[1].setText(cur_q.wrong_answer1)
    radio_buttons[2].setText(cur_q.wrong_answer2)
    radio_buttons[3].setText(cur_q.wrong_answer3)
new_question()


def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText('Правильно')
            else:
                lb_result.setText('Не вірно')
                cur_q.got_wrong()
            break


def change_screen():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')

    else:
        new_question()
        gb_answer.hide()
        gb_question.show()
        btn_next.setText('Відповісти')


def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()

def menu_show():
    window.hide()
    menu_win.show()
    lb_statistic.setText(
        f'Кількість правильних відповідей: {cur_q.count_right}\nКількість всього відповідей: {cur_q.count_asked}')



def clear():
    le_quest.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def back_menu():
    menu_win.hide()
    window.show()

def add_question():
    new_q = Question(le_quest.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(),le_wrong_ans3.text())
    question.append(new_q)
    clear()

btn_add.clicked.connect(add_question)
btn_clear.clicked.connect(clear)
btn_back.clicked.connect(back_menu)
btn_menu.clicked.connect(menu_show)
btn_rest.clicked.connect(rest)
btn_next.clicked.connect(change_screen)


app.exec()
