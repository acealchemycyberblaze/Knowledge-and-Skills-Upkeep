; nasm -f elf calc-str-lngth.asm 
; ld -m elf_i386 calc-str-lngth.o -o calc-str-lngth
; https://syscalls.kernelgrok.com/

SECTION	.data 
msg 	db	'Hello World I often feel like a noob!', 0Ah			; message string 

SECTION	.text
global 	_start

_start:
    mov     ebx, msg        ; move message string into EBX
    mov     eax, ebx        ; move EBX into EAX as well so that both pointers have msg string in memory
 
nextchar:
    cmp     byte [eax], 0   ; compare byte pointed by EAX at this address against zero EOSD
    jz      finished        ; jump to the point in the code labeled 'finished'
    inc     eax             ; increment EAX by one byte if zero not set
    jmp     nextchar        ; jump to code labeled 'nextchar'
 
finished:
    sub     eax, ebx        ; subtract EBX from the address in EAX
                            ; start same address but EAX has been incremented one byte for each character in the message string
                            ; when you subtract one memory address from another of the same type
                            ; the result is number of segments between them - in this case the number of bytes
 
    mov     edx, eax        ; EAX now equals the number of bytes in our string
    mov     ecx, msg       
    mov     ebx, 1
    mov     eax, 4
    int     80h
 
    mov     ebx, 0
    mov     eax, 1
    int     80h
