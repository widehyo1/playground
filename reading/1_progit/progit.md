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


vagrant로 실습 중

```
vagrant
├── config
│   └── vagrant_host.conf
├── Vagrantfile
└── vagrant_host
    └── index.html
```

```vagrant/config/vagrant_host.conf
<VirtualHost *:80>
    ServerAdmin   vagrant@vagrant_host.com
    ServerName    www.vagrant_host.com
    ServerAlias   vagrant_host.com
    DocumentRoot  /var/www/vagrant_host
    ErrorLog      /var/log/httpd/vagrant_host.com-error.log
    CustomLog     /var/log/httpd/vagrant_host.com-access.log combined
</VirtualHost>
```

```vagrant/vagrant_host/index.html
<html>
<head>
<title>welcome httpd</title>
</head>
<body>
<h1>Hello vagrant host</h1>
</body>
</html>
```

```vagrant/Vagrantfile
Vagrant.configure("2") do |config|

  config.vm.box = "rockylinux/9"
  config.vm.box_version = "4.0.0"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.synced_folder "./config", "/root/config"
  config.vm.synced_folder "./vagrant_host", "/root/vagrant_host"
  config.vm.synced_folder "./demo_proj.git", "/root/demo_proj.git"

  config.vm.provision "shell", inline: <<-SHELL
    echo 'HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "' | tee -a /etc/profile
    dnf update
    dnf install -y httpd net-tools git
    httpd -v
    systemctl start httpd
    systemctl enable httpd
    ifconfig
    cp /root/config/vagrant_host.conf /etc/httpd/conf.d/vagrant_host.conf
    cp -r /root/vagrant_host /var/www/vagrant_host
    chown -R vagrant:vagrant /var/www/vagrant_host/index.html
    apachectl configtest
    systemctl restart httpd
    mkdir -p /opt/git/demo_proj.git
    cd /opt/git/demo_proj.git
    git init --bare --shared
  SHELL
end
```

```bash
git clone vagrant@192.168.56.10:/opt/git/demo_proj.git
Cloning into 'demo_proj'...
vagrant@192.168.56.10's password: 
fatal: detected dubious ownership in repository at '/opt/git/demo_proj.git'
To add an exception for this directory, call:

	git config --global --add safe.directory /opt/git/demo_proj.git
```

$ git config --global --add safe.directory /opt/git/demo_proj.git


```bash
~/gitclone ❯ git clone vagrant@192.168.56.10:/opt/git/demo_proj.git
Cloning into 'demo_proj'...
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:360IVP62Nr2q9s3/9f4JtQQBOgwgqpjxhzPKH/B7AgA.
Please contact your system administrator.
Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/user/.ssh/known_hosts:2
ECDSA host key for 192.168.56.10 has changed and you have requested strict checking.
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```


```bash
reading/progit/vagrant on  main [!?] via ⍱ v2.4.3 ❯ ssh-keygen -R 192.168.56.10
# Host 192.168.56.10 found: line 2
/home/user/.ssh/known_hosts updated.
Original contents retained as /home/user/.ssh/known_hosts.old
reading/progit/vagrant on  main [!?] via ⍱ v2.4.3 ❯ cat ~/.ssh/known_hosts
gitlab.com,172.65.251.78 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFSMqzJeV9rUzU4kWitGjeR4PWSa29SPqJ1fVkhtj3Hw9xjLVXVYrU9QlYWrOLXBpQ6KWjbjTDTdDkoohFzgbEY=
reading/progit/vagrant on  main [!?] via ⍱ v2.4.3 ❯ git clone vagrant@192.168.56.10:/opt/git/demo_proj.git
Cloning into 'demo_proj'...
The authenticity of host '192.168.56.10 (192.168.56.10)' can't be established.
ECDSA key fingerprint is SHA256:360IVP62Nr2q9s3/9f4JtQQBOgwgqpjxhzPKH/B7AgA.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.10' (ECDSA) to the list of known hosts.
vagrant@192.168.56.10's password: 
fatal: detected dubious ownership in repository at '/opt/git/demo_proj.git'
To add an exception for this directory, call:

	git config --global --add safe.directory /opt/git/demo_proj.git
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
가 발생한 이유는 vagrant용 서버를 항상 delete && create해서 생긴 문제였다.

alias reva='vagrant destroy -f && vagrant up'

서버가 새로 생기니 ~/.ssh/known_host에 기록한 ssh key 값이 서버와 달라지게 되어 위의 에러 메시지가 발생한다. 그리고 이 과정은 터미널에서
The authenticity of host '192.168.56.10 (192.168.56.10)' can't be established.
ECDSA key fingerprint is SHA256:360IVP62Nr2q9s3/9f4JtQQBOgwgqpjxhzPKH/B7AgA.
Are you sure you want to continue connecting (yes/no)?

가 수행된 경우에만 정상적으로 동작한다.


```bash
~/gitclone took 2s ❯ git clone vagrant@192.168.56.10:/opt/git/demo_proj.git
Cloning into 'demo_proj'...
The authenticity of host '192.168.56.10 (192.168.56.10)' can't be established.
ECDSA key fingerprint is SHA256:EJ9fiXFhLy3KHIbwsgUg/j5wrHHFA9vrV5TykxMqvJI.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.10' (ECDSA) to the list of known hosts.
vagrant@192.168.56.10's password: 
warning: You appear to have cloned an empty repository.
~/gitclone took 6s ❯ ls
algorithm-interview  demo_proj                  private_bak  tui_playground
CSharpRepl           functional-programming-js  sed_awk      urwid_tui
demo                 playground                 travel       workspace
~/gitclone ❯ cd demo
demo on  project1 ❯ cd ..
~/gitclone ❯ cd demo_proj/
demo_proj on  master ❯ ls
demo_proj on  master ❯ ls -al
total 4
drwxrwxr-x.  3 user user   18 Dec 28 22:35 .
drwxrwxr-x. 14 user user 4096 Dec 28 22:35 ..
drwxrwxr-x.  7 user user  119 Dec 28 22:35 .git
demo_proj on  master ❯ cd ..
~/gitclone ❯ date
Sat Dec 28 22:36:29 KST 2024
```


```bash
demo_proj on  master ❯ vi Readme.md
demo_proj on  master [?] took 10s ❯ git add .
demo_proj on  master [+] ❯ git commit -m "test commit"
[master (root-commit) 7fd4183] test commit
 1 file changed, 1 insertion(+)
 create mode 100644 Readme.md
demo_proj on  master ❯ git push
vagrant@192.168.56.10's password: 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 231 bytes | 231.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To 192.168.56.10:/opt/git/demo_proj.git
 * [new branch]      master -> master
demo_proj on  master took 3s ❯ ginfo
* master                7fd4183 [origin/master] test commit
  remotes/origin/master 7fd4183 test commit
demo_proj on  master ❯ exit

reading/progit/vagrant on  main [!?] via ⍱ v2.4.3 ❯ vagrant ssh
[vagrant@localhost ~]$ cd /opt/git/demo_proj.git/
[vagrant@localhost demo_proj.git]$ git log
commit 7fd41835b7596b1540f08eedcbd065b96c54c75f (HEAD -> master)
Author: widehyo@gmail.com <widehyo@gmail.com>
Date:   Sat Dec 28 22:40:53 2024 +0900

    test commit
[vagrant@localhost demo_proj.git]$ 
```

성공!

---
---

```bash
  config.vm.provision "shell", inline: <<-SHELL
    # echo 'HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "' | tee -a /etc/profile
    echo 'HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "' >> /etc/profile
    dnf update
    dnf install -y httpd net-tools git util-linux-user
    useradd -m -p $(perl -e 'print crypt($ARGV[0], "password")' 'gitgit') git
    mkdir /home/git/.ssh
    touch /home/git/.ssh/authorized_keys
    chown -R git:git /home/git/.ssh
    chmod 700 /home/git/.ssh
    chmod 600 /home/git/.ssh/authorized_keys
    which git-shell >> /etc/shells
    chsh -s $(which git-shell) git
    mkdir -p /opt/git/demo_proj.git
    cd /opt/git/demo_proj.git
    git init --bare --shared
    chown -R git:git .
    httpd -v
    systemctl start httpd
    systemctl enable httpd
    ifconfig
    cp /root/config/vagrant_host.conf /etc/httpd/conf.d/vagrant_host.conf
    cp -r /root/vagrant_host /var/www/vagrant_host
    chown -R git:git /var/www/vagrant_host/index.html
    apachectl configtest
    systemctl restart httpd
  SHELL
```

git 유저를 서버용으로만 생성하고 사용하는 예제 확인 완료

```
~/gitclone ❯ ls
algorithm-interview  functional-programming-js  sed_awk         urwid_tui
CSharpRepl           playground                 travel          workspace
demo                 private_bak                tui_playground
~/gitclone ❯ git clone git@192.168.56.10:/opt/git/demo_proj.git
Cloning into 'demo_proj'...
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:7XS491+2hr+wcBkKUh27DvZ98qx1sbj79mml5ccsmbM.
Please contact your system administrator.
Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/user/.ssh/known_hosts:2
ECDSA host key for 192.168.56.10 has changed and you have requested strict checking.
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
~/gitclone ❯ vi ~/.ssh/known_hosts
~/gitclone took 2s ❯ git clone git@192.168.56.10:/opt/git/demo_proj.git
Cloning into 'demo_proj'...
The authenticity of host '192.168.56.10 (192.168.56.10)' can't be established.
ECDSA key fingerprint is SHA256:7XS491+2hr+wcBkKUh27DvZ98qx1sbj79mml5ccsmbM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.10' (ECDSA) to the list of known hosts.
git@192.168.56.10's password: 
Permission denied, please try again.
git@192.168.56.10's password: 
warning: You appear to have cloned an empty repository.
~/gitclone took 11s ❯ ll
total 12
drwxrwxr-x.  9 user user 4096 Jun 17  2024 algorithm-interview
drwxrwxr-x.  8 user user 4096 Apr 27  2024 CSharpRepl
drwxrwxr-x.  4 user user   48 Sep 22 22:35 demo
drwxrwxr-x.  3 user user   18 Dec 28 23:13 demo_proj
drwxrwxr-x.  4 user user  128 Apr 16  2024 functional-programming-js
drwxrwxr-x.  7 user user   96 Dec 28 20:44 playground
drwxrwxr-x.  4 user user   47 Nov 17 15:12 private_bak
drwxrwxr-x.  4 user user  154 Mar 23  2024 sed_awk
drwxrwxr-x.  4 user user   47 Aug  4 15:51 travel
drwxrwxr-x.  4 user user   59 Aug 25 20:56 tui_playground
drwxrwxr-x.  5 user user  105 Aug 25 20:58 urwid_tui
drwxrwxr-x. 10 user user 4096 Nov 17 15:18 workspace
~/gitclone ❯ cd demo_proj/
demo_proj on  master ❯ ls
demo_proj on  master ❯ ssh git@192.168.56.10
git@192.168.56.10's password: 
Last failed login: Sat Dec 28 14:19:20 UTC 2024 from 192.168.56.1 on ssh:notty
There was 1 failed login attempt since the last successful login.
fatal: Interactive git shell is not enabled.
hint: ~/git-shell-commands should exist and have read and execute access.
Connection to 192.168.56.10 closed.
demo_proj on  master took 2s ❯ vi readme.md
demo_proj on  master [?] took 26s ❯ git add .
demo_proj on  master [+] ❯ git commit -m "vagrant server as git host"
[master (root-commit) 9badc42] vagrant server as git host
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md
demo_proj on  master ❯ git push
git@192.168.56.10's password: 
Permission denied, please try again.
git@192.168.56.10's password: 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 261 bytes | 261.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To 192.168.56.10:/opt/git/demo_proj.git
 * [new branch]      master -> master
demo_proj on  master took 6s ❯ exit

reading/progit/vagrant on  main [!?] via ⍱ v2.4.3 ❯ vagrant ssh
[vagrant@localhost ~]$ cd /opt/git/demo_proj.git/
[vagrant@localhost demo_proj.git]$ git log --oneline
fatal: detected dubious ownership in repository at '/opt/git/demo_proj.git'
To add an exception for this directory, call:

	git config --global --add safe.directory /opt/git/demo_proj.git
[vagrant@localhost demo_proj.git]$ sudo su
[root@localhost demo_proj.git]# su - git
Last login: Sat Dec 28 14:19:50 UTC 2024 from 192.168.56.1 on pts/0
Last failed login: Sat Dec 28 14:20:54 UTC 2024 from 192.168.56.1 on ssh:notty
There was 1 failed login attempt since the last successful login.
fatal: Interactive git shell is not enabled.
hint: ~/git-shell-commands should exist and have read and execute access.
[root@localhost demo_proj.git]# su git
fatal: Interactive git shell is not enabled.
hint: ~/git-shell-commands should exist and have read and execute access.
[root@localhost demo_proj.git]# git config --global --add safe.directory /opt/git/demo_proj.git
[root@localhost demo_proj.git]# git log
commit 9badc4200de3c79f3d8fe44c30e4d15cbf14f5ae (HEAD -> master)
Author: widehyo@gmail.com <widehyo@gmail.com>
Date:   Sat Dec 28 23:15:04 2024 +0900

    vagrant server as git host
```

---
---
---


reading/progit/vagrant on  main [✘!?] via ⍱ v2.4.3 took 55s ❯ cat Vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "rockylinux/9"
  config.vm.box_version = "4.0.0"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "forwarded_port", guest: 443, host: 8443, host_ip: "127.0.0.1"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.56.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./config", "/root/config"
  config.vm.synced_folder "./mygit", "/root/mygit"

  # Disable the default share of the current code directory. Doing this
  # provides improved isolation between the vagrant box and your host
  # by making sure your Vagrantfile isn't accessible to the vagrant box.
  # If you use this you may want to enable additional shared subfolders as
  # shown above.
  # config.vm.synced_folder ".", "/vagrant", disabled: true

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    # echo 'HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "' | tee -a /etc/profile
    echo 'HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "' >> /etc/profile
    dnf update
    dnf install -y httpd net-tools git
    mkdir -p /opt/git/demo_proj.git
    cd /opt/git/demo_proj.git
    git init --bare --shared
    chown -R apache:apache /opt/git
    htpasswd -c /opt/git/.htpasswd git
    hostnamectl set-hostname mygit
    echo "127.0.0.1 localhost mygit" >> /etc/hosts
    echo "::1 localhost mygit" >> /etc/hosts
    echo "ServerName mygit" >> /etc/httpd/conf/httpd.conf
    echo "LoadModule cgi_module modules/mod_cgi.so" >> /etc/httpd/conf.modules.d/00-base.conf
    httpd -v
    systemctl start httpd
    systemctl enable httpd
    ifconfig
    cp /root/config/mygit.conf /etc/httpd/conf.d/mygit.conf
    cp -r /root/mygit /var/www/mygit
    chown -R apache:apache /var/www/mygit/index.html
    apachectl configtest
    systemctl restart httpd
  SHELL
end

reading/progit/vagrant on  main [✘!?] via ⍱ v2.4.3 ❯ cdg
~/gitclone ❯ ls
algorithm-interview  demo_proj_with_user_git    private_bak  tui_playground
CSharpRepl           functional-programming-js  sed_awk      urwid_tui
demo                 playground                 travel       workspace
~/gitclone ❯ git clone http://192.168.56.10/git/demo_proj.git
Cloning into 'demo_proj'...
warning: You appear to have cloned an empty repository.

[vagrant@mygit ~]$ sudo htpasswd /opt/git/.htpasswd git
New password: 
Re-type new password: 
Updating password for user git

demo_proj on  master ❯ git push
Gtk-Message: 00:35:51.099: Failed to load module "canberra-gtk-module"
Gtk-Message: 00:35:52.570: Failed to load module "canberra-gtk-module"
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 215 bytes | 215.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
error: RPC failed; HTTP 403 curl 22 The requested URL returned error: 403
send-pack: unexpected disconnect while reading sideband packet
fatal: the remote end hung up unexpectedly
Everything up-to-date

---

Integration-Manager 워크플로

1. 프로젝트 Integration-Manager는 프로젝트 메인저장소에 Push한다.
2. 프로젝트 기여자는 메인 저장소를 Clone하고 수정한다.
3. 기여자는 자신의 저장소에 Push하고 Integration-Manager가 접근할 수 있도록 공개해놓는다.
4. 기여자는 Integration-Manager에게 변경사항을 적용해 줄 것을 이메일로 요청한다.
5. Integration-Manager는 기여자의 저장소를 리모트 저장소로 등록하고 수정하상을 Merge하여 테스트한다.
6. Integration-Manager는 Merge한 사항을 메인 저장소에 Push한다.

> $ git log --no-merges issue54..origin/master
> issue54..origin/master 문법은 히스토리를 검색할 때 뒤의 브랜치(origin/master)에 속한 커밋 중 앞의 브랜치(issue54)에 속하지 않은 커밋을 검색하는 문법이다.

> $ git push -u origin featureA
> 리모트 저장소에 featureA 브랜치를 생성한다.
> $ git push -u origin featureB:featureBee
> 로컬 featureB 브랜치를 리모트 featureBee브랜치에 push한다.

> git log contrib --not master
> ==
> git log master..contrib

> 정말 보고 싶은 것은 토픽 브랜치에서 추가한 것이고 결국에는 이것을 master 브랜치에 추가하려는 것이다. 그러니까 master 브랜치와 토픽 브랜치의 공통조상인 커밋을 찾아서 토픽 브랜치가 현재 가리키는 커밋과 비교해야 한다.
> git merge-base contrib master
> $HASH
> git diff $HASH

> TFAE

> git diff master...contrib
> diff 명령을 사용할 때 두 브랜치 사이에 ...을 쓰면, 두 브랜치의 공통조상과 브랜치의 마지막 커밋을 비교한다.

git 명령중에 협업을 위한 명령들이 많구나
그리고 이런 명령들은 직접 써봐야 겠다.

flow도 얘기만 들어본 것들이 나온다
main / next / pu / maint
언젠가 이런 프로젝트에 참여하게 될까

git archive나 hash-object, 그리고 메일링 관련 명령이나 패치 적용하는 git am, git patch, git apply도 존재를 모르고 있었음
일단 실습은 뒤로

---

cat .git/config

> fetch =로 시작되는 라인이 "refspec."이라는 거다. 리모트 이름과 로컬 .git 디렉터리를 어떻게 매핑하는지 나타낸다.


---

05/30 1회독 완료
