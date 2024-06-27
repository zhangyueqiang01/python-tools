#!/bin/bash

# 检查是否有提供参数
if [ -z "$1" ]; then
    echo "请提供一个参数。"
    exit 1
fi

if [ "$1" == "-h" ]; then
    echo "请提供一个参数。"
    exit 0
fi

# 将命令行参数保存到变量new_param中
new_param="$1"

# 打印变量new_param的值
echo "添加新的功能是: $new_param"

# modify parser.add_argument
sed -i "s/,'xxxx'/,'$new_param','xxxx'/g" ./mytool.py

# 备份原文件
cp mytool.py mytool.py.bak

# 替换并复制内容
awk -v param="$new_param" '
{
    if ($0 ~ /elif args.show == .xxxx.:/) {
        # 替换并打印替换后的行
        gsub(/xxxx/, param, $0)
        print
        # 读取并替换下一行
        getline
        gsub(/xxxx/, param, $0)
        print
        # 打印原始内容的副本
        gsub(param, "xxxx", $0)
        print "    elif args.show == '\''xxxx'\'':"
        print $0
    } else {
        print
    }
}' mytool.py.bak > mytool.py

cp templet.txt tmp.txt
sed -i "s/xxxx/$new_param/g" tmp.txt

echo "新功能添加完毕: $new_param"
echo "请继续完善当前目录下的tmp.txt文件"

# 脚本结束
exit 0
