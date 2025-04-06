기본적인 내용을 학습한 다음에는 무엇을 배워야 할까? 이 질문의 답은 '팁'이다.
팁은 특정 문제를 해결하기 위한 조리법이다. 눈앞의 문제는 풀었지만 최적의 해결책이 아니란 기분이 들 때, 여러분은 그 문제를 해결하는 팁을 검색해볼 것이다. ... 하지만 이 전략의 단점은 학습이 느리다는 것이다. 커서 밑에 있는 단어를 검색하기 위해서 * 명령을 사용하는 방법을 배우면 유용하기야 하겠지만 이것이 Vim 숙련자처럼 생각하도록 해주는 데에는 도움이 되지 않는다.


이 책은 각 내용에 따른 기법을 사용해서 해결책을 제시한다. 그 기법을 읽는 것으로 끝내지 말고 매일 직면하는 무제와 어떤 점이 유사한지 찾기 위해 노력해야 한다. 그러한 노력이 결과적으로는 당신의 시간을 아껴줄 것이다.

Vim 버전은 Vim 7.4.110 버전 이상(gn 도입)

vim -u NONE -N
: vimrc 파일을 사용하지 않고 실행

최소조건:
vim -u code/essential.vim

```vim
" essential.vim
set nocompativle
filetype plugin on
```

:script로 확인!

:version으로 feature 확인

. 반복 예제는 간단하게 A;
j.j. 세미콜론 추가하기로 보이자

대상은 js파일

@:를 이용한 Ex명령 반복하기가 가능한 이유:
특수 레지스터 중 ":"에 대하여

```
var tpl = [
    '<a href="{url}">{title}</a>'
]
```

```
console.log([{'a':1},{'b':2}])
```

```
<table>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
  </tr>
</table>
```

```
<table>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
  </tr>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
  </tr>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
  </tr>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
  </tr>
  <tr>
    <td>Symbol</td>
    <td>Name</td>
  </tr>
</table>
```


P와 gP 명령 모두 붙여넣기 동작을 수행하지만 붙여넣기 후에 커서의 위치에 차이가 있다.
P 명령은 붙여넣은 내용이 시작하는 위치에 커서를 둔다. 위 예제에서 사용한 gP 명령은 복제 후에 커서를 붙여넣은 본문 끝 즉, 두 번째 위치에 놓기 때문에 붙여넣은 후에도 필요한 내용을 편리하게 수정할 수 있을 것이다.


```
1. one
2. two
3. three
4. four
5. five
6. six
7. vesen
8. eight
9. nine
10. ten
11. eleven
```

```
1) One
2) Two
3) Three
4) Four
5) Five
6) Six
7) Seven
8) Eight
9) Nine
10) Ten
11) Eleven
```

put 0

g&

아무거나 치환한 후 g& 로 모두 찾아바꾸기

'<,'>s/)/asdf/g
g&




UserK@Win11-01 MINGW64 /c/Windows/System32
$ ls PATHPING.EXE
PATHPING.EXE*

UserK@Win11-01 MINGW64 /c/Windows/System32
$ ls PATHPING.EXE | clip

UserK@Win11-01 MINGW64 /c/Windows/System32
$ powershell -command Get-Clipboard
PATHPING.EXE*


UserK@Win11-01 MINGW64 /c/Windows/System32
$

read !powershell -command Get-Clipboard


system("


read !powershell -command Get-Clipboard
read !powershell -command Get-Clipboard
read !powershell -command Get-Clipboard


call system('clip', @0)
read !powershell -command Get-Clipboard


system("


read !powershell -command Get-Clipboard
read !powershell -command Get-Clipboard
read !powershell -command Get-Clipboard


call system('clip.exe', @0)
read !powershell -command Get-Clipboard
call system('clip.exe', @0)

wsl, git bash 공용
read !powershell.exe -command Get-Clipboard
call system('clip.exe', @0)

:read !powershell.exe -command Get-Clipboard
:call system('clip.exe', @0)

