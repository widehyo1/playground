> Git의 모든기능을 지원하는 것은 CLI 뿐이다.
> Git은 curl, zlib, openssl, expat, libiconv를 필요로 한다.
> git status -s 또는 git status --short처럼옵션을 주면현재 변경한상태를 짤막하게 보여준다.

[Working Directory]|[Staging Area]|[git Directory]
git diff: difference between working directory and staging area
git diff --staged: difference between staging area and git directory
git diff --cached == git diff --staged

> Git에서 파일을 제거하려면 git rm 명령으로 Tracked 상태의 파일을 삭제한 후에(정확하게는 Staging Area에서 삭제하는 것) 커밋해야 한다. 이 명령은 워킹 디렉터리에 있는 파일도 삭제하기 때문에 실제로 파일도 지워진다.
> 또 Staging Area에서만 제거하고 워킹 디렉터리에 있는 파일은 지우지 않고 남겨둘 수 있다.
> git log -p -2: -p는 각 커밋의 diff 결과를 보여준다. -2는 최근 두 개의 결과만 보여주는 옵션이다.
> 마지막으로 파일 경로로 검색하는 옵션이 있는데 이것도 정말 유용하다. 디렉터리나 파일 이름을 사용하여 그 파일이 변경된 log의 결과를 검색할 수 있다. 이 옵션은 --와 함께 경로 이름을 사용하는데 명령어 끝 부분에 쓴다. git log -- path1 path2
> git log --after="2024-12-01" -- 2024
> git log --since=2.weeks, git log --since="2008-10-01" --before="2008-11-01"
> git log -S history: -S는 커밋 변경(추가/삭제) 내용 안의 텍스트를 검색한다.
> git log: --since, --after, --until, --before
> git rm --cached README

> git commit --amend
> git tag
> annotated 태그(git 데이터베이스에 태그를 만든사람의 이름, 이메일과 태그를 만든 날짜, 그리고 태그 메시지도 저장한다.) 이 모든 정보를 저장해둬야 할 때문 Annotated 태그를 추천한다.
> git tag -a v1.4 -m 'my version 1.4'
> git show 명령으로 태그 정보와 커밋 정보를 모두 확인할 수 있다.
> git tag v1.4-lw

> git config --global alias.co checkout
> git config --global alias.br branch
> git config --global alias.ci commit
> git config --global alias.st status
> git config --global alias.unstage 'reset HEAD --'
> git config --global alias.last 'log -1 HEAD'
> git config --global alias.llog '!~/shell/git_commit_hist.sh | less'
