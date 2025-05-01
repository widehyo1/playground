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
let @t = '/`/-1V?`?+1'
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

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    mov rbp, rsp; for correct debugging
    ;write your code here

    PRINT_STRING input_msg
    GET_DEC 2,a
    NEWLINE
    PRINT_STRING input_msg
    GET_DEC 2,b
    NEWLINE
    PRINT_STRING input_msg
    GET_DEC 2,c
    NEWLINE

    mov ax,[a]

    ; prepare new variable b
    mov bx,[b]

    mov [max],ax ; init max value
    cmp bx,ax ; compare with max value and b
    jg L_bx_gt1 ; set max value
    
L_cmp1:

    mov [min],ax ; init min value
    cmp bx,ax ; compare with min value and b
    jl L_bx_lt1 ; set min value

L_cmp2:
    ; prepare new variable c
    mov bx,[c]

    mov ax,[max]
    cmp bx,ax ; compare with max value and c
    jg L_bx_gt2 ; set max value

L_cmp3:

    mov ax,[min]
    cmp bx,ax ; compare with min value and c
    jl L_bx_lt2 ; set min vlaue

L_cmp4:
    PRINT_STRING max_msg
    PRINT_DEC 2,max
    NEWLINE

    PRINT_STRING min_msg
    PRINT_DEC 2,min
    NEWLINE

    ; res = max * min
    mov ax,[max]
    mov bx,[min]

    mul bx
    shl edx,16
    and eax,0x0000ffff
    or  eax,edx
    mov [res],eax

    PRINT_STRING total_msg
    PRINT_DEC 4,res
    NEWLINE

    xor rax, rax
    ret

L_bx_gt1:
    mov [max],bx ; update max
    jmp L_cmp1

L_bx_lt1:
    mov [min],bx ; update min
    jmp L_cmp2

L_bx_gt2:
    mov [max],bx ; update max
    jmp L_cmp3

L_bx_lt2:
    mov [min],bx ; update min
    jmp L_cmp4

section .data
    input_msg db 'input number:',0x00
    max_msg db 'max:',0x00
    min_msg db 'min:',0x00
    total_msg db 'max * min = ',0x00

section .bss
    a resw 1
    b resw 1
    c resw 1
    max resw 1
    min resw 1
    res resd 1
```

반복문
MOV ECX, 반복횟수
라벨:
  <<반복되는 내용>>
LOOP 라벨

반복 블록 내에서 ECX 레지스터는 절대 사용금지
LOOP 라벨 명령어에 도착하면 ECX 값을 1 감소시키고, 만약 ECX 값이 0이면 블록을 종료하고, 그렇지 않으면 라벨에서부터 다시 실행된다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,0
    mov cx,10
L1:
    add ax,cx
    loop L1

    PRINT_DEC 2,ax
    NEWLINE

    xor rax, rax
    ret
```

INC para
para: 1 더할 곳의 주소(레지스터, 메모리)

DEC para
para: 1 감소시킬 곳의 주소(레지스터, 메모리)

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,0
    mov bx,1
    mov cx,10
L1:
    add ax,bx
    inc bx
    loop L1

    PRINT_DEC 2,ax
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
    mov ax,0
    mov bx,0
L1:
    add ax,bx
    inc bx
    cmp bx,10
    jle L1

    PRINT_DEC 2, ax
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
    mov ax,0
    mov bx,0
L1:
    cmp bx,10
    jg L2
    add ax,bx
    inc bx
    jmp L1
L2:
    PRINT_DEC 2,ax
    NEWLINE

    xor rax, rax
    ret
```

초기 값이 있는 배열 변수 선언

section .data에서 선언
<변수이름> <데이터타입> <배열 개수만큼의 값>
<변수이름> TIMES <변수개수> <데이터타입> <초기값>

초기 값이 없는 배열 변수 선언
section .bss에서 선언
<변수이름> <예약 데이터 타입> <배열 개수>

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov eax,a
    PRINT_HEX 4,eax ; 403044
    NEWLINE

    mov eax, [a]
    PRINT_HEX 4,eax ; 4614321e <- 값으로 표현되는 수
    NEWLINE

    xor rax, rax
    ret

section .data
    a db 30,50,20,70,60 ; 1E,32,14,46,3C <- 실제 저장되어 있는 메모리, 리틀엔디언
    b times 5 dw 0 ; 0000 0000 0000 0000 0000
    a1 dw 0x1234,0x5678,10 ; 3412 7856 9A00

section .bss
    c resb 3
    d resw 4

```


인덱스로 배열 요소에 접근할 때 주의점

반드시 메모리값으로 접근한다
접근 주소 = 시작 주소(변수 이름 또는 시작 주소를 가지고 있는 4byte 레지스터 이름) + 배열인덱스 * 데이터타입 바이트 크기

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov al,[a]
    PRINT_DEC 1,al
    NEWLINE

    mov al,[a+1] ; a+1*1
    PRINT_DEC 1,al
    NEWLINE

    mov ax,[a1]
    PRINT_HEX 2,ax
    NEWLINE

    mov ax,[a1+1] ; bug
    PRINT_HEX 2,ax
    NEWLINE

    mov ax,[a1+2] ; bug
    PRINT_HEX 2,ax
    NEWLINE

    xor rax, rax
    ret

section .data
    a db 30,50,20,70,60 ; 1E,32,14,46,3C
    b times 5 dw 0 ; 0000 0000 0000 0000 0000
    a1 dw 0x1234,0x5678,10 ; 3412 7856 9A00

section .bss
    c resb 3
    d resw 4

```


```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov eax,0
    mov ecx,3
L1:
    mov ebx, [my + eax*2]
    mov [you + eax*2],ebx
    inc eax
    loop L1

    ; print you[3]
    mov edx,you
    mov eax,0
L2:
    PRINT_HEX 2,[edx+eax*2]
    NEWLINE
    inc eax
    cmp eax,3
    jl L2

    xor rax, rax
    ret

section .data
    my dw 0x1234,0x4567,0x1133 ; 34 12 67 45 33 11
section .bss
    you resw 3
```


ECX 레지스터에 반복 횟수를 넣고 LOOP 문으로 반복을 구현하는 문법 사용 시 유의해야 하는 것이 있는데 반복 블록 내에서는 PRINT 계역의 매크로 함수(io64.inc)를 사용할 수 없다는 것이다. PRINT 계역의 매크로 함수 내부에서 사용하는 라벨의 범위와 LOOP 명령어에서 사용하는 라벨의 범위가 충돌하기 때문이다. ... 이런 경우 DO WHILE 문장을 사용해서 구현하여 동일한 목표를 달성할 수 있다.

```
my1[3](W)={0x1234,0x4567,10};
you1[3](W);
edx;
edx=0;
for(ecx=3;0<ecx;ecx--) {
    eax = my1[edx];
    you1[edx]=eax;
    edx++;
}
edx=0;
do{
    print(my1[edx])
    edx++;
}while(edx < 3);
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov eax,my1
    mov ebx,you1

    mov edx,0
    mov ecx,3
L1:
    mov eax, [my1+edx*2]
    mov [you1+edx*2],eax
    inc edx
    loop L1

    mov edx,0
L2:
    PRINT_HEX 2,my1+edx*2
    NEWLINE
    inc edx
    cmp edx,3
    jl L2

    xor rax, rax
    ret

section .data
    my1 dw 0x1234,0x4567,10

section .bss
    you1 resw 3
```


임의의 숫자를 입력받아(2byte 크기) 1에서부터 그 숫자까지 3의 배수만 선택하여 모두 배열에 저장하고 그 개수와 값을 각각 출력하라.
저장된 모든 수의 합을 구하여 출력하라.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    PRINT_STRING msg_input
    GET_DEC 2,input
    NEWLINE

    mov [count],0
    mov [total],0
    mov cx,1 ; temporary variable
L1:
    mov ax,cx
    mov bx,3
    div bx ; dx:ax with ax(quotient), dx(remain)
    cmp dx,0
    je L_target
    jmp L_target_end
L_target:
    mov [arr + 2 * count],cx
    inc count
L_target_end:
    inc cx
    cmp input,cx
    jge L1

    PRINT_STRING msg_count
    PRINT_DEC 2,count
    NEWLINE

    cmp count,0
    jg L_print_arr
    jmp L_print_arr_end

L_print_arr:
    mov cx,[count]
    mov bx,0
L_print:
    mov ax,[total]
    mov dx,[arr + 2 * bx]
    add ax,dx
    mov [total],ax
    PRINT_DEC 2,dx
    NEWLINE
    inc bx
    dec cx
    cmp cx,0
    jne L_print
L_print_arr_end:
    PRINT_STRING msg_total
    PRINT_DEC 2,total
    NEWLINE

    xor rax, rax
    ret

section .data
    msg_input db '# input max number:',0x00
    msg_count db '# number count:',0x00
    msg_total db '# total:',0x00
section .bss
    input resw 1
    count resw 1
    total resw 1
    arr resw 100

```


DIV para(2byte)
para가 2byte일 때: DX:AX / para(2byte) : AX(몫), DX(나머지)
para는 레지스터만 허용된다.
나누어지는 값은 무조건 DX:AX 레지스터에만 넣어야 한다.
결과는 AX, DX의 레지스터에서만 얻을 수 있다.

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
    mov rbp, rsp; for correct debugging
    ;write your code here
    PRINT_STRING msg_input
    GET_DEC 2,input
    NEWLINE

    mov [count],word 0
    mov [total],word 0
    mov cx,1 ; temporary variable
L1:
    mov ax,cx
    mov bl,3
    div bl ; dx:ax with ax(quotient), dx(remain)
    cmp ah,0
    je L_target
    jmp L_target_end
L_target:
    mov edx,[count]
    mov [arr + 2 * edx],cx
    mov ax,dx
    add ax,1
    mov [count],ax

L_target_end:
    inc cx
    mov ax,[input]
    cmp ax,cx
    jge L1

    PRINT_STRING msg_count
    PRINT_DEC 2,count
    NEWLINE
    
    mov eax,[count]
    cmp eax,0
    jg L_print_arr
    jmp L_print_arr_end

L_print_arr:
    mov cx,[count]
    mov ebx,0
L_print:
    mov ax,[total]
    mov dx,[arr + 2 * ebx]
    add ax,dx
    mov [total],ax
    PRINT_DEC 2,dx
    NEWLINE
    inc bx
    dec cx
    cmp cx,0
    jne L_print
L_print_arr_end:
    PRINT_STRING msg_total
    PRINT_DEC 2,total
    NEWLINE

    xor rax, rax
    ret

section .data
    msg_input db '# input max number:',0x00
    msg_count db '# number count:',0x00
    msg_total db '# total:',0x00
section .bss
    input resw 1
    count resw 1
    total resw 1
    arr resw 100

```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    mov ax,10
    call MyShow

    xor rax, rax
    ret

MyShow:
    PRINT_STRING msg1
    NEWLINE
    ret

section .data
    msg1 db 'haha',0x00
```

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    GET_DEC 2,ax
    GET_DEC 2,bx

    call MyCheck

    PRINT_DEC 2,ax
    NEWLINE

    xor rax, rax
    ret

MyCheck: ; inpupt: ax,bx return: ax
    cmp ax,bx
    jl L_less
    add ax,bx
    jmp L_less_end
L_less:
    sub ax,bx
L_less_end:
    ret
```

프로시저의 선언은 section .text에서 선언하고, section .text 내에서 호출(call)한다. 프로시저가 끝나는 부분은 항상 ret 명령어를 사용하는데, 이것은 명령어의 흐름을 call했던 다음 라인으로 보내는 일종의 특수한 jmp문이라고 생각하면 된다.
section .data, section .bss 등에 있는 변수들은 모든 프로시저에서 접근 가능하며 공유된다.
라벨의 이름은 모든 프로시저에서 인식되는 전역 범위이기 때문에 동일한 이름의 라벨이 2개 이상 프로시저 내에 존재할 수 없다.


Pointer Registers
- Instruction Pointer(IP)
  - 다음에 수행한 명령어가 있는 곳의 주소값을 저장
  - CPU가 관리함
- Stack Pointer(SP)
  - 현재 스택의 Top값의 주소를 저장
  - 주로 CPU가 관리하고, 프로그래머가 변경해야 하는 경우도 있음
- Base Pointer(BP)
  - 프로그래머가 계산 중 주소를 저장하기 위한 용도
  - 프로시저의 파라미터 접근 등에 사용됨


64bit 어셈블러 모드에서
스택에 자료 넣기
PUSH para: para는 넣고자 하는 자료값으로 2byte 또는 8byte 크기 상수값 또는 레지스터
- para가 상수인 경우는 크기를 명시적으로 표시
(push word 0x12, push qword 0x1234)

스택에서 자료 빼기
POP para: para는 저장된 자료를 받을 곳 2byte 또는 8byte 크기의 레지스터 또는 메모리
para가 메모리인 경우는 크기를 명시해야 함
(pop word [a], pop qword [b])

32bit 어셈블러 모드에서
스택에 자료 넣기
PUSH para: para는 넣고자 하는 자료값으로 2byte 또는 4byte 크기 상수값 또는 레지스터
- para가 상수인 경우는 크기를 명시적으로 표시
(push word 0x12, push dword 0x1234)

스택에서 자료 빼기
POP para: para는 저장된 자료를 받을 곳 2byte 또는 4byte 크기의 레지스터 또는 메모리
para가 메모리인 경우는 크기를 명시해야 함
(pop word [a], pop dword [b])


스택은 메모리의 영역에서 미리 예약되어 있는 일정 크기의 특별한 배열 변수라고 생각하면 쉽다. 이 배열은 마지막 인덱스부터 앞쪽으로 오면서(주소의 높은 쪽에서 낮은 쪽으로) 사용한다. PUSH 연산은 뒤쪽에서 앞쪽으로(높은 주소에서 낮은 주소로) 이루어지고, POP은 그 반대 방향으로 연산이 진행된다. 또 요소크기의 기본 단위는 64bit 모드인 경우는 2byte 또는 8byte이며, 32bit 모드일 때는 2byte 또는 4byte이다. 그리고 현재 어떤 인덱스(주소)까지 작업했는지를 기억하기 위해 특별한 레지스터를 사용하는데, 이 레지스터가 RSP(stack pointer) 레지스터이다. 이런 이유로 PUSH 연산을 수행하면 RSP 값(주소)은 데이터의 크기만큼 감소한다. POP의 경우는 데이터의 크기만큼 증가한다.

```asm
%include "io64.inc"

section .text
global CMAIN
CMAIN:
    ;write your code here
    GET_DEC 2,ax
    GET_DEC 2,bx

    ; push ax
    ; push bx
    call MyCheck

    PRINT_DEC 2,ax
    NEWLINE
    ; pop bx
    ; pop ax

    PRINT_DEC 2,ax
    NEWLINE

    xor rax, rax
    ret

MyCheck: ; inpupt: ax,bx return: ax
    cmp ax,bx
    jl L_less
    add ax,bx
    jmp L_less_end
L_less:
    sub ax,bx
L_less_end:
    ret
```


