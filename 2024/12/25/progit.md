Git은 유닉스 파일 시스템과 비슷한 방법으로 저장하지만 좀 더 단순하다. 모든 것을 Tree와 Blob 개체로 저장한다. Tree는 유닉스의 디렉토리에 대응되고 Blob은 Inode나 일반 파일에 대응된다.

Git은 일반적으로 Staging Area(Index)의 상태대로 Tree 개체를 만들고 기록한다. 그래서 Tree 개체를 만들려면 우선 Staging Area에 파일을 추가해서 Index를 만들어야 한다. 아직 Staging Area에 없는 파일이기 때문에 --add 옵션을 꼭 줘야한다. 그리고 디렉토리에 있는 파일이 아니라 데이터베이스에 있는 파일을 추가하는 것이기 때문에 --cacheinfo 옵션이 필요하다. 파일 모드, SHA-1해시, 파일 으름 정보도 입력한다.

Staging Area를 Tree 개체로 저장할 때는 write-tree 명령을 사용한다. write-tree 명령은 Tree 개체가 없으면 자동으로 생성하므로 -w 옵션이 필요 없다.

```
test on  master [!+] ❯ git write-tree
d8329fc1cc938780ffdd9f94e0d364e0ea74f579

test on  master [!+] ❯ git cat-file -p d8329fc1cc938780ffdd9f94e0d364e0ea74f579
100644 blob 83baae61804e65cc73a7201a7252750c76066a30    test.txt

test on  master [!+] ❯ git cat-file -t d8329fc1cc938780ffdd9f94e0d364e0ea74f579
tree

test on  master [!+] ❯ echo 'new file' > new.txt

test on  master [!+?] ❯ git update-index test.txt

test on  master [+?] ❯ git update-index --add new.txt

test on  master [+] ❯ git write-tree
0155eb4229851634a0f03eb265b69f5a2d56f341

test on  master [+] ❯ git cat-file -p 0155eb4229851634a0f03eb265b69f5a2d56f341
100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt

test on  master [!+?] ❯ git update-index test.txt

test on  master [+?] ❯ git update-index --add new.txt

test on  master [+] ❯ git write-tree
0155eb4229851634a0f03eb265b69f5a2d56f341
```

각기 다른 스냅샷을 나타내는 Tree 개체를 세 개 만들었다. 하지만, 여전히 이 스냅샷을 불러오려면 SHA-1 값을 기억하고 있어야 한다. 스냅샷을 누가, 언제, 왜 저장했는지에 대한 정보는 아예 없다. 이런 정보는 커밋 개체애 저장된다.

커밋 개체의 형식은 간단하다. 해당 스냅샷에서 최상단 Tree를 하나 가리킨다. 그리고 user.name과 user.email 설정에서 가져온 Augher/Committer 정보, 시간 정보, 그리고 한 라인 띄운 다음 커밋 메시지가 들어간다.

```bash
test on  master [✘+] ❯ git cat-file -p 3c4e9cd789d88d8d89c1073707c3585e41b0e614
040000 tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579    bak
100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt

test on  master [✘+] ❯ echo 'first commit' | git commit-tree d8329f
502dfe4a5112ae13127e7064f70c8047323bce23


test on  master [✘+] ❯ git cat-file -p 502dfe
tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579
author widehyo@gmail.com <widehyo@gmail.com> 1735102822 +0900
committer widehyo@gmail.com <widehyo@gmail.com> 1735102822 +0900

first commit
```


```bash
test on  master [+] ❯ find .git/objects/ -type f
.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4
.git/objects/83/baae61804e65cc73a7201a7252750c76066a30
.git/objects/fa/49b077972391ad58037050f2a75f74e3671e92
.git/objects/d8/329fc1cc938780ffdd9f94e0d364e0ea74f579
.git/objects/d3/dad9a0c1ab3e240d83f78646a7641ec805ade3
.git/objects/1f/7a7a472abf3dd9643fd615f6da379c4acb3e3a
.git/objects/01/55eb4229851634a0f03eb265b69f5a2d56f341

test on  master [+] ❯ git cat-file -p 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a
version 2

test on  master [+] ❯ git cat-file -p 0155eb4229851634a0f03eb265b69f5a2d56f341
100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt

test on  master [+] ❯ git cat-file -p d3dad9a0c1ab3e240d83f78646a7641ec805ade3
040000 tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579    bak
040000 tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579    bax
100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt

test on  master [+] ❯ git cat-file -p d8329fc1cc938780ffdd9f94e0d364e0ea74f579
100644 blob 83baae61804e65cc73a7201a7252750c76066a30    test.txt

test on  master [+] ❯ git cat-file -p fa49b077972391ad58037050f2a75f74e3671e92
new file

test on  master [+] ❯ git cat-file -p baae61804e65cc73a7201a7252750c76066a30
fatal: Not a valid object name baae61804e65cc73a7201a7252750c76066a30

test on  master [+] ❯ git cat-file -p 83baae61804e65cc73a7201a7252750c76066a30
version 1

test on  master [+] ❯ git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4
test content

test on  master [+] ❯ git cat-file -p 0155eb4229851634a0f03eb265b69f5a2d56f341
100644 blob fa49b077972391ad58037050f2a75f74e3671e92    new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a    test.txt

test on  master [+] ❯ git read-tree --prefix=bak d8329fc1cc938780ffdd9f94e0d364e0ea74f579

test on  master [✘+] ❯ git write-tree
3c4e9cd789d88d8d89c1073707c3585e41b0e614

test on  master [✘+] ❯ echo 'second commit' | git commit-tree 0155eb4 -p 502dfe4
71fc23efa4f266d9baac0f5bec8662b2c201bf7d

test on  master [✘+] ❯ echo 'third commit' | git commit-tree 3c4e9cd -p 71fc23e
76aefda68f1fead41a4ca349a433fef5f5daa2ab

test on  master [✘+] ❯ git log --stat 76aefda

commit 76aefda68f1fead41a4ca349a433fef5f5daa2ab
Author: widehyo@gmail.com <widehyo@gmail.com>
Date:   Wed Dec 25 14:06:31 2024 +0900

    third commit

 bak/test.txt | 1 +
 1 file changed, 1 insertion(+)

commit 71fc23efa4f266d9baac0f5bec8662b2c201bf7d
Author: widehyo@gmail.com <widehyo@gmail.com>
Date:   Wed Dec 25 14:05:47 2024 +0900

    second commit

 new.txt  | 1 +
 test.txt | 2 +-
 2 files changed, 2 insertions(+), 1 deletion(-)

commit 502dfe4a5112ae13127e7064f70c8047323bce23
Author: widehyo@gmail.com <widehyo@gmail.com>
Date:   Wed Dec 25 14:00:22 2024 +0900

    first commit

 test.txt | 1 +
 1 file changed, 1 insertion(+)
```



```
test on  master [✘+] took 3s ❯ which irb
/usr/bin/irb

test on  master [✘+] ❯ irb
irb(main):001:0> content = "what is up, doc?"
=> "what is up, doc?"
# 컨텐츠는 내용이다

irb(main):002:0> header = "blob #{content.length}\0"
=> "blob 16\u0000"
# 헤더는 타입 + " " + 컨텐츠의 길이 + 널문자 로 구성된다.

irb(main):003:0> store = header + content
=> "blob 16\u0000what is up, doc?"
# 헤더와 컨텐츠를 묶어 하나의 저장단위로 만든다

irb(main):004:0> require 'digest/sha1'
=> true
irb(main):005:0> sha1 = Digest::SHA1.hexdigest(store)
=> "bd9dbf5aae1a3862dd1526723246b20206e5fc37"
# SHA1로 저장단위의 해시 값을 가져와
irb(main):006:0> require 'zlib'
=> true

irb(main):007:0> zlib_content = Zlib::Deflate.deplate(store)
(irb):7:in `<main>': undefined method `deplate' for Zlib::Deflate:Class (NoMethodError)
Did you mean?  deflate
        from /usr/lib/ruby/gems/3.0.0/gems/irb-1.3.5/exe/irb:11:in `<top (required)>'
        from /usr/bin/irb:23:in `load'
        from /usr/bin/irb:23:in `<main>'
irb(main):008:0> zlib_content = Zlib::Deflate.deflate(store)
=> "x\x9CK\xCA\xC9OR04c(\xCFH,Q\xC8,V(-\xD0QH\xC9O\xB6\a\x00_\x1C\a\x9D"
irb(main):009:0> path = '.git/objects/' + sha1[0,2] + '/' + sha1[2,38]
# 앞 2글자를 디렉터리 명, 뒤 38자를 파일명으로 사용한다

=> ".git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37"
irb(main):010:0> require 'fileutils'
=> false
irb(main):011:0> require 'fileutils'
=> false
irb(main):012:0> FileUtils.mkdir_p(File.dirname(path))
=> [".git/objects/bd"]
irb(main):013:0> File.open(path, 'w') { |f| f.write zlib_content }
=> 32
# 파일 자체는 store를 zlib으로 압축한 내용을 개체로 저장한다.
```

  git log 76aefda라고 실행하면 전체 히스토리를 볼 수 있지만, 여전히 76aefda를 기억해야 한다. 이 커밋은 마지막 커밋이기 때문에 히스토리를 따라 모든 개체를 조회할 수 있다. SHA-1 값을 날로 사용하기보다 쉬운 이름으로 된 포인터가 있으면 그걸 사용하는 게 더 좋다. 외우기 쉬운 이름으로 된 파일에 SHA-1 값을 저장한다.
  Git에서는이런 것을 "Refs"라고 부른다. SHA-1값이 든 파일은 .git/refs 디렉토리에 있다.

```bash
test on  master [✘+] ❯ tree -a
.
├── .git
│   ├── HEAD
│   ├── branches
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── objects
│   │   ├── 01
│   │   │   └── 55eb4229851634a0f03eb265b69f5a2d56f341
│   │   ├── 1f
│   │   │   └── 7a7a472abf3dd9643fd615f6da379c4acb3e3a
│   │   ├── 3c
│   │   │   └── 4e9cd789d88d8d89c1073707c3585e41b0e614
│   │   ├── 50
│   │   │   └── 2dfe4a5112ae13127e7064f70c8047323bce23
│   │   ├── 71
│   │   │   └── fc23efa4f266d9baac0f5bec8662b2c201bf7d
│   │   ├── 76
│   │   │   └── aefda68f1fead41a4ca349a433fef5f5daa2ab
│   │   ├── 83
│   │   │   └── baae61804e65cc73a7201a7252750c76066a30
│   │   ├── bd
│   │   │   └── 9dbf5aae1a3862dd1526723246b20206e5fc37
│   │   ├── d3
│   │   │   └── dad9a0c1ab3e240d83f78646a7641ec805ade3
│   │   ├── d6
│   │   │   └── 70460b4b4aece5915caf5c68d12f560a9fe3e4
│   │   ├── d8
│   │   │   └── 329fc1cc938780ffdd9f94e0d364e0ea74f579
│   │   ├── fa
│   │   │   └── 49b077972391ad58037050f2a75f74e3671e92
│   │   ├── info
│   │   └── pack
│   └── refs
│       ├── heads
│       └── tags
├── new.txt
└── test.txt

22 directories, 32 files
test on  master [✘+] ❯ echo "76aefda68f1fead41a4ca349a433fef5f5daa2ab" > .git/refs/heads/master

test on  master [✘] ❯ git log --pretty=oneline master
```
