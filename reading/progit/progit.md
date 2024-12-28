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

---
> Git은 데이터를 변경사항(Diff)으로 기록하지 않고 일련의 스냅샷으로 기록한다는 것을 1장에서 보여줬다.
> git commit으로 커밋하면 먼저 루트 디렉터리와 각 하위 디렉터리의 트리 개체를 체크섬과 함께 저장소에 저장한다. 그 다음에 커밋 개체를 만들고 메타데이터와 루트 디렉터리 트리 개체를 가리키는 포인터 정보를 커밋 개체에 넣어 저장한다.

Commit.keys() = [tree, parent, author, committer]

> Merge 메시지에서 "fast-forward"가 보이는가. Merge할 브랜치가 가리키는 커밋이 현 브랜치 커밋의 Upstream 브랜치이기 때문에 master 브랜치 포인터는 Merge 과정 없이 그저 최신 커밋으로 이동한다. 이런 Merge 방식을 'Fast forward'라고 부른다. 다시 말해 A 브랜치에서 다른 B 브랜치를 Merge할 때 B 브랜치가 A 브랜치 이후의 커밋을 가리키고 있으면 그저 A 브랜치가 B 브랜치와 동일한 커밋을 가리키도록 이동시킬 뿐이다.
> 현재 브랜치가 가리키는 커밋이 Merge할 브랜치의 조상이 아니므로... Git은 각 브랜치가 기리키는 커밋 두 개와 공통 조상 하나를 사용하여 3-way Merge한다.
> 단순히 브랜치 포인터를 최신 커밋으로 옮기는 게 아니라 3-way Merge의 결과를 별도의 커밋으로 만들고 나서 해당 브랜치가 그 커밋을 가리키도록 이동시킨다. 그래서 이런 커밋은 부모가 여러 개고 Merge 커밋이라고 부른다.
> Git은 Merge하는데 필요한 최적의 공통 조상을 자동으로 찾는다.
> 리모트 브랜치 삭제
> git push origin --delete serverfix 명령을 실행하면 서버에서 브랜치(즉 커밋을 가리키는 포인터) 하나가 사라진다.
> 서버에서 가비지 컬렉터가 동작하지 않는 한 데이터는 사라지지 않기 때문에 종종 의도치 않게 삭제한 경우엥도 커밋한 데이터를 살릴 수 있다.
>
> git checkout experiment
> git rebase master
experiment <- C4 pointing C2
master <- C3 pointing C3
1. 두 브랜치가 나뉘기 전인 공통 커밋(C2)으로 이동(공통조상 이동)
2. C2 커밋부터 지금 Checkout한 브랜치(experiment)가 가리키는 커밋까지 diff를 차례로 만들어 어딘가에 임시로 저장해 놓는다.(diff 생성)
3. Rebase할 브랜치(experiment, C4)가 합칠 브랜치(master, C3)를 카리키게 하고 아까 저장해 놓았던 변경사항을 차례대로 적용한다(커밋 브랜치 이동 후 diff 적용)
4. 그리고 나서 master 브랜치를 Fast-forward한다.

> git rebase --onto master server client
> 이 명령은 "client 브랜치를 Checkout하고 server와 client의 공통 조상 이후의 Patch를 만들어 master에 적용"하라는 내용이다.

선생님? 진도가 너무 빠릅니다.
client 브랜치 specific한 변경사항만 master 브랜치에 적용하고 싶을 때 사용한다.

> git rebase master server
> git checkout master
> git merge server
> git branch -d client
> git branch -d server

---

```bash
playground/reading/progit on  main [!?] ❯ git clone --bare my_project my_project.git
fatal: repository 'my_project' does not exist

playground/reading/progit on  main [!?] ❯ mkdir my_project

playground/reading/progit on  main [!?] ❯ git clone --bare my_project my_project.git
fatal: repository 'my_project' does not exist

playground/reading/progit on  main [!?] ❯ ls
my_project  progit.md  simplegit-progit

playground/reading/progit on  main [!?] ❯ cd my_project/

reading/progit/my_project on  main [!?] ❯ git init
Initialized empty Git repository in /home/widehyo/gitclone/playground/reading/progit/my_project/.git/

my_project on  master ❯ ls

my_project on  master ❯ ls -al
total 12
drwxr-xr-x 3 widehyo widehyo 4096 Dec 28 20:36 .
drwxr-xr-x 4 widehyo widehyo 4096 Dec 28 20:35 ..
drwxr-xr-x 7 widehyo widehyo 4096 Dec 28 20:36 .git

my_project on  master ❯ cd ..

playground/reading/progit on  main [!?] ❯ git clone --bare my_project my_project.git
Cloning into bare repository 'my_project.git'...
warning: You appear to have cloned an empty repository.
done.
```
