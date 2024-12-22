# vimenter 2024

## presentations

### 이재열님 : You don't need Plugin, Long live the command-line
- 마스토돈 nvim 플러그인 개발자
- neovim으로 생산성 퀀텀점프하기
- 플러그인이 정말 필요할까
  - 어떤 플러그인은 거의 필수
- vscode는 chromium기반으로 개발 됨
- pipe/popen (CLI 도구 작성)
- GUM

### 이효승님 : IdeaVim 사용 경험 공유
- 게임엔진 개발자
- neovim으로도 기능이 잘 되는 것을 확인했습니다만...
  - LSP가 완벽하지 않음(unreal cpp), indexing > 10 hours
- VSvim vs IdeaVim
  - rc파일 shortcut 지원
  - recursive fold clodse/open 지원
  - global mark(파일간 mark) 지원
  - 최신 플러그인 부분지원
- 게임 개발 터미널 키고 로그 watch하는 경우는 잘 없음
-  ss: Telescope <Action> in rc map <leader>ss <Action>(GotoSymbol)
  - IdeaVim: track action ids
  - advanced settings -> left margin in distraction free mode

### 이광효님 : 터미널에서 Vim을 활용해서 생산성을 높이는 방법
- 클로저 좋다는데?
- emacs같은 느낌

### 은은수님 : 대학생의 터미널 생활 적응기
- 리눅스를 깔고싶어서 이분 진짜다...
- 터미널이 가장 익숙함
- 터머널 간지 인정
- 듀얼부팅

### aca님 : nix를 활용해서 vim의 다양한 문제를 해결하기
- vim 7,8년
- 옆 사수분 vim 유명인, 앞 분 fzf 만든분 ㄷㄷ
- 환경설정
  - tools break
    - nightly build가 뭐임
- nix
  - 패키지매니저이자 함수형 언어이자 기반한 OS도 있음
- 근본적으로 해결하고 싶다면 해도 좋음
- zls
- brew install 등 안해도 lsp에서 install만 해도 다 됨
- fzf.vim
- fzf의 의존성, lsp의 의존성 등이 각자의 몫이지만 nix에서는 아니다.
- linux 사용자에게 nixOS 추천
- update를 롤백할 수 있음
- aca github nixconfig라는 repo
- wsl에서 nix?
  - nix깔고 ssh로 다운하거나
  - 아예 wsl에 nix 있음
  - wslg 있음
  - wsl install하면 다 됨
  - 자기만의 설정을 올려두면 여러 머신에 적용 가능
- nix 패키지로 한번에 설치하면 가능(centos, rocky, arch 등)
- flake nix를 패키지매니저로 install
- 내가 관리하는 여러 서버를 모두 적용하고 rolling update도 됨
- 모든 system을 nix로 동기화 중
- 대신 disk 용량을 많이 씀

### 황정현님 : vscode-vim 사용후기
- set matchmairs
- gh <- vscode vim에서 cursor에 hover하는 기능
- auxiliary 보조
- editor, editor group, auxiliary bar, panel
- 커서 이동 = Focus
- Magitts extension
- symbol navigate back
- > terminal link
- git log | code -
- keybindings.json
- when 특정한 단축키가 우리가 원하는 상황에서만 실행되어야 함
- devtools context keys를 하면 console이 있음
- 이걸 개발자도구에서 확인해서
- contextkeys
- Y콤퓨타체
- 디버깅 DAP 적용이 너무 어려워서 넘어감

### 차주훈님 : 전통적인 커밋 패턴과는 다르게, 개발자의 의도를 먼저 선언하는 Git Workflow 제안
- 커밋: 의도를 기록
- WIP work in progress
- 커밋의 범위가 커지는 걸 어떻게 방지할까?
  - 코드를 작성할 때 의식적으로 커밋 범위 생각하기
  - atomic commit
  - 자주 커밋
- git commit --allow-empty -m 'TODO: ...'
- git commit --fixup <hash>
- git rebase -i <hash> --autosquash
- 네오빔으로 워크플로우 자동화하기
  - 오
- 자신만의 워크플로우를 만들자

### 이종립님 : vi 문법으로 sed 처럼 사용할 수 있는 명령어, vised 개발 후기
- 지난 13,14년간 vim을 쓰며 현재 vim에 대해 가지고 있는 생각
- vim의 전능감
- vim 처음 배울때 작은 프로그램 짜는 것 같다고 느낀 그거네
  - 텍스트 처리 언어로서의 vim
- kotlin, java
- nodejs
- vim에 대해서 생각하게 되는 좋은 발표
