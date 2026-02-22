   21  2026-02-21 16:59:13 ls /usr/bin/lxc-* >> ~/temp.txt

```awk
BEGIN {
  FS="/"
}
{
  printf "alias l%s='%s'\n", substr($4, 5), $4
}
```

alias virc="vi ~/.bashrc"
alias catrc="cat ~/.bashrc"

alias lattach='lxc-attach'
alias lautostart='lxc-autostart'
alias lcgroup='lxc-cgroup'
alias lcheckconfig='lxc-checkconfig'
alias lcheckpoint='lxc-checkpoint'
alias lconfig='lxc-config'
alias lconsole='lxc-console'
alias lcopy='lxc-copy'
alias lcreate='lxc-create'
alias ldestroy='lxc-destroy'
alias ldevice='lxc-device'
alias lexecute='lxc-execute'
alias lfreeze='lxc-freeze'
alias linfo='lxc-info'
alias lls='lxc-ls'
alias lmonitor='lxc-monitor'
alias lsnapshot='lxc-snapshot'
alias lstart='lxc-start'
alias lstop='lxc-stop'
alias ltop='lxc-top'
alias lunfreeze='lxc-unfreeze'
alias lunshare='lxc-unshare'
alias lupdate-config='lxc-update-config'
alias lusernsexec='lxc-usernsexec'
alias lwait='lxc-wait'

alias uvpy='uv run python'
export PATH=$PATH:$HOME/.local/bin

alias rp='realpath'

wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant



```bash
root@ubuntu22:~/gitclone/playground/reading/52_Containerization_with_LXC# vagrant plugin install vagrant-LXC
Installing the 'vagrant-LXC' plugin. This can take a few minutes...
Vagrant failed to properly resolve required dependencies. These
errors can commonly be caused by misconfigured plugin installations
or transient network issues. The reported error is:

Unable to resolve dependency: user requested 'vagrant-LXC (> 0)'

root@ubuntu22:~/gitclone/playground/reading/52_Containerization_with_LXC# vagrant plugin install vagrant-lxd
Installing the 'vagrant-lxd' plugin. This can take a few minutes...
Fetching public_suffix-7.0.2.gem
Fetching addressable-2.8.8.gem
Fetching sawyer-0.9.3.gem
Fetching thread_safe-0.3.6.gem
Fetching tzinfo-1.2.11.gem
Fetching minitest-5.27.0.gem
NOTE: minitest 5 will be the last in the minitest family to support
      ruby 1.8 to 2.7. If you need to keep using these versions,
      you need to pin your dependency to minitest with something
      like "~> 5.0". See History.rdoc to locate compatible
      versions.

      Further, minitest 6 will be dropping the following:

      + MiniTest (it's been Minitest for >10 years)
      + MiniTest::Unit
      + MiniTest::Unit::TestCase
      + assert_send (unless you argue for it well)
      + assert_equal nil, obj
      + mocks and stubs: moving minitest/mock.rb to its own gem
Fetching activesupport-5.2.8.1.gem
Fetching hyperkit-1.2.0.gem
Fetching vagrant-lxd-0.4.3.gem
Installed the plugin 'vagrant-lxd (0.4.3)'!

root@ubuntu22:~/gitclone/playground/reading/52_Containerization_with_LXC# lxc list
If this is your first time running LXD on this machine, you should also run: lxd init
To start your first container, try: lxc launch ubuntu:22.04
Or for a virtual machine: lxc launch ubuntu:22.04 --vm

+------+-------+------+------+------+-----------+
| NAME | STATE | IPV4 | IPV6 | TYPE | SNAPSHOTS |
+------+-------+------+------+------+-----------+

root@ubuntu22:~# lxd init
Would you like to use LXD clustering? (yes/no) [default=no]: 
Do you want to configure a new storage pool? (yes/no) [default=yes]: 
Name of the new storage pool [default=default]: 
Name of the storage backend to use (lvm, zfs, btrfs, ceph, cephobject, dir) [default=zfs]: 
Create a new ZFS pool? (yes/no) [default=yes]: 
Would you like to use an existing empty block device (e.g. a disk or partition)? (yes/no) [default=no]: 
Size in GiB of the new loop device (1GiB minimum) [default=5GiB]: 
Would you like to connect to a MAAS server? (yes/no) [default=no]: 
Would you like to create a new local network bridge? (yes/no) [default=yes]: 
What should the new bridge be called? [default=lxdbr0]: 
What IPv4 address should be used? (CIDR subnet notation, “auto” or “none”) [default=auto]: 
What IPv6 address should be used? (CIDR subnet notation, “auto” or “none”) [default=auto]: 
Would you like the LXD server to be available over the network? (yes/no) [default=no]: 
Would you like stale cached images to be updated automatically? (yes/no) [default=yes]: 
Would you like a YAML "lxd init" preseed to be printed? (yes/no) [default=no]: 
root@ubuntu22:~# lxc list
+------+-------+------+------+------+-----------+
| NAME | STATE | IPV4 | IPV6 | TYPE | SNAPSHOTS |
+------+-------+------+------+------+-----------+
root@ubuntu22:~# vagrant plugin list
vagrant-lxd (0.4.3, global)


root@ubuntu22:~# lxc launch ubuntu:22.04 test1
Creating test1
Starting test1                                
root@ubuntu22:~# lxc list      
+-------+---------+------+----------------------------------------------+-----------+-----------+
| NAME  |  STATE  | IPV4 |                     IPV6                     |   TYPE    | SNAPSHOTS |
+-------+---------+------+----------------------------------------------+-----------+-----------+
| test1 | RUNNING |      | fd42:58c:603e:5968:216:3eff:fe91:aab6 (eth0) | CONTAINER | 0         |
+-------+---------+------+----------------------------------------------+-----------+-----------+
root@ubuntu22:~# lxc exec test1 -- bash
root@test1:~# ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 12:58 ?        00:00:00 /sbin/init
root          59       1  0 12:58 ?        00:00:00 /lib/systemd/systemd-journald
root         100       1  0 12:58 ?        00:00:00 /lib/systemd/systemd-udevd
root         107       1  0 12:58 ?        00:00:00 snapfuse /var/lib/snapd/snaps/snapd_25935.snap /
root         110       1  0 12:58 ?        00:00:00 snapfuse /var/lib/snapd/snaps/lxd_36918.snap /sn
root         113       1  0 12:58 ?        00:00:00 snapfuse /var/lib/snapd/snaps/core20_2686.snap /
systemd+     185       1  0 12:58 ?        00:00:00 /lib/systemd/systemd-networkd
systemd+     187       1  0 12:58 ?        00:00:00 /lib/systemd/systemd-resolved
root         218       1  0 12:58 ?        00:00:00 /usr/sbin/cron -f -P
message+     219       1  0 12:58 ?        00:00:00 @dbus-daemon --system --address=systemd: --nofor
root         222       1  0 12:58 ?        00:00:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --
syslog       223       1  0 12:58 ?        00:00:00 /usr/sbin/rsyslogd -n -iNONE
root         225       1  0 12:58 ?        00:00:00 /usr/bin/snap wait system seed.loaded
root         226       1  0 12:58 ?        00:00:00 /usr/lib/snapd/snapd
root         228       1  0 12:58 ?        00:00:00 /lib/systemd/systemd-logind
root         230       1  0 12:58 ?        00:00:00 /usr/bin/python3 /usr/lib/ubuntu-advantage/daemo
root         234       1  0 12:58 pts/0    00:00:00 /sbin/agetty -o -p -- \u --noclear --keep-baud c
root         239       1  0 12:58 ?        00:00:00 /lib/systemd/systemd-hostnamed
root         240       1  0 12:58 ?        00:00:00 /usr/bin/python3 /usr/share/unattended-upgrades/
root         241       1  0 12:58 ?        00:00:00 /usr/libexec/polkitd --no-debug
root         245       1  0 12:58 ?        00:00:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 s
root         383       0  0 12:58 pts/1    00:00:00 bash
root         727       1  0 12:59 ?        00:00:00 /lib/systemd/systemd-timedated
root         728     383  0 12:59 pts/1    00:00:00 ps -ef
root@test1:~# 
exit
root@ubuntu22:~# lxc delete -f test1
```
---


```py
from flask import Flask, jsonify
import lxc

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def list_containers():
    containers = lxc.list_containers()
    return jsonify({"containers": containers})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```

```curl
request = "GET"
url = "http://localhost:8080/list"
silent
# verbose
```

```txt
{
  "containers": []
}
```

---


```py
@app.route('/build', methods=['POST'])
def build():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    print(data)
    return jsonify({"temp": "a"})
```

```curl
request = "POST"
url = "http://localhost:8080/build"
header = "Content-Type: application/json"
silent
data = "@/root/request.json"
# verbose
```


```json
{ "name": "rest_container",
"dist": "ubuntu",
"release": "jammy",
"arch": "amd64"
 }
```

```json
{
  "temp": "a"
}
```


```log
127.0.0.1 - - [22/Feb/2026 13:32:17] "POST /build HTTP/1.1" 200 -
{'name': 'rest_container', 'dist': 'ubuntu', 'release': 'jammy', 'arch': 'amd64'}
```


```py
name = "python_container"
container = lxc.Container(name)

if not container.defined:
    if container.create("download", 0, {"dist": "ubuntu", "release": "jammy", "arch": "amd64"}):
        print("container created")
```
---


```py
@app.route('/build', methods=['POST'])
def build():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    
    name = data.get('name')
    container = lxc.Container(name)
    payload = dict(**data)
    payload.pop('name')
    if not container.defined:
        if container.create('download', 0, payload):
            return jsonify({'message': 'container created'})
        else:
            return jsonify({'message': 'creation failed'})
    else:
        return jsonify({"message": "container already exists"})
```


```json
{
  "message": "container created"
}
```


```log
 * Detected change in '/root/gitclone/playground/reading/52_Containerization_with_LXC/lxc-rest/app.p
y', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 195-016-110
Using image from local cache
Unpacking the rootfs

---
You just created an Ubuntu jammy amd64 (20260221_07:42) container.

To enable SSH, run: apt install openssh-server
No default root or user password are set by LXC.
127.0.0.1 - - [22/Feb/2026 13:44:34] "POST /build HTTP/1.1" 200 -
```
