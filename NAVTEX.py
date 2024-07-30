import pandas as pd

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_dict(dict_file):
    # 加载Excel文件
    df = pd.read_excel(dict_file)
    # 将第一列作为键，第二列作为值创建一个字典，并将所有值转换为字符串
    return dict(zip(df.iloc[:, 0].astype(str), df.iloc[:, 1].astype(str).fillna('')))

def convert_to_chinese(text, dictionary):
    result = []
    for i in range(0, len(text), 3):
        key = text[i:i+3]
        if key in dictionary:
            result.append(dictionary[key])
        else:
            result.append(key)  # 如果找不到对应的汉字，保留原始字符串
    return ''.join(result)

def main():
    input_file = 'input.txt'
    dict_file = 'dict.xlsx'
    output_file = 'output.txt'

    # 读取文件
    text = read_file(input_file)
    # 加载字典
    dictionary = load_dict(dict_file)
    # 转换为汉字
    chinese_text = convert_to_chinese(text, dictionary)

    # 将结果写入文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(chinese_text)

if __name__ == '__main__':
    main()
