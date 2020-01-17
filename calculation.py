import tkinter as tk
from functools import partial
window = tk.Tk()
top_frame = tk.Frame(window)
window.geometry('800x600')
window.configure(background='white')
buttonText = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['+', '-', 'c'],
    ['x', '÷', '=']]
count = 0
is_add = False
is_minus = False
is_times = False
is_divided = False
action = []
def calculate_number(number):
    global count
    global is_add
    global is_minus
    global is_divided
    global is_times
    if number == '=':
        action2 = countTimesAndDivided()
        countNumber2(action2)
    elif number == 'c':
        count = 0
        is_add = False
        is_minus = False
        is_times = False
        is_divided = False
        action.clear()
        text = ''.join(action)
        result_label.configure(text=text)
    else:
        action.append(number)
        text = ''.join(action)
        result_label.configure(text=text)
def countTimesAndDivided():
    index = 0
    action2 = []
    while index <= len(action) - 1:
        if action[index] == 'x':
            if index > 1:
                if (action[index - 2]) == 'x' or (action[index - 2]) == '÷':
                    TimesNumber = int(action2[-1]) * int(action[index + 1])
                    action2.append(TimesNumber)
                else:
                    TimesNumber = int(action[index-1]) * int(action[index + 1])
                    action2.append(TimesNumber)
            else:
                TimesNumber = int(action[index - 1]) * int(action[index + 1])
                action2.append(TimesNumber)
            del action2[-2]
            index += 2
        elif action[index] == '÷':
            if index > 1:
                if (action[index - 2]) == 'x' or (action[index - 2]) == '÷':
                    TimesNumber = int(action2[-1]) / int(action[index + 1])
                    action2.append(TimesNumber)
                else:
                    TimesNumber = int(action[index-1]) / int(action[index + 1])
                    action2.append(TimesNumber)
            else:
                DividedNumber = int(action[index - 1]) / int(action[index + 1])
                action2.append(DividedNumber)
            del action2[-2]
            index += 2
        else:
            action2.append(action[index])
            index += 1
    return action2
def countNumber2(action2):
    for number in action2:
        global count
        global is_add
        global is_minus
        if number == '+':
            is_add = True
        elif number == '-':
            is_minus = True
        else:
            if is_add:
                count += int(number)
                is_add = False
            elif is_minus:
                count -= int(number)
                is_minus = False
            else:
                count = int(number)
            print(action2)

    result_label.configure(text=count)


output_frame = tk.Frame(window)
output_frame.pack(side=tk.TOP)
output_label = tk.Label(output_frame, text='結果')
output_label.pack(side=tk.LEFT)

result_frame = tk.Frame(window)
result_frame.pack(side=tk.TOP)
result_label = tk.Label(result_frame, text='', background='gray', width=20, height=1)
result_label.pack(side=tk.TOP)

for i in range(5):
    for j in range(3):
        l = tk.Button(window, text=buttonText[i][j], fg='red', command=partial(calculate_number, buttonText[i][j]))
        l.place(x=20 + j * 30, y=30 + i * 30, width=30, height=30)

window.mainloop()