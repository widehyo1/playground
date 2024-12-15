# teminal-vim

## 발표내용

### 0. introduction
- 소개
  - vim 사용 경험(2021~)
  - practical-vim 정독 3회 +\alpha
  - vim user, nvim 입문 진행 중
  - 주 업무: java web 개발, 최근 python 개발 중

### 0. introduction
- 경험
  - 2년간 공공기관 내부에 위치한 사무실에서 근무
    - 소스 작업 및 배포 주 근무 환경: 내부망 (인트라넷 only) + 노트북(외부망)
    - 노트북에서 작업한 코드를 내부망으로 옮기려면
      - 사무실 내 외부망 컴퓨터로 코드 이전
      - 망연계 시스템 프로그램을 이용하여 소스 파일 전송(외부망->내부망)
    - 외부망에서 작업한 코드가 내부망에서 동작하지 않는 현상 다수 목격
    - 운영 서버는 공공기관 소유 VM, 발급된 인증서를 이용해 접속

### 0. introduction
- 제약
  - 인터넷은 사용할 수 없다(폐쇄망)
    - 지금까지 접한 모든 상용서버는 폐쇄망
    - 인터넷 망에서 잘 돌던 코드가 상용서버에서만 제대로 동작하지 않는데
      그 이유가 코드 내부에서 인터넷을 사용(ex. cdn)하기 때문이라면
  - 내 마음에 드는 도구를 설치할 수 없다(내 소유가 아닌 서버)
    - 각종 2세대 utility: lsd, bat, fzf, sysz
    - neovim
    - 심지어는 git(미설치된 상용서버를 본 적이 있다)

### 0. instroduction
- 결론
  - 모든 작업환경에서 공통적으로 사용할 수 있는 기술에 집중(기본제공 명령어)
  - 최소한의 공통분모: bash와 vim
  - posix 표준 utility 명령어(coreutils)
    - dpkg -L coreutils, rmp -ql coreutils, pacman -Ql coreutils, brew list coreutils, ...
    - 참고자료 (IEEE Std 1003.1-2017 utility 문서):
      - https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html
  - plugin과 cli tool을 설치에 대한 강한 저항(어차피 서버에서 못쓰는데)
    - 생산성의 현저한 증가를 가져오는 경우에만 설치(nerdtree, vimium C)

### 1. 왜 터미널인가
- 왜 터미널인가
  - 터미널에 수렴한 과정
    - 1. 자바스크립트
      - 내 마음대로 동작하지 않는 코드
      - 코드는 작성 후 동작 확인하려면 로컬환경을 구동 또는 브라우저 sandbox 이용
      - nodejs > 내가 작성한 로직만 빠르게 테스트 가능
  - 상용 서버에서 사용 가능한 환경이 터미널 밖에 없다(GUI 제공 X, IDE 제공 X)
  - 배포 작업 중 발생한 오류를 해결해야 한다

- 터미널의 장점
  - 빠르다
  - 작성 코드의 가장 빠른 피드백 제공
  - 인터넷 없이 동작 가능하다
  - 디버깅에서 런타임환경을 직접 볼 수 있다

- shell의 장점
  - 기록이 남는다 따라서 재현 가능하다(reproducible)
  - history를 사용할 수 있다
  - 목적하는 명령어를 한번만 실행하면 그 이후는 반복할 수 있다
    - alias를 이용하여 개인용 cli tool을 직접 만들어 사용 가능
    - export를 이용하여 원하는 환경변수 설정 및 활용 가능
  - stdin, stdout, pipe의 기능이 강력하다
  - text를 다루는데 특화된 도구가 내장되어 있다(cat, echo, sed, awk, grep 등)
  - systemcall에 특화되어 있다 (파일시스템: mv, cp, rm)

### 2. terminal-vim 토글하기(vim)
- terminal-vim 토글하기(vim)
  - vim에는 :sh로 내장 shell을 실행시킬 수 있음(!명령과는 다르다 !와는)
  - :sh로 진입한 터미널 디렉터리 path는 :pwd로 확인 가능
  - vim의 :pwd는 :cd를 이용하여 변경가능, 해당 기능은 nerdtree가 지원
  - 다시 돌아오는 법: <C-d> (terminal -> vim)
  - 위의 동작 중 history 변경 없음(history 사용 가능)
    - 예시: 직전 명령 수행(!!)
  - <C-d>를 terminal-vim간 토글키로 사용하는 방법
    - nnoremap <C-D> :sh<CR> "(vim -> terminal) in .vimrc

### 2. terminal-vim 토글하기(vim)
- 실행 예시
  - python
    [image]
  - java <- maven 이용해서 한번만 실행하면 된다고 한거 보여주기 alias or !!
    [image]
  - nodejs
    [image]
  - c <- make 이용해서
    [image]
  - cpp <- makefile 이용해서
    [image]
  - c# <- mcs 이용해서
    [image]
  - lua
    [image]

- 특히 REPL을 제공하는 경우 python, nodejs, haskell, lua <C-d>의 위력 설명


### 3. terminal-vim 토글하기(neovim)
- terminal-vim 토글하기(neovim)
  - nvim에는 :sh이 없음
  - terminal에서는 프로세스를 control하는 단축키들이 있다
    - 프로세스 끝내기 terminate process(SIGINT) <C-c>
    - 입력이 끝났음(EOF)을 알리기 <C-d> (interactive shell에서 유용)
    - 프로세스 중단하기 <C-z> (foreground process를 suspend, 관리 영역이 job control로 넘어감)
  - nvim에서 <C-z>를 눌러보자

### 3. terminal-vim 토글하기(neovim)
  - [image]
  - 터미널로 돌아온 상태
  - suspend된 process 조회: jobs
  - 다시 돌아오려면? fg
  - 그럼 <C-z>를 fg로 설정하면 될까? 굉장히 부담됨

### 3. terminal-vim 토글하기(neovim)
  - 적당한 단축키 찾기의 시작
  - 그런데, <C-z>는 어디에서 설정된 키일까
    - stty -a
    - [image]
  - 그런데, 커맨드라인 작성시 잘 활용하는 <C-a>, <C-e>, <C-n>, <C-p>는 stty -a에 없던데?
    - bind -p
    - 기본키를 피하자 <- 디폴트로 바인딩된 키 목록 조회
    - bind -p | grep -v "^#" | cut -d: -f1 | sort | uniq | nl
    - bind -p | grep -v "^#" | cut -d: -f1 | sort | uniq | nl | grep "C-x"
    [image]
    - bind -p 에서 <C-x>를 일종의 leader key로 사용하고 있는 것 확인
    - 적당한 단축키를 <C-x><C-x>로 설정
    - bind '"\C-x\C-x": "fg\n"' # in .bashrc

### 3. terminal-vim 토글하기(neovim)
  - [demo gif] toggle terminal-vim
  - happy?
  - no!
  - history를 이용한 반복이 방해받음
  - bash 설정 중 특정 명령어가 history를 어지럽히지 않게 하는 설정이 있다.
  - man bash | grep -A 5 "       HISTIGNORE"
  - solution: export HISTIGNORE="fg:"

### 3. terminal-vim 토글하기(neovim)
  - [image]
  - [demo gif]

### solution
export HISTIGNORE="fg:"


-------


20369  2024-12-14_12:08:41 curl https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html > ieee_1003.1-2017_utilities.html
20370  2024-12-14_12:08:45 cat ieee_1003.1-2017_utilities.html
20388  2024-12-14_12:26:26 cat ieee_1003.1-2017_utilities.html | grep href
20388  2024-12-14_12:26:26 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }'
20388  2024-12-14_12:26:26 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq
20394  2024-12-14_12:28:46 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc
20394  2024-12-14_12:28:46 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-30
20395  2024-12-14_12:28:50 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-29
20396  2024-12-14_12:28:54 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-34
20397  2024-12-14_12:28:56 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-36
20398  2024-12-14_12:28:58 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-37
20399  2024-12-14_12:28:59 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-38
20400  2024-12-14_12:29:01 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c1-39
20401  2024-12-14_12:29:08 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c38-
20402  2024-12-14_12:29:46 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed -n 's/.html*$//p'
20403  2024-12-14_12:29:51 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed -n 's/.html*$//'
20404  2024-12-14_12:30:00 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed -n 's/.html//'
20405  2024-12-14_12:30:08 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html//'
20406  2024-12-14_12:30:20 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html*$//'
20407  2024-12-14_12:30:36 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html#tag.*$//'
20408  2024-12-14_12:30:54 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html*$//' > commands.txt
20409  2024-12-14_12:30:58 cat commands.txt
20410  2024-12-14_12:31:09 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html*$//'
20411  2024-12-14_12:31:15 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html#tag.*$//'
20412  2024-12-14_12:31:20 cat ieee_1003.1-2017_utilities.html | grep href | awk -F_ 'NF=2{ print $0 }' | sort | uniq | grep disc | cut -c39- | sed 's/.html#tag.*$//' > commands.txt


20452  2024-12-14_16:10:02 bind -p
20453  2024-12-14_16:10:12 bind -p | grep -v #
20454  2024-12-14_16:10:17 bind -p | grep -v "#"
20455  2024-12-14_16:10:21 bind -p | grep -v "^#"
20456  2024-12-14_16:10:38 bind -p | grep -v "^#" | cut -d: -f1
20457  2024-12-14_16:10:41 bind -p | grep -v "^#" | cut -d: -f1 | sort
20458  2024-12-14_16:10:45 bind -p | grep -v "^#" | cut -d: -f1 | sort | uniq
20459  2024-12-14_16:11:21 bind -p | grep -v "^#" | cut -d: -f1 | sort | uniq | nl
20460  2024-12-14_16:12:01 bind -p | grep -v "^#" | cut -d: -f1 | sort | uniq | nl | grep "C-x"



```bash
~ took 11s ❯ echo $HISTIGNORE


~ ❯ echo $HISTCONTROL
ignoreboth

~ ❯ man bash
       HISTIGNORE
              A  colon-separated  list of patterns used to decide which command lines should be saved on the history list.  Each pattern is anchored at the beginning of the line and must match the complete line (no implicit `*' is
              appended).  Each pattern is tested against the line after the checks specified by HISTCONTROL are applied.  In addition to the normal shell pattern matching characters, `&' matches the previous history line.  `&' may
              be escaped using a backslash; the backslash is removed before attempting a match.  The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value
              of HISTIGNORE.  The pattern matching honors the setting of the extglob shell option.

~ ❯ history | tail
19645  2024-12-10_10:18:30 vi
19646  2024-12-10_10:37:54 :q
19647  2024-12-10_10:37:56 exit
19648  2024-12-10_10:38:45 man bash
19649  2024-12-10_10:40:16 echo $HISTIGNORE
19650  2024-12-10_10:40:41 echo $HISTCONTROL
19651  2024-12-10_10:41:06 virc
19652  2024-12-10_10:42:45 exit
19653  2024-12-10_10:42:56 history
19654  2024-12-10_10:43:11 history | tail

~ ❯ fg
-bash: fg: current: no such job

~ ❯ history | tail
19645  2024-12-10_10:18:30 vi
19646  2024-12-10_10:37:54 :q
19647  2024-12-10_10:37:56 exit
19648  2024-12-10_10:38:45 man bash
19649  2024-12-10_10:40:16 echo $HISTIGNORE
19650  2024-12-10_10:40:41 echo $HISTCONTROL
19651  2024-12-10_10:41:06 virc
19652  2024-12-10_10:42:45 exit
19653  2024-12-10_10:42:56 history
19654  2024-12-10_10:43:11 history | tail

~ ❯ fg
-bash: fg: current: no such job

~ ❯ !!
history | tail
19645  2024-12-10_10:18:30 vi
19646  2024-12-10_10:37:54 :q
19647  2024-12-10_10:37:56 exit
19648  2024-12-10_10:38:45 man bash
19649  2024-12-10_10:40:16 echo $HISTIGNORE
19650  2024-12-10_10:40:41 echo $HISTCONTROL
19651  2024-12-10_10:41:06 virc
19652  2024-12-10_10:42:45 exit
19653  2024-12-10_10:42:56 history
19654  2024-12-10_10:43:11 history | tail

~ ❯ echo $HISTIGNORE
fg:

ai-agent/playground/playground on  gpt-analysis:feature/gpt-analysis [!?] via 🐍 v3.10.12 (playground-py3.10) ❯ nvim

[1]+  Stopped                 nvim

ai-agent/playground/playground on  gpt-analysis:feature/gpt-analysis via 🐍 v3.10.12 (playground-py3.10) took 50s ✦ ❯ python __init__.py
Traceback (most recent call last):
  File "/mnt/d/gitclone/ai-agent/playground/playground/__init__.py", line 6, in <module>
    from playground.database.base import (
ModuleNotFoundError: No module named 'playground'

ai-agent/playground/playground on  gpt-analysis:feature/gpt-analysis [!?] via 🐍 v3.10.12 (playground-py3.10) ✦ ❯ fg
nvim

[1]+  Stopped                 nvim

ai-agent/playground/playground on  gpt-analysis:feature/gpt-analysis [!?] via 🐍 v3.10.12 (playground-py3.10) took 15s ✦ ❯ !!
python __init__.py
[INFO] '__init__.py is executed'
```

```bash
content_base/java/demo on  main [?] is 📦 v1.0-SNAPSHOT via ☕ v11.0.25 took 2s ❯ java --version
openjdk 11.0.25 2024-10-15
OpenJDK Runtime Environment (build 11.0.25+9-post-Ubuntu-1ubuntu122.04)
OpenJDK 64-Bit Server VM (build 11.0.25+9-post-Ubuntu-1ubuntu122.04, mixed mode, sharing)
```

```bash
mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-quickstart
sed -i "s/compiler.release>17/compiler.release>11/" pom.xml # default java version for maven-archetype-quickstart is 17.
mvn clean package exec:java -Dexec.mainClass="com.widehyo.App" | sed -n '/exec-maven-plugin/,/Finished at/p'
```

```log
content_base/java/demo on  main [?] is 📦 v1.0-SNAPSHOT via ☕ v11.0.25 ❯ mvn clean package exec:java -Dexec.mainClass="com.widehyo.App" | sed -n '/exec-maven-plugin/,/Finished at/p'
[INFO] --- exec-maven-plugin:3.5.0:java (default-cli) @ demo ---
Hello World!
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.958 s
[INFO] Finished at: 2024-12-14T19:24:18+09:00
```

```bash
content_base/java/demo on  main [?] is 📦 v1.0-SNAPSHOT via ☕ v11.0.25 took 2s ❯ java --version
openjdk 11.0.25 2024-10-15
OpenJDK Runtime Environment (build 11.0.25+9-post-Ubuntu-1ubuntu122.04)
OpenJDK 64-Bit Server VM (build 11.0.25+9-post-Ubuntu-1ubuntu122.04, mixed mode, sharing)
```


mvn clean package exec:java -Dexec.mainClass="com.widehyo.App" | sed -n '/exec-maven-plugin/,/Finished at/p'

content_base/java/demo on  main [?] is 📦 v1.0-SNAPSHOT via ☕ v11.0.25 ❯ !mvn
mvn clean package exec:java -Dexec.mainClass="com.widehyo.App" | sed -n '/exec-maven-plugin/,/Finished at/p'
[INFO] --- exec-maven-plugin:3.5.0:java (default-cli) @ demo ---
* App start ====================
result: 120
* App end ======================

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.930 s
[INFO] Finished at: 2024-12-14T19:26:55+09:00
