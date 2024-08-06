import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def load_dict(dict_file):
    # 加载Excel文件
    df = pd.read_excel(dict_file)
    # 将第一列作为键，第二列作为值创建一个字典，并将所有值转换为字符串
    return dict(zip(df.iloc[:, 0].astype(str), df.iloc[:, 1].astype(str).fillna('')))

def convert_to_chinese(text, dictionary):
    result = []
    i = 0
    pattern = re.compile(r'ZCZC|NNNN|QA\d{2}\d{9}')
    
    while i < len(text):
        match = pattern.match(text, i)
        if match:
            # 如果匹配到保留字符序列，直接添加到结果中
            result.append(match.group())
            i += len(match.group())
        else:
            key = text[i:i+3]
            if key in dictionary:
                result.append(dictionary[key])
            else:
                result.append(key)  # 如果找不到对应的汉字，保留原始字符串
            i += 3
    return ''.join(result)

def open_dict_file():
    filepath = 'dict.xlsx'
    if filepath:
        try:
            return load_dict(filepath)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dictionary file: {e}")
    return None

def convert_text():
    input_text = input_text_box.get("1.0", tk.END).replace('\n', '').replace('\r', '')
    dictionary = open_dict_file()
    if dictionary:
        chinese_text = convert_to_chinese(input_text, dictionary)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, chinese_text)

# 创建主窗口
root = tk.Tk()
root.title("中文NAVTEX转换")

# 创建输入文本框
input_label = tk.Label(root, text="输入接收内容:")
input_label.pack()
input_text_box = tk.Text(root, height=20, width=100)
input_text_box.pack()

# 创建转换按钮
convert_button = tk.Button(root, text="转换", command=convert_text)
convert_button.pack()

# 创建输出文本框
output_label = tk.Label(root, text="输出中文结果:")
output_label.pack()
output_text_box = tk.Text(root, height=20, width=100)
output_text_box.pack()

# 运行主循环
root.mainloop()
