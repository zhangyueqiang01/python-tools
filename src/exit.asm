# 使用 int $0x80 (32位风格)
.section .text
.globl _start
_start:
    movl $1, %eax        # sys_exit = 1
    movl $42, %ebx       # 退出状态码
    int $0x80

# 使用 syscall (64位风格)  
.section .text
.globl _start
_start:
    movl $60, %eax       # sys_exit = 60
    movl $42, %edi       # 退出状态码
    syscall

	
	
# 编译与连接
as program.s -o program.o
ld program.o -o program

# 运行
./program

# 查看退出状态码
echo $?  # 输出 42
