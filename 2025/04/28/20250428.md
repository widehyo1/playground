https://dman95.github.io/SASM/english.html

Downlaod .exe for Windows

create new project

settings > settings > build > Mode: x64 check, apply and ok

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov eax,10
    PRINT_DEC 1, eax
    
    xor rax, rax
    ret
```

build and run
10
```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov eax,0x1234    ; A레지스터 32bit 크기에 0x1234값을 저장
    mov ax,0x1234     ; A레지스터 16bit 크기에 0x1234값을 저장
    mov ax,bx         ; bx의 값을 ax로 복사
    mov ax,ebx        ; [error] ebx(32bit) 값을 ax(16bit)에 복사 (데이터 손실로 허용되지 않음)
    
    xor rax, rax
    ret
```

초기화되지 않은 변수 선언:
초기화 되지 않은 변수는 section .bss블록에서 선언해야하며
사용하고자 하는 크기와 변수 개수를 지정하면 된다

변수이름 크기지시자 개수
resb : 1byte
resw : 2byte
resd : 4byte
resq : 8byte
```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here

    xor rax, rax
    ret

section .bss
    a resb 1    ; declare 1byte size one   a variable
    b resw 2    ; declare 2byte size two   b variables
    c resd 1    ; declare 4byte size one   c variable
    d resq 3    ; declare 8byte size three d variables
```

초기화된 변수 선언: section .data
변수이름 크기지시자 개수
db: 1byte
dw: 2byte
dd: 4byte
dq: 8byte
```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here

    xor rax, rax
    ret

section .data
    a db 0x33      ; declare 1byte variable a with value 0x33
    b dw 0x1234    ; declare 2byte variable b with value 0x1234
    c dd 0x12345678; declare 4byte variable c with value 0x12345678
    d dq 0x1234    ; declare 8byte variable d with value 0x1234
```

변수는 크기, 주소값, 실제 저장된 값을 가진다.
```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,[a]        ; move from the value of variable a to ax register
    mov [b],ax        ; move from the stored value of ax register to b variable

    PRINT_HEX 2,ax    ; print the value of ax register with hex base per 2byte
    NEWLINE
    PRINT_HEX 2,a     ; print the value of variable a with hex base per 2byte
    NEWLINE
    PRINT_HEX 2,b     ; print the value of variable b with hex base per 2byte
    NEWLINE
    PRINT_DEC 2,ax    ; print the value of register ax with 10 base pre 2byte

    xor rax, rax
    ret

section .data
    a dw 0x12
section .bss
    b resw 1
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov [e],a
    mov [f],b
    mov [g],c
    mov [h],d
    PRINT_HEX 2,a
    NEWLINE
    PRINT_HEX 2,b
    NEWLINE
    PRINT_HEX 2,c
    NEWLINE
    PRINT_HEX 2,d
    NEWLINE
    PRINT_HEX 2,e
    NEWLINE
    PRINT_HEX 2,f
    NEWLINE
    PRINT_HEX 2,g
    NEWLINE
    PRINT_HEX 2,h
    NEWLINE
    xor rax, rax
    ret
section .data
    a db 0x01
    b dw 0x0002
    c dd 0x00000003
    d dq 0x0000000000000004
section .bss
    e resb 1
    f resw 1
    g resd 1
    h resq 1
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ah,[a]
    mov [e],ah
    mov ax,[b]
    mov [f],ax
    mov eax,[c]
    mov [g],eax
    mov rax,[d]
    mov [h],rax
    PRINT_HEX 1,a
    NEWLINE
    PRINT_HEX 2,b
    NEWLINE
    PRINT_HEX 4,c
    NEWLINE
    PRINT_HEX 8,d
    NEWLINE
    PRINT_HEX 1,e
    NEWLINE
    PRINT_HEX 2,f
    NEWLINE
    PRINT_HEX 4,g
    NEWLINE
    PRINT_HEX 8,h
    NEWLINE
    xor rax, rax
    ret
    
section .data
    a db 0x01
    b dw 0x0002
    c dd 0x00000003
    d dq 0x0000000000000004
    
section .bss
    e resb 1
    f resw 1
    g resd 1
    h resq 1
```

PRINT_STRING para
para: 출력할 곳의 주소
단, 문자열 종료는 0x00으로 표시되어야 한다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    PRINT_STRING msg1
    NEWLINE
    PRINT_STRING msg2
    NEWLINE
    PRINT_STRING msg3
    NEWLINE

    xor rax, rax
    ret

section .data
    msg1 db 'haha ',0x00
    msg2 db 'hello !',0x00
    msg3 db "msg3 ok",0x00
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    PRINT_STRING msg1
    NEWLINE
    PRINT_STRING msg2
    NEWLINE
    PRINT_STRING msg3
    NEWLINE

    xor rax, rax
    ret

section .data
    msg1 db 'haha ',0x00
    msg2 db 'hello !',0x0A,'world',0x0D,'wow',0x00
    msg3 db "msg3 ok",0x00
```

여기서 문자열에 캐리지 리턴(CR:0x0D) 또는 라인 피드(LF:0x0A)를 포함하면 PRINT_STRING 매크로 함수는 C처럼 output 창의 줄을 변경하여 문자열을 출력해준다
보통 윈도우는 0x0D, 0x0A의 연속 문자를 유닉스는 0x0A만으로 줄 변경을 수행할 수 있는데...

GET_DEC para1, para2(키보드로 입력된 문자열은 10진수로 인식)
para1: 입력할 바이트 수
para2: 입력받을 곳으로 레지스터 또는 메모리 주소

GET_HEX para1, para2(키보드로 입력된 문자열은 16진수로 인식)
para1: 입력할 바이트 수
para2: 입력받을 곳으로 레지스터 또는 메모리 주소

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    GET_DEC 1,al ; 1byte input
    GET_DEC 2,a  ; 2byte input

    PRINT_DEC 1,al
    NEWLINE
    PRINT_DEC 2, a

    xor rax, rax
    ret

section .bss
    a resw 1
```

ADD para1, para2(para1 = para1 + para2의 의미)
para1: 레지스터 또는 메모리에 있는 값
para2: 레지스터, 메모리, 값
para1, para2가 모두 메모리인 경우는 허용되지 않는다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,1
    mov bx,3

    add ax,bx
    PRINT_DEC 2,ax
    NEWLINE

    mov [a],word 7
    add ax,[a]
    PRINT_DEC 2,ax
    NEWLINE

    mov bx,2
    add [a],bx
    PRINT_DEC 2,a
    NEWLINE

    mov [b],byte 2
    ; add [a],[b] <= error!

    xor rax, rax
    ret

section .bss
    a resw 1
    b resw 1
```

SUB para1, para2(para1 = para1 - para2의 의미)
para1: 레지스터 또는 메모리에 있는 값
para2: 레지스터, 메모리, 값
para1, para2가 모두 메모리인 경우는 허용되지 않는다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,1
    mov bx,3

    sub ax,bx
    PRINT_DEC 2,ax
    NEWLINE

    mov [a],word 7
    sub ax,[a]
    PRINT_DEC 2,ax
    NEWLINE

    mov bx,2
    sub [a],bx
    PRINT_DEC 2,a
    NEWLINE

    mov [b],byte 2
    ; sub [a],[b]

    xor rax, rax
    ret

section .bss
    a resw 1
    b resw 1

```

MUL para(1byte)
para가 1byte일 때: AX=AL * para
para는 레지스터만 허용된다.
곱해지는 값은 반드시 AL 레지스터에만 넣어야 한다
연산결과는 무조건 AX 레지스터로만 리턴된다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    PRINT_DEC 2,ax
    NEWLINE

    ; 2 * 3
    mov ax,0
    mov al,2
    mov bl,3
    mul bx

    PRINT_DEC 1,ax
    NEWLINE

    xor rax, rax
    ret
```


DIV para(1byte)
para가 1byte일 때: AX / para : AL(몫), AH(나머지)
para는 레지스터만 허용된다
나누어지는 값은 반드시 AX레지스터에만 넣어야 한다
연산결과는 무조건 AL, AH의 고정된 레지스터로만 리턴된다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    ; 7(AX)/2 = 3(AL), 1(AH)

    mov ax,7
    mov bl,2
    div bl

    mov bl,ah

    PRINT_DEC 1,al
    NEWLINE
    PRINT_DEC 1,bl
    NEWLINE
    xor rax, rax
    ret
```

디버깅 실습

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,0
    mov al,2
    mov bl,3
    mul bx

    PRINT_DEC 1,ax
    NEWLINE

    mov ax,7
    mov bl,2
    div bl
    mov bl,ah

    PRINT_DEC 1,al
    NEWLINE
    PRINT_DEC 1,bl
    NEWLINE

    xor rax, rax
    ret
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    GET_DEC 1,a
    GET_DEC 1,b

    mov ax,[a]
    mov bx,[b]
    add ax,[b]
    mov [c],word ax

    mov ax,[a]
    mov bx,[b]
    sub ax,[b]
    mov [d],byte ax

    mov ax,[a]
    mov bx,[b]
    mul bx
    mov [e],ax

    mov ax,0
    mov al,[a]
    mov bl,[b]
    div bl

    mov bl,ah
    mov [f],al
    mov [g],bl

    PRINT_DEC 1,a
    NEWLINE
    PRINT_DEC 1,b
    NEWLINE
    PRINT_DEC 1,c
    NEWLINE
    PRINT_DEC 1,d
    NEWLINE
    PRINT_DEC 1,e
    NEWLINE
    PRINT_DEC 1,f
    NEWLINE
    PRINT_DEC 1,g
    NEWLINE

    xor rax, rax
    ret

section .bss
    a resb 1 ; input param1
    b resb 1 ; input param2
    c resw 1 ; result of addition
    d resb 1 ; result of substraction
    e resw 1 ; result of multiplication
    f resb 1 ; quotient
    g resb 1 ; remains
```

