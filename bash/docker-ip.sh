#!/bin/bash
# 脚本功能：快速查看所有Docker容器的IP地址

# 检查是否安装了docker
if ! command -v docker &> /dev/null; then
    echo "错误：未安装Docker，请先安装Docker！"
    exit 1
fi

# 输出表头
echo -e "\033[32m=========================================\033[0m"
echo -e "\033[34m容器ID\t\t容器名称\t\tIP地址\033[0m"
echo -e "\033[32m=========================================\033[0m"

# 遍历所有运行中的容器
docker ps -q | while read container_id; do
    # 获取容器名称（去掉前缀/）
    container_name=$(docker inspect -f '{{.Name}}' $container_id | sed 's/^\///')
    # 获取容器IP地址
    container_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container_id)
    
    # 输出信息（如果IP为空，显示"无"）
    if [ -z "$container_ip" ]; then
        container_ip="无"
    fi
    echo -e "${container_id:0:12}\t$container_name\t$container_ip"
done

echo -e "\033[32m=========================================\033[0m"
echo "提示：仅显示运行中的容器，如需查看所有容器，请修改脚本中的 docker ps -q 为 docker ps -aq"
