; nasm -f elf helloworld.asm 
; ld -m elf_i386 helloworld.o -o helloworld 
; https://syscalls.kernelgrok.com/
; edx lob of string | ecx address of .data | ebc loaded with the file we want to write to (STDOUT)

SECTION	.data 
msg 	db	'Hello World!', 0Ah			; this would be your message string 

SECTION	.text
global 	_start

_start:
	mov		edx, 13		; 12bytes + 0Ah=13 which is lfc
	mov		ecx, msg	; mov mem of string into ecx
	mov 	ebc, 1		; STDOUT file
	mov		eax, 4		; invoke SYS_WRITE (optcode4)
	int		80h 		; opt code for inturupts 
