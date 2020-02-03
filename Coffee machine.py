import tkinter as tk
from functools import partial
window = tk.Tk()
top_frame = tk.Frame(window)
window.geometry('400x250')
window.configure(background='silver')
dict = {'咖啡豆': 10,'牛奶': 10,'砂糖': 10,'奶精':10}
IngredientsBox =['咖啡豆','牛奶','砂糖','奶精']
Cup = []
def MakingDrinks(Coffee):
    print(Coffee)
    if Coffee == '黑咖啡':
        Cup.clear()
        Cup.append(IngredientsBox[0])
        dict['咖啡豆'] = dict['咖啡豆'] - 1
        print(dict)
    elif Coffee == '焦糖瑪奇朵':
        Cup.clear()
        Cup.append(IngredientsBox[0])
        Cup.append(IngredientsBox[1])
        Cup.append(IngredientsBox[2])
        print(Cup)
        dict['咖啡豆'] = dict['咖啡豆'] - 1
        dict['牛奶'] = dict['牛奶'] - 1
        dict['砂糖'] = dict['砂糖'] - 1
        print(dict)
    elif Coffee == '卡布奇諾':
        Cup.clear()
        Cup.append(IngredientsBox[0])
        Cup.append(IngredientsBox[1])
        dict['咖啡豆'] = dict['咖啡豆'] - 1
        dict['牛奶'] = dict['牛奶'] - 1
        print(dict)
    else:
        if Coffee == '加糖':
            Cup.append('\n額外加'+IngredientsBox[2])
            dict['砂糖'] = dict['砂糖'] - 1
            print(dict)
        elif Coffee == '加奶精':
            Cup.append('\n額外加'+IngredientsBox[3])
            dict['奶精'] = dict['奶精'] - 1
            print(dict)

    text = ''.join(Cup)
    result_label.configure(text='使用'+text)
i = 10
j = 50
StoreName_frame = tk.Frame(window)
StoreName_frame.pack(side=tk.TOP)
StoreName_label = tk.Label(window, text='RoFish 好想喝咖啡機', width=20, height=2)
StoreName_label.pack(side=tk.TOP)

blackCoffee_label = tk.Button(window, text='黑咖啡', width=20, height=2, command=partial(MakingDrinks, '黑咖啡'))
blackCoffee_label.place(x=i, y=j)

CaramelMacchiato_label = tk.Button(window, text='焦糖瑪奇朵', width=20, height=2, command=partial(MakingDrinks, '焦糖瑪奇朵'))
CaramelMacchiato_label.place(x=i, y=j + 50)

Cappuccino_label = tk.Button(window, text='卡布奇諾', width=20, height=2, command=partial(MakingDrinks, '卡布奇諾'))
Cappuccino_label.place(x=i, y=j + 100)

Sugar_label = tk.Button(window, text='加糖', width=9, height=2,command=partial(MakingDrinks, '加糖'))
Sugar_label.place(x=i, y=j + 150)

creamers_label = tk.Button(window, text='加奶精', width=9, height=2,command=partial(MakingDrinks, '加奶精'))
creamers_label.place(x=i + 80, y=j + 150)

# result_frame = tk.Frame(window)
# result_frame.pack(side=tk.RIGHT)
result_label = tk.Label(window, background='White', width=20, height=10)
result_label.place(x=i + 200, y=j + 5)

window.mainloop()
