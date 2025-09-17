section .data
    msg db 'Hello, World!', 0xA  ; 要输出的字符串，0xA是换行符
    len equ $ - msg             ; 计算字符串长度

section .text
    global _start

_start:
    ; 系统调用write(fd, buf, count)
    mov rax, 1                  ; sys_write系统调用号（64位系统中为1）
    mov rdi, 1                  ; 文件描述符1表示标准输出
    mov rsi, msg                ; 要输出的字符串地址
    mov rdx, len                ; 字符串长度
    syscall                     ; 64位系统使用syscall指令而非int 0x80

    ; 系统调用exit(0)
    mov rax, 60                 ; sys_exit系统调用号（64位系统中为60）
    xor rdi, rdi                ; 退出状态码0
    syscall                     ; 触发系统调用

