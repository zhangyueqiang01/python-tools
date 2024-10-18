#!/bin/bash

# 打印脚本的使用方法
usage() {
  echo "使用方法: $0 <测试文件路径>"
  echo "例如: $0 /tmp/testfile"
  echo "选项:"
  echo "  -h    显示此帮助信息"
}

# 判断是否传入参数或 -h 选项
if [ "$1" == "-h" ]; then
  usage
  exit 0
fi

if [ -z "$1" ]; then
  echo "错误: 缺少测试文件路径参数"
  usage
  exit 1
fi

TEST_FILE=$1
WRITE_SUM=0
READ_SUM=0
LOOPS=3
FILE_SIZE=1G  # 可以根据需要调整测试文件大小

# 开始循环测试
for i in $(seq 1 $LOOPS); do
  echo "第 $i 次测试写入速度..."
  WRITE_SPEED=$(dd if=/dev/zero of=${TEST_FILE} bs=$FILE_SIZE count=1 oflag=direct 2>&1 | grep -o '[0-9.]* [KMG]B/s' | awk '{print $1}')
  sync

  echo "第 $i 次测试读取速度..."
  READ_SPEED=$(dd if=${TEST_FILE} of=/dev/null bs=$FILE_SIZE count=1 iflag=direct 2>&1 | grep -o '[0-9.]* [KMG]B/s' | awk '{print $1}')
  sync

  # 累加每次的读写速度数值
  WRITE_SUM=$(echo "$WRITE_SUM + $WRITE_SPEED" | bc)
  READ_SUM=$(echo "$READ_SUM + $READ_SPEED" | bc)
done

# 计算平均值
WRITE_AVG=$(echo "scale=2; $WRITE_SUM / $LOOPS" | bc)
READ_AVG=$(echo "scale=2; $READ_SUM / $LOOPS" | bc)

# 删除临时测试文件
rm -f $TEST_FILE

# 输出平均速度结果
echo "写入速度平均值: $WRITE_AVG MB/s"
echo "读取速度平均值: $READ_AVG MB/s"


#dd if=/dev/zero of=testfile bs=1G count=1 oflag=direct：通过将/dev/zero的内容写入testfile，并使用oflag=direct来避免缓存的影响，测试写入速度。
#dd if=testfile of=/dev/null bs=1G count=1 iflag=direct：读取testfile的内容，直接传递到/dev/null，用iflag=direct来避免缓存，测试读取速度。
#sync：确保所有数据写入磁盘。
