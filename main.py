import os
import json
from cssbeautifier import beautify as css_beautify
from bs4 import BeautifulSoup
from jsbeautifier import beautify as js_beautify

base_dir = r"E:\repo\!Others\code-readable\pagenote_u"

class btf:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def js(self):
        with open(self.input_file, "r", encoding='utf-8') as f:
            compressed_code = f.read()
        uncompressed_code = js_beautify(compressed_code)
        with open(self.output_file, "w", encoding='utf-8') as f:
            f.write(uncompressed_code)
        print(f"处理完成：\t{self.output_file}")

    def css(self):
        with open(self.input_file, "r", encoding='utf-8') as f:
            compressed_code = f.read()
        # 使用 css_beautify 格式化 CSS
        uncompressed_code = css_beautify(compressed_code)
        with open(self.output_file, "w", encoding='utf-8') as f:
            f.write(uncompressed_code)
        print(f"处理完成：\t{self.output_file}")

    def html(self):
        with open(self.input_file, "r", encoding='utf-8') as f:
            compressed_code = f.read()
        soup = BeautifulSoup(compressed_code, 'html.parser')
        uncompressed_code = soup.prettify()
        with open(self.output_file, "w", encoding='utf-8') as f:
            f.write(uncompressed_code)
        print(f"处理完成：\t{self.output_file}")

    def json(self):
        with open(self.input_file, "r", encoding='utf-8') as f:
            compressed_code = f.read()
        # 不需要将 JSON 字符串转换成对象再转回字符串
        uncompressed_code = json.dumps(json.loads(compressed_code), indent=2, ensure_ascii=False)
        with open(self.output_file, "w", encoding='utf-8') as f:
            f.write(uncompressed_code)
        print(f"处理完成：\t{self.output_file}")

def walk_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            input_path = os.path.join(root, file)
            output_path = os.path.join(root, file)
            if file.endswith(".js"):
                print(f'正在处理文件：\t{input_path}')
                btf(input_path, output_path).js()
            elif file.endswith(".css"):
                print(f'正在处理文件：\t{input_path}')
                btf(input_path, output_path).css()
            elif file.endswith(".html"):
                print(f'正在处理文件：\t{input_path}')
                btf(input_path, output_path).html()
            elif file.endswith(".json"):  # 添加对 JSON 文件的处理
                print(f'正在处理文件：\t{input_path}')
                btf(input_path, output_path).json()
            else:
                print(f'跳过文件：\t{input_path}')
    print("所有文件处理完成！")

walk_dir(base_dir)
