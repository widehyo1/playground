- 중괄호 확장을 이용해서 slice(start,end,step) 사용 가능

```bash
~/gitclone/playground/reading $ ls {11..20..2}_*
11_LearnWindowsSubsystemForLinux:
wsl_setting.md

13_assembly_tutorial:
note.md  temp.vim

15_flent_python:
done.md  note.md

17_Understanding_compiler:
done.md  note.md

19_woowahan_typescript_and_react:
a.py  note.md  test.ts
```

`cmd << text`
text와 동일한 라인까지의 셸 스크립트 내용이 cmd에 대한 표준 입력이 된다(here document).
입력은 키보드로 타이핑하거나 셸 프로그램으로 받을 수 있다. 대개 cat, ex, sed 같은 명령들이
이 문법을 사용한다. (만약 <<-가 사용되면 히어 도큐먼트 앞부분의 탭들은ㄴ 제거되며,
그 탭들은 text의 입력 종료 표시와 입력을 비교할 때 무시쇤다.

`cmd <<< word`
뉴라인이 뒤에 붙은 word의 텍스트를 cmd의 입력으로 제공한다(here string)

`cmd <> file`
표준 입력에 읽고 쓰는 file을 연다. 파일 내용은 훼손되지 않는다.

`cmd >&n`
cmd 출력을 파일 디스크립터 n으로 보낸다

`cmd m>&n`
cmd의 파일디스크립터 m의 출력을 파일 디스크립터 n으로 보낸다

`cmd > file 2>&1`
표준 출력과 표준 에러를 file로 보낸다(= `cmd >& file` = `cmd &> file`)

특수 파일명

/dev/stdin == file descriptor 0
/dev/stdout == file descriptor 1
/dev/stderr == file descriptor 2
/dev/fd/<n> == file descriptor n

/dev/tcp/<host>/<port>
배시는 호스트명이나 IP 주소로 된 <host>와 <port> 포트에 TCP 연결을 열고, 리디렉션에 그 파일 서술자를 사용한다.

/dev/udp/<host>/<port>
배시는 호스트명이나 IP 주소로 된 <host>와 <port> 포트에 UDP 연결을 열고, 리디렉션에 그 파일 서술자를 사용한다.


diff -u <(sort file1) <(sort file2) | less


```bash
~/gitclone/playground/reading/42_bash_pocket_reference $ echo $a
/home/widehyo/gitclone/playground/reading/42_bash_pocket_reference
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a#*/}
home/widehyo/gitclone/playground/reading/42_bash_pocket_reference
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a##*/}
42_bash_pocket_reference
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a%*/}
/home/widehyo/gitclone/playground/reading/42_bash_pocket_reference
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a%%*/}
/home/widehyo/gitclone/playground/reading/42_bash_pocket_reference
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a#/*}
home/widehyo/gitclone/playground/reading/42_bash_pocket_reference
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a##/*}

~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a%/*}
/home/widehyo/gitclone/playground/reading
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${a%%/*}

~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${PWD%/*}
/home/widehyo/gitclone/playground/reading
~/gitclone/playground/reading/42_bash_pocket_reference $ echo ${PWD##*/}
42_bash_pocket_reference
```

내장 셸 변수
$#: 명령 라인 인자의 개수
$-: (명령 라인에서 제공됐거나 set로 제공된) 현제 유효한 옵션들이다. 셸은 일부 옵션을 자동으로 설정한다.
$?: 마지막 실행 명령의 exit code
$$: 셸의 프로세스 번호
$!: 마지막 백그라운드 명령의 프로세스 번호
$0: 첫 번째 단어이며, 이는 명령 이름이다. PATH 검색을 통해 명령을 찾았다면 이 값은 전체 경로명을 포함한다
$n: 명령 라인의 개별 인자들이다(위치 파라미터). 본 셸은 9개의 파라미터만을 직접 참고하도록 호용한다(n=1-9). ${n}으로 지정되었다면 9보다 큰 n을 허용한다
$*, $@: 명령 라인의 모든 인자들이다($1 $2 ...)
"$*": 한 문자열로 된 명령 라인의 모든 인자들이다("$1 $2 ..."). $IFS의 첫 문자로 값들을 구분한다.
"$@": 각각 쿼팅된 명령 라인의 모든 인자들이다("$1" "$2" ...)



```bash
~/gitclone/playground/reading/42_bash_pocket_reference $ echo $BASHOPTS
checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:globasciiranges:histappend:interactive_comments:progcomp:promptvars:sourcepath
~/gitclone/playground/reading/42_bash_pocket_reference $ !! | tr : '\n'
echo $BASHOPTS | tr : '\n'
checkwinsize
cmdhist
complete_fullquote
expand_aliases
extglob
extquote
force_fignore
globasciiranges
histappend
interactive_comments
progcomp
promptvars
sourcepath

~/gitclone/playground/reading/42_bash_pocket_reference $ echo $SHELLOPTS
braceexpand:emacs:hashall:histexpand:history:interactive-comments:monitor
~/gitclone/playground/reading/42_bash_pocket_reference $ !! | tr ':' '\n'
echo $SHELLOPTS | tr ':' '\n'
braceexpand
emacs
hashall
histexpand
history
interactive-comments
monitor
```
