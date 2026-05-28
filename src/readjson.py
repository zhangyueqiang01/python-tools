#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys

def format_json_file(input_filename, output_filename="formatted.json"):
    try:
        with open(input_filename, 'r') as f:
            raw_data = f.read()

        data = json.loads(raw_data)
        formatted = json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
            sort_keys=True
        )

        with open(output_filename, 'w') as f:
            f.write(formatted.encode("utf-8"))

        print(u"\n✅ 格式化成功！")
        print(u"📄 原文件：%s" % input_filename)
        print(u"💾 输出文件：%s" % output_filename)
        print(u"\n===== 格式化内容 =====\n")
        print(formatted)

    except IOError:
        print(u"❌ 错误：文件 %s 不存在或无法读取" % input_filename)
    except ValueError:
        print(u"❌ 错误：文件内容不是合法 JSON")
    except Exception as e:
        print(u"❌ 未知错误：%s" % str(e))

if __name__ == "__main__":
    # 判断命令行参数
    if len(sys.argv) < 2:
        # 无参数，交互式让用户输入文件名
        print(u"未传入JSON文件，请输入JSON文件路径/名称：")
        in_file = raw_input().strip()
        if not in_file:
            print(u"❌ 未输入文件名，程序退出")
            sys.exit(1)
        format_json_file(in_file)
    else:
        # 取命令行第一个参数作为输入文件
        in_file = sys.argv[1]
        format_json_file(in_file)

