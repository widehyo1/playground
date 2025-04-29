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


SHR para1,para2 (오른쪽으로 비트 이동)
para1: 작업할 레지스터 | 메모리
para2: 오른쪽으로 이동할 비트 수(주로 4의 배수로 활용)


SHL para1,para2 (왼쪽으로 비트 이동)
para1: 작업할 레지스터 | 메모리
para2: 왼쪽으로 이동할 비트 수(주로 4의 배수로 활용)


mov ax,0x1234
;
shl ax,4 ; ax = 0x2340

mov ax,0x1234
;
shr ax,4 ; ax = 0x0123

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,0x1234

    PRINT_HEX 2,ax
    NEWLINE

    shl ax,4

    PRINT_HEX 2,ax
    NEWLINE

    mov [a],word 0x1234

    PRINT_HEX 2,a
    NEWLINE

    shr word [a],4

    PRINT_HEX 2,a
    NEWLINE

    xor rax, rax
    ret

section .bss
    a resw 1

```

AND,OR,XOR para1,para2(para1 = para1 opr para2)
para1,para2: 레지스터 | 메모리 | 상수
연산결과는 para1에 저장된다
para1,para2 모두 메모리인 경우는 연산 불가

xor: 다르면 1, 같으면 0

NOT para(para = not para, 0은 1로, 1은 0으로 변경)
para: 레지스터 | 메모리 | 상수
연산결과는 para에 저장

mov al,0xb6
mov bl,0x55

al: 0b10110110
bl: 0b01010101

and al,bl: 0b00010100 = 0x14
or  al,bl: 0b11110111 = 0xf7
xor al,bl: 0b11100011 = 0xe3
not al   : 0b01001001 = 0x49

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov al,0b10110110
    mov bl,0b01010101

    PRINT_HEX 1,al ; 0xb6
    NEWLINE
    PRINT_HEX 1,bl ; 0x55
    NEWLINE

    and al,bl
    PRINT_HEX 1,al ; 0x14
    NEWLINE

    mov al,0b10110110
    mov bl,0b01010101
    or al,bl

    PRINT_HEX 1,al ; 0xf7
    NEWLINE

    mov al,0b10110110
    not al

    PRINT_HEX 1,al ; 0x49
    NEWLINE

    xor rax, rax
    ret
```

MUL para(2byte)
para가 2byte일 때: DX: AX=AX * para
para는 레지스터만 허용된다.
연산결과는 무조건 지정된 레지스터로만 들어온다(DX:AX).

MUL para(4byte)
para가 4byte일 때: EDX: EAX=EAX * para
para는 레지스터만 허용된다.
연산결과는 무조건 지정된 레지스터로만 들어온다(EDX:EAX).

상위 숫자는 DX레지스터에 하위 숫자는 AX 레지스터로 그 결과 값이 들어온다.
DX:AX를 연결해서 4byte로 해석해서 읽어야 한다.

DX:AX
DX: 0x1234
AX: 0x5678

shl edx,16
edx: 0x12340000

and eax,0x0000ffff
eax: 0x00005678

or eax,edx
eax: 0x12345678


```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    xor rax, rax
    ret
```

:reg v
Type Name Content
  c  "v   /`/-1^MV?`?+1^M
/`/-1<CR>?`?+1<CR>
let @t = '/`/-1V?`?+1'
let @t = '/`/-1^MV?`?+1^M'
let @t = '/`/-1V?`'

nnoremap <leader>`v /`/-1<CR>V?`?+1


```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov dx,0x1234
    mov ax,0x5678
    PRINT_HEX 2,dx
    NEWLINE
    PRINT_HEX 2,ax
    NEWLINE

    shl edx,16
    PRINT_HEX 4,edx
    NEWLINE

    and eax,0x0000ffff
    PRINT_HEX 4,eax
    NEWLINE

    or eax,edx
    PRINT_HEX 4,eax
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
    mov ax,0xff12
    mov bx,0xff23

    mul bx       ; dx:ax = ax * bx
    shl edx,16
    and eax,0x0000ffff
    or eax,edx   ; eax = dx:ax

    mov [ok],eax
    PRINT_HEX 4, ok
    NEWLINE

    xor rax, rax
    ret

section .bss
    ok resd 1
```
>>> a = 0xff12
>>> b = 0xff23
>>> a
65298
>>> b
65315
>>> a * b
4264938870
>>> hex(a)
'0xff12'
>>> hex(a*b)
'0xfe35cd76'

DIV para(2byte)
para가 2byte일 때: DX:AX / para(2byte) : AX(몫), DX(나머지)
para는 레지스터만 허용된다.
나누어지는 값은 무조건 DX:AX 레지스터에만 넣어야 한다.
결과는 AX, DX의 레지스터에서만 얻을 수 있다.

eax: 0x12345678
mov edx,eax
edx: 0x12345678
shr edx,16
edx: 0x00001234

and eax,0x0000ffff
eax: 0x00005678

eax -> dx:ax

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov eax,0x12345678
    PRINT_HEX 4,eax
    NEWLINE

    mov edx,eax
    shr edx,16
    and eax,0x0000ffff

    PRINT_HEX 2,dx
    NEWLINE
    PRINT_HEX 2,ax
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
    mov eax,0x12345678
    mov bx,0x4567

    mov edx,eax
    shr edx,16
    and eax,0x0000ffff
    div bx

    mov [quotient],ax
    mov [remain],dx

    PRINT_HEX 2,quotient
    NEWLINE
    PRINT_HEX 2,remain
    NEWLINE

    xor rax, rax
    ret

section .bss
    quotient resw 1
    remain resw 1
```

>>> a = 0x12345678
>>> b = 0x4567
>>> a
305419896
>>> b
17767
>>> a // b
17190
>>> a % b
5166
>>> hex(a // b)
'0x4326'
>>> hex(a % b)
'0x142e'
>>>

연산에서 특별한 일들이 발생했는지 상태를 모니터링해주는 특별한 레지스터
플래그 레지스터(컨트롤 레지스터)

ZF(Zero Flag): 연산 결과가 Zero이면 설정됨
CF(Carry Flag): 연산에서 캐리가 발생하면 설정됨

플래그 레지스터는 프로그램에서 특별히 다른 레지스터처럼 명시적으로 사용되지는 않고
각각의 플래그 상태 값을 이용하는 다른 명령어들에서 비 명시적으로 사용된다.

TEST para1,para2
para1과 para2의 and 연산을 행하고 결과를 플래그 레지스터에 반영하라

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,0x1234
    and ax,0x0000
    PRINT_HEX 2,ax
    NEWLINE

    add ax,0x1234
    mov ax,0x1234
    test ax,0x0000
    PRINT_HEX 2,ax
    NEWLINE

    xor rax, rax
    ret
```

CMP dst, src
dst를 중심으로 src와 비교 연산을 수행한다
연산 결과는 플래그 레지스터에 저장된다
결과는 JMP 명령문과 연결되어 사용된다.

JMP 계열 명령어(플래그 레지스터의 플래그를 보고 수행됨)
JE/JNE label: 같거나/같지 않다면 label로 jump
JG/JGE label: 크거나/크지 않다면 label로 jump
JL/JLE label: 작거나/작지 않다면 label로 jump
JMP    label: label로 jump

```c
int ax = 20;
int bx = 20;
int cx;
if (ax == bx) {
    cx = 100;
} else {
    cx = 0;
}
printf("%d\n", cx);
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,20
    mov bx,20

    cmp ax,bx
    je L_equal
    mov cx,0
    jmp L_equal_end
L_equal:
    mov cx,100
L_equal_end:

    PRINT_DEC 2,cx
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
    mov ax,20
    mov bx,20

    cmp ax,bx
    je L_equal
    jmp L_not_equal
L_equal:
    mov cx,100
    jmp L_not_equal_end
L_not_equal:
    mov cx,0
L_not_equal_end:

    PRINT_DEC 2,cx
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
    mov ax,20
    mov bx,20

    cmp ax,bx
    jne L_not_equal
    mov cx,100
    jmp L_not_equal_end
L_not_equal:
    mov cx,0
L_not_equal_end:

    PRINT_DEC 2,cx
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
    mov ax,20
    mov bx,20

    cmp ax,bx
    jne L_not_equal
    L_equal:
        mov cx,100
        jmp L_not_equal_end
    L_equal_end:
    L_not_equal:
        mov cx,0
    L_not_equal_end:

    PRINT_DEC 2,cx
    NEWLINE

    xor rax, rax
    ret
```

3개의 숫자 중 가장 큰 수를 선택하는 알고리즘
```c
int a,b,c,max,min;
a = 3;
b = 4;
c = 5;
if (a < b) max = b;
else max = a;
if (max < c) max = c;

```
