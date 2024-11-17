## prerequisite
- install virtual box
  - [Linux_Downloads – Oracle VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)
  ```bash
  $ hostnamectl
   Static hostname: Win11-01
         Icon name: computer-container
           Chassis: container
        Machine ID: 5fd73bc9d5e542ab9a843d715bd535e0
           Boot ID: 869c6a16916546f1afff409235805976
    Virtualization: wsl
  Operating System: Ubuntu 22.04.5 LTS
            Kernel: Linux 5.15.167.4-microsoft-standard-WSL2
      Architecture: x86-64
  $
  ```

> Debian-based Linux distributions
> Add the following line to your /etc/apt/sources.list. For Debian 11 and older, replace '<mydist>' with 'bullseye', 'buster', or 'stretch'. For Ubuntu 22.04 and older, 'replace '<mydist>' with 'jammy', 'eoan', 'bionic', 'xenial',
> 
> deb [arch=amd64 signed-by=/usr/share/keyrings/oracle-virtualbox-2016.gpg] https://download.virtualbox.org/virtualbox/debian <mydist> contrib
> The Oracle public key for verifying the signatures can be downloaded here. You can add these keys with
> 
> sudo gpg --yes --output /usr/share/keyrings/oracle-virtualbox-2016.gpg --dearmor oracle_vbox_2016.asc
> or combine downloading and registering:
> 
> wget -O- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --yes --output /usr/share/keyrings/oracle-virtualbox-2016.gpg --dearmor
> The key fingerprint for oracle_vbox_2016.asc is
> 
> B9F8 D658 297A F3EF C18D  5CDF A2F6 83C5 2980 AECF
> Oracle Corporation (VirtualBox archive signing key) <info@virtualbox.org>
> To install VirtualBox, do
> 
> sudo apt-get update
> sudo apt-get install virtualbox-7.1

  ```bash
$ sudo echo "deb [arch=amd64 signed-by=/usr/share/keyrings/oracle-virtualbox-2016.
gpg] https://download.virtualbox.org/virtualbox/debian jammy contrib" >> /etc/apt/sources.list
bash: /etc/apt/sources.list: Permission denied
$ sudo vi /etc/apt/sources.list
$ wget -O- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --yes --output /usr/share/keyrings/oracle-virtualbox-2016.gpg --dearmor
$ ls
$ sudo apt-get update
$ sudo apt-get install virtualbox-7.1
$ virtualbox
  ```

## install vagrant
- [Install | Vagrant | HashiCorp Developer](https://developer.hashicorp.com/vagrant/install?product_intent=vagrant#linux)

> wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
> echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
> sudo apt update && sudo apt install vagrant
  ```bash
  $ vagrant -v
  Vagrant 2.4.3
  ```

## add rocky linux 8
- [HashiCorp Cloud Platform](https://portal.cloud.hashicorp.com/vagrant/discover/rockylinux/8)
> vagrant init rockylinux/8 --box-version 9.0.0

> Vagrant.configure("2") do |config|
>   config.vm.box = "rockylinux/8"
>   config.vm.box_version = "9.0.0"
> end

> vagrant up

```bash
$ vagrant
Vagrant failed to initialize at a very early stage:

Vagrant is unable to use the VirtualBox provider from the Windows Subsystem for
Linux without access to the Windows environment. Enabling this access must be
done with caution and an understanding of the implications. For more information
on enabling Windows access and using VirtualBox from the Windows Subsystem for
Linux, please refer to the Vagrant documentation:

  https://www.vagrantup.com/docs/other/wsl.html
```

[Vagrant and Windows Subsystem for Linux | Vagrant | HashiCorp Developer](https://developer.hashicorp.com/vagrant/docs/other/wsl)
> export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
> export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox"

### install virtual box for window
[Downloads – Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads)


```bash
$ ls "/mnt/c/Program Files/Oracle/VirtualBox"
$ vi ~/.bashrc
$ source ~/.bashrc
```

---

### install virtual box for rocky linux 8.9
  - [Linux_Downloads – Oracle VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)
> Oracle Linux
> Users of Oracle Linux 7, 8 and 9 can use the Oracle Linux yum repository and enable the ol7_developer channel for Oracle Linux 7, the ol8_developer channel for Oracle Linux 8, or the ol9_developer channel for Oracle Linux 9.
> 
> This can be done with
> 
> yum install oraclelinux-developer-release-*
> After that, do
> 
> yum install VirtualBox-7.0
> to get the latest maintenance release of VirtualBox 7.0.x installed.

```bash
$ virtualbox
```

### install vagrant for rocky linux
> sudo yum install -y yum-utils
> sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
> sudo yum -y install vagrant

```bash
$ vagrant up
No usable default provider could be found for your system.

Vagrant relies on interactions with 3rd party systems, known as
"providers", to provide Vagrant with resources to run development
environments. Examples are VirtualBox, VMware, Hyper-V.

The easiest solution to this message is to install VirtualBox, which
is available for free on all major platforms.

If you believe you already have a provider available, make sure it
is properly installed and configured. You can see more details about
why a particular provider isn't working by forcing usage with
`vagrant up --provider=PROVIDER`, which should give you a more specific
error message for that particular provider.

$ vagrant up --provider=virtualbox
The provider 'virtualbox' that was requested to back the machine
'default' is reporting that it isn't usable on this system. The
reason is shown below:

VirtualBox is complaining that the kernel module is not loaded. Please
run `VBoxManage --version` or open the VirtualBox GUI to see the error
message which should contain instructions on how to fix this error.

$ VBoxManage --version
WARNING: The vboxdrv kernel module is not loaded. Either there is no module
         available for the current kernel (4.18.0-553.16.1.el8_10.x86_64) or it failed to
         load. Please recompile the kernel module and install it by

           sudo /sbin/vboxconfig

         You will not be able to start VMs until this problem is fixed.
7.0.22r165102
```


```bash
$ sudo /sbin/vboxconfig
vboxdrv.sh: Stopping VirtualBox services.
vboxdrv.sh: Starting VirtualBox services.
vboxdrv.sh: Building VirtualBox kernel modules.
This system is currently not set up to build kernel modules.
Please install the Linux kernel "header" files matching the current kernel
for adding new hardware support to the system.
The distribution packages containing the headers are probably:
    kernel-devel kernel-devel-4.18.0-553.16.1.el8_10.x86_64
This system is currently not set up to build kernel modules.
Please install the Linux kernel "header" files matching the current kernel
for adding new hardware support to the system.
The distribution packages containing the headers are probably:
    kernel-devel kernel-devel-4.18.0-553.16.1.el8_10.x86_64

There were problems setting up VirtualBox.  To re-start the set-up process, run
  /sbin/vboxconfig
as root.  If your system is using EFI Secure Boot you may need to sign the
kernel modules (vboxdrv, vboxnetflt, vboxnetadp, vboxpci) before you can load
them. Please see your Linux system's documentation for more information.

$ sudo dnf install kernel-devel kernel-devel-4.18.0-553.16.1.el8_10.x86_64
Last metadata expiration check: 0:02:33 ago on Sun 17 Nov 2024 02:38:24 PM KST.
Dependencies resolved.
==============================================================================================================================================================================================
 Package                                             Architecture                         Version                                               Repository                               Size
==============================================================================================================================================================================================
Installing:
 kernel-devel                                        x86_64                               4.18.0-553.16.1.el8_10                                baseos                                   24 M
 kernel-devel                                        x86_64                               4.18.0-553.27.1.el8_10                                baseos                                   24 M
Installing dependencies:
 libzstd-devel                                       x86_64                               1.4.4-1.el8                                           baseos                                   43 k
 m4                                                  x86_64                               1.4.18-7.el8                                          baseos                                  221 k
Installing weak dependencies:
 bison                                               x86_64                               3.0.4-10.el8                                          appstream                               687 k
 elfutils-libelf-devel                               x86_64                               0.190-2.el8                                           baseos                                   61 k
 flex                                                x86_64                               2.6.1-9.el8                                           appstream                               318 k

Transaction Summary
==============================================================================================================================================================================================
Install  7 Packages

$ sudo /sbin/vboxconfig
vboxdrv.sh: Stopping VirtualBox services.
vboxdrv.sh: Starting VirtualBox services.
vboxdrv.sh: Building VirtualBox kernel modules.


$ vagrant up
A Vagrant environment or target machine is required to run this
command. Run `vagrant init` to create a new Vagrant environment. Or,
get an ID of a target machine from `vagrant global-status` to run
this command on. A final option is to change to a directory with a
Vagrantfile and to try again.

$ vagrant init
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.

$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'base' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Box file was not detected as metadata. Adding it directly...
==> default: Adding box 'base' (v0) for provider: virtualbox
    default: Downloading: base
An error occurred while downloading the remote file. The error
message, if any, is reproduced below. Please fix this error and try
again.

Couldn't open file /home/user/gitclone/playground/content_base/infra/note/base
```



### add rocky linux 9
- [HashiCorp Cloud Platform](https://portal.cloud.hashicorp.com/vagrant/discover/rockylinux/8) < link is broken
- [HashiCorp Cloud Platform](https://portal.cloud.hashicorp.com/vagrant/discover/rockylinux/9)
> vagrant init rockylinux/9 --box-version 4.0.0

> Vagrant.configure("2") do |config|
>   config.vm.box = "rockylinux/9"
>   config.vm.box_version = "4.0.0"
> end

> vagrant up

```bash
content_base/infra/vagrant on  main [✘!?] ❯ vagrant init rockylinux/9 --box-version 4.0.0
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
content_base/infra/vagrant on  main [!?] via ⍱ v2.4.3 ❯ ll
total 4
-rw-rw-r--. 1 user user 3420 Nov 17 14:51 Vagrantfile
content_base/infra/vagrant on  main [!?] via ⍱ v2.4.3 ❯ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'rockylinux/9' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: 4.0.0
==> default: Loading metadata for box 'rockylinux/9'
    default: URL: https://vagrantcloud.com/api/v2/vagrant/rockylinux/9
==> default: Adding box 'rockylinux/9' (v4.0.0) for provider: virtualbox (amd64)
    default: Downloading: https://vagrantcloud.com/rockylinux/boxes/9/versions/4.0.0/providers/virtualbox/amd64/vagrant.box
Download redirected to host: dl.rockylinux.org
    default: Calculating and comparing box checksum...
==> default: Successfully added box 'rockylinux/9' (v4.0.0) for 'virtualbox (amd64)'!
==> default: Importing base box 'rockylinux/9'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'rockylinux/9' version '4.0.0' is up to date...
==> default: Setting the name of the VM: vagrant_default_1731822853548_98892
Vagrant is currently configured to create VirtualBox synced folders with
the `SharedFoldersEnableSymlinksCreate` option enabled. If the Vagrant
guest is not trusted, you may want to disable this option. For more
information on this option, please refer to the VirtualBox manual:

  https://www.virtualbox.org/manual/ch04.html#sharedfolders

This option can be disabled globally with an environment variable:

  VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

or on a per folder basis within the Vagrantfile:

  config.vm.synced_folder '/host/path', '/guest/path', SharedFoldersEnableSymlinksCreate: false
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /home/user/gitclone/playground/content_base/infra/vagrant => /vagrant
content_base/infra/vagrant on  main [!?] via ⍱ v2.4.3 took 2m34s ❯ ls
Vagrantfile
content_base/infra/vagrant on  main [!?] via ⍱ v2.4.3 ❯ vagrant  ssh
[vagrant@localhost ~]$ 
logout
Connection to 127.0.0.1 closed.
```

```bash
$ vagrant ssh-config --host webdb >> ~/.ssh/config
$ cat ~/.ssh/config 
Host webdb
  HostName 127.0.0.1
  User vagrant
  Port 2222
  ...
```

```bash
$ ssh webdb
Bad owner or permissions on ~/.ssh/config
$ sudo chmod go-w ~/.ssh/config
$ ssh webdb
Last login: Sun Nov 17 06:00:02 2024 from 10.0.2.2
[vagrant@localhost ~]$
logout
Connection to 127.0.0.1 closed.
```

### install docker in vagrant
- [RHEL | Docker Docs](https://docs.docker.com/engine/install/rhel/)
```bash
[vagrant@localhost ~]$ sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine \
                  podman \
                  runc

[vagrant@localhost ~]$ sudo dnf -y install dnf-plugins-core
[vagrant@localhost ~]$ sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

[vagrant@localhost ~]$ sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

[vagrant@localhost ~]$ sudo systemctl enable --now docker
```


```bash
[vagrant@localhost ~]$ sudo systemctl enable --now docker
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.
[vagrant@localhost ~]$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:305243c734571da2d100c8c8b3c3167a098cab6049c9a5b066b6021a60fcb966
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### install elastic search with docker
- [Install Elasticsearch with Docker | Elasticsearch Guide [8.16] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

> docker network create elastic
> docker pull docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> wget https://artifacts.elastic.co/cosign.pub
> cosign verify --key cosign.pub docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> docker run --name es01 --net elastic -p 9200:9200 -it -m 6GB -e "xpack.ml.use_auto_machine_memory_percent=true" docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
> 
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node
> docker run -e ENROLLMENT_TOKEN="<token>" --name es02 --net elastic -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
> 
> docker pull docker.elastic.co/kibana/kibana:8.16.0
> wget https://artifacts.elastic.co/cosign.pub
> cosign verify --key cosign.pub docker.elastic.co/kibana/kibana:8.16.0
> docker run --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.16.0
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
> 
> # Remove the Elastic network
> docker network rm elastic
> 
> # Remove Elasticsearch containers
> docker rm es01
> docker rm es02
> 
> # Remove the Kibana container
> docker rm kib01

```bash
[vagrant@localhost ~]$ docker network create elastic
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
[vagrant@localhost ~]$ sudo docker network create elastic
36ea0433c72d0be06e3f356e635fdc8e46690266e1ae468bd16f7501da56d8cb
[vagrant@localhost ~]$ docker pull docker.elastic.co/elasticsearch/elasticsearch:8.16.0
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.47/images/create?fromImage=docker.elastic.co%2Felasticsearch%2Felasticsearch&tag=8.16.0": dial unix /var/run/docker.sock: connect: permission denied
[vagrant@localhost ~]$ sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:8.16.0
8.16.0: Pulling from elasticsearch/elasticsearch
e7894aa63b6b: Pull complete 
3a11bd602b31: Pull complete 
c3ca649064d5: Pull complete 
4ca545ee6d5d: Pull complete 
bbaceb9bc3e3: Pull complete 
941573d1b9f4: Pull complete 
a27032c45257: Pull complete 
dbdca3ea852c: Pull complete 
9170f2c20f1f: Pull complete 
553e85e02c6f: Pull complete 
Digest: sha256:93a9a7e1908f0c59ffce42ff494791bd785c36de40189759fc2a0ed7d6006c9d
Status: Downloaded newer image for docker.elastic.co/elasticsearch/elasticsearch:8.16.0
docker.elastic.co/elasticsearch/elasticsearch:8.16.0
```

#### install wget and cosign
  - install wget
```bash
[vagrant@localhost ~]$ wget https://artifacts.elastic.co/cosign.pub
bash: wget: command not found
[vagrant@localhost ~]$ sudo dnf install wget
Last metadata expiration check: 0:10:33 ago on Sun 17 Nov 2024 07:04:45 AM UTC.
Dependencies resolved.
==============================================================================================================================================================================================
 Package                                  Architecture                               Version                                              Repository                                     Size
==============================================================================================================================================================================================
Installing:
 wget                                     x86_64                                     1.21.1-8.el9_4                                       appstream                                     768 k

Transaction Summary
==============================================================================================================================================================================================
Install  1 Package

```
  - [How to Install Cosign — Chainguard Academy](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-install-cosign/)
> wget "https://github.com/sigstore/cosign/releases/download/v2.0.0/cosign-linux-amd64"
> sudo mv cosign-linux-amd64 /usr/local/bin/cosign
> sudo chmod +x /usr/local/bin/cosign

```bash

[vagrant@localhost ~]$ docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.

[vagrant@localhost ~]$ sudo docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
CompileCommand: dontinline java/lang/invoke/MethodHandle.setAsTypeCache bool dontinline = true
CompileCommand: dontinline java/lang/invoke/MethodHandle.asTypeUncached bool dontinline = true
{"@timestamp":"2024-11-17T07:23:41.647Z", "log.level": "INFO", "message":"Using native vector library; to disable start with -Dorg.elasticsearch.nativeaccess.enableVectorLibrary=false", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.nativeaccess.NativeAccess","elasticsearch.node.name":"fb1c558d5756","elasticsearch.cluster.name":"docker-cluster"}
{"@timestamp":"2024-11-17T07:23:41.685Z", "log.level": "INFO", "message":"Using [jdk] native provider and native methods for [Linux]", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.nativeaccess.NativeAccess","elasticsearch.node.name":"fb1c558d5756","elasticsearch.cluster.name":"docker-cluster"}
...
{"@timestamp":"2024-11-17T07:23:52.528Z", "log.level": "INFO", "message":"Native controller process has stopped - no new native processes can be started", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"ml-cpp-log-tail-thread","log.logger":"org.elasticsearch.xpack.ml.process.NativeController","elasticsearch.node.name":"fb1c558d5756","elasticsearch.cluster.name":"docker-cluster"}

ERROR: Elasticsearch died while starting up, with exit code 78

```



> docker run --name es01 --net elastic -p 9200:9200 -it -m 6GB -e "xpack.ml.use_auto_machine_memory_percent=true" docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
> 
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node
> docker run -e ENROLLMENT_TOKEN="<token>" --name es02 --net elastic -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
> 
> docker pull docker.elastic.co/kibana/kibana:8.16.0
> wget https://artifacts.elastic.co/cosign.pub
> cosign verify --key cosign.pub docker.elastic.co/kibana/kibana:8.16.0
> docker run --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.16.0
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
> 
> # Remove the Elastic network
> docker network rm elastic
> 
> # Remove Elasticsearch containers
> docker rm es01
> docker rm es02
> 
> # Remove the Kibana container
> docker rm kib01


```bash
{"@timestamp":"2024-11-17T07:26:30.703Z", "log.level": "INFO", "message":"Native controller process has stopped - no new native processes can be started", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"ml-cpp-log-tail-thread","log.logger":"org.elasticsearch.xpack.ml.process.NativeController","elasticsearch.node.name":"2668a2add73b","elasticsearch.cluster.name":"docker-cluster"}

ERROR: Elasticsearch died while starting up, with exit code 78

[vagrant@localhost ~]$ sudo sysctl -w vm.max_map_count=262144
vm.max_map_count = 262144

[vagrant@localhost ~]$ sudo docker rm es01
es01

[vagrant@localhost ~]$ sudo docker run --name es01 --net elastic -p 9200:9200 -it -m 6GB -e "xpack.ml.use_auto_machine_memory_percent=true" docker.elastic.co/elasticsearch/elasticsearch:8.16.0

CompileCommand: dontinline java/lang/invoke/MethodHandle.setAsTypeCache bool dontinline = true
CompileCommand: dontinline java/lang/invoke/MethodHandle.asTypeUncached bool dontinline = true
{"@timestamp":"2024-11-17T07:28:27.893Z", "log.level": "INFO", "message":"Using native vector library; to disable start with -Dorg.elasticsearch.nativeaccess.enableVectorLibrary=false", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.nativeaccess.NativeAccess","elasticsearch.node.name":"c8967468ad81","elasticsearch.cluster.name":"docker-cluster"}

...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  *masked*

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  *masked*

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  *masked*

ℹ️ Configure other nodes to join this cluster:
• Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  *masked*

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.16.0`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```


```bash

[vagrant@localhost ~]$ sudo docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
Error response from daemon: container c8967468ad81204accca573e5c466a0dd918f4c3bcc315389494ef3ebce9bc51 is not running
[vagrant@localhost ~]$ sudo docker run --name es01 --net elastic -p 9200:9200 -it -m 6GB -e "xpack.ml.use_auto_machine_memory_percent=true" -d docker.elastic.co/elasticsearch/elasticsearch:8.16.0
docker: Error response from daemon: Conflict. The container name "/es01" is already in use by container "c8967468ad81204accca573e5c466a0dd918f4c3bcc315389494ef3ebce9bc51". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.

[vagrant@localhost ~]$ docker ps
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.47/containers/json": dial unix /var/run/docker.sock: connect: permission denied

[vagrant@localhost ~]$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[vagrant@localhost ~]$ id
uid=1000(vagrant) gid=1000(vagrant) groups=1000(vagrant) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
[vagrant@localhost ~]$ groups
vagrant
[vagrant@localhost ~]$ groups root
root : root
[vagrant@localhost ~]$ sudo groupadd docker
groupadd: group 'docker' already exists
[vagrant@localhost ~]$ sudo usermod -aG docker vagrant
[vagrant@localhost ~]$ groups
vagrant
[vagrant@localhost ~]$ 
logout
Connection to 127.0.0.1 closed.
playground/content_base/infra on  main [!?] took 32m19s ❯ esssh
Last login: Sun Nov 17 07:01:59 2024 from 10.0.2.2
[vagrant@localhost ~]$ groups
vagrant docker
```

> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
> 
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node
> docker run -e ENROLLMENT_TOKEN="<token>" --name es02 --net elastic -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
> 
> docker pull docker.elastic.co/kibana/kibana:8.16.0
> wget https://artifacts.elastic.co/cosign.pub
> cosign verify --key cosign.pub docker.elastic.co/kibana/kibana:8.16.0
> docker run --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.16.0
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic

> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
```
[vagrant@localhost ~]$ docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
WARNING: Owner of file [/usr/share/elasticsearch/config/users] used to be [root], but now is [elasticsearch]
WARNING: Owner of file [/usr/share/elasticsearch/config/users_roles] used to be [root], but now is [elasticsearch]
This tool will reset the password of the [elastic] user to an autogenerated value.
The password will be printed in the console.
Please confirm that you would like to continue [y/N]y


Password for the [elastic] user successfully reset.
New value: *masked*

```

```bash
[vagrant@localhost ~]$ docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
*masked*
```


.bashrc
```bash
export ELASTIC_PASSWORD="*"
export KIBANA_TOKEN="*"
```

```bash
[vagrant@localhost ~]$ ls
cosign.pub  ELK  note
[vagrant@localhost ~]$ cd ELK/
[vagrant@localhost ELK]$ ls
elasticsearch
[vagrant@localhost ELK]$ cd elasticsearch/
[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
{
  "name" : "c8967468ad81",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "*",
  "version" : {
    "number" : "8.16.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "*",
    "build_date" : "2024-11-08T10:05:56.292914697Z",
    "build_snapshot" : false,
    "lucene_version" : "9.12.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

> docker run -e ENROLLMENT_TOKEN="<token>" --name es02 --net elastic -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
```
[vagrant@localhost ~]$ docker run -e ENROLLMENT_TOKEN="$ENROLLMENT_TOKEN" --name es02 --net elastic -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.16.0
CompileCommand: dontinline java/lang/invoke/MethodHandle.setAsTypeCache bool dontinline = true
CompileCommand: dontinline java/lang/invoke/MethodHandle.asTypeUncached bool dontinline = true
{"@timestamp":"2024-11-17T07:47:18.157Z", "log.level": "INFO", "message":"Using native vector library; to disable start with -Dorg.elasticsearch.nativeaccess.enableVectorLibrary=false", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.nativeaccess.NativeAccess","elasticsearch.node.name":"70bc4bc6d3ea","elasticsearch.cluster.name":"docker-cluster"}
...
{"@timestamp":"2024-11-17T07:47:31.093Z", "log.level": "INFO", "message":"publish_address {172.18.0.3:9200}, bound_addresses {[::]:9200}", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.http.AbstractHttpServerTransport","elasticsearch.cluster.uuid":"wOUcQh8rSJKroF0XyIyn4w","elasticsearch.node.id":"BexJ1mizSaGvzft3K8mKsQ","elasticsearch.node.name":"70bc4bc6d3ea","elasticsearch.cluster.name":"docker-cluster"}
{"@timestamp":"2024-11-17T07:47:31.121Z", "log.level": "INFO", "message":"started {70bc4bc6d3ea}{BexJ1mizSaGvzft3K8mKsQ}{QRBEYro0R86DZeP9fZLE6g}{70bc4bc6d3ea}{172.18.0.3}{172.18.0.3:9300}{cdfhilmrstw}{8.16.0}{7000099-8518000}{ml.allocated_processors=2, ml.allocated_processors_double=2.0, ml.max_jvm_size=536870912, ml.config_version=12.0.0, xpack.installed=true, transform.config_version=10.0.0, ml.machine_memory=1073741824}", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.node.Node","elasticsearch.cluster.uuid":"wOUcQh8rSJKroF0XyIyn4w","elasticsearch.node.id":"BexJ1mizSaGvzft3K8mKsQ","elasticsearch.node.name":"70bc4bc6d3ea","elasticsearch.cluster.name":"docker-cluster"}

```


> curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
```bash
[vagrant@localhost ~]$ docker ps -a
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED          STATUS                            PORTS                                                 NAMES
70bc4bc6d3ea   docker.elastic.co/elasticsearch/elasticsearch:8.16.0   "/bin/tini -- /usr/l…"   2 minutes ago    Exited (130) About a minute ago                                                         es02
c8967468ad81   docker.elastic.co/elasticsearch/elasticsearch:8.16.0   "/bin/tini -- /usr/l…"   21 minutes ago   Up 12 minutes                     0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 9300/tcp   es01
94b87d8a0146   hello-world                                            "/hello"                 44 minutes ago   Exited (0) 44 minutes ago                                                               funny_almeida
[vagrant@localhost ~]$ docker start es02
es02
[vagrant@localhost ~]$ cd ELK/elasticsearch/
[vagrant@localhost elasticsearch]$ ls
http_ca.crt
[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
172.18.0.2 9 58 4 0.10 0.18 0.12 cdfhilmrstw * c8967468ad81
```

> docker pull docker.elastic.co/kibana/kibana:8.16.0
> wget https://artifacts.elastic.co/cosign.pub
> cosign verify --key cosign.pub docker.elastic.co/kibana/kibana:8.16.0
> docker run --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.16.0
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic

> docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic


```bash
[vagrant@localhost ~]$ curl -XGET https://localhost:9200
curl: (60) SSL certificate problem: self-signed certificate in certificate chain
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
[vagrant@localhost ~]$ ls
cosign.pub  elasticseach_success_private_message.txt  ELK  note
[vagrant@localhost ~]$ cd ELK/
[vagrant@localhost ELK]$ ls
elasticsearch
[vagrant@localhost ELK]$ cd elasticsearch/
[vagrant@localhost elasticsearch]$ ls
http_ca.crt
[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
172.18.0.2 14 58 0 0.00 0.03 0.06 cdfhilmrstw * c8967468ad81
[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
{
  "name" : "c8967468ad81",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "*",
  "version" : {
    "number" : "8.16.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "*",
    "build_date" : "2024-11-08T10:05:56.292914697Z",
    "build_snapshot" : false,
    "lucene_version" : "9.12.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/indices
[vagrant@localhost elasticsearch]$ 
```


#### make index and check
```bash
[vagrant@localhost elasticsearch]$ cat sample.json 
{ "settings": { "queries.cache.enabled": "true", "max_ngram_diff": 8, "max_shingle_diff": 8, "refresh_interval": "60s", "number_of_shards": 1, "number_of_replicas": 1, "analysis": { "filter": { "ngram_filter": { "type": "ngram", "min_gram": 2, "max_gram": 8, "token_chars": [ "letter", "digit" ] }, "shingle_filter": { "type": "shingle", "min_shingle_size": 2, "max_shingle_size": 8 } }, "analyzer": { "english_analyzer": { "tokenizer": "standard", "filter": [ "lowercase", "ngram_filter", "shingle_filter" ] } } } }, "mappings": { "properties": { "@timestamp": { "type": "date" }, "@version": { "type": "text", "fields": { "keyword": { "type": "keyword", "ignore_above": 256 } } }, "join_field": { "type": "join", "relations": { "parent": "child" } }, "knlg_info_id": { "type": "keyword", "ignore_above": 128 }, "korn_nm": { "type": "text", "analyzer": "english_analyzer" }, "expln": { "type": "text", "analyzer": "english_analyzer" }, "smy_cn": { "type": "text", "analyzer": "english_analyzer" }, "pstg_yn": { "type": "keyword", "ignore_above": 32 }, "rls_cd": { "type": "keyword", "ignore_above": 32 }, "kwrd_ivlst": { "type": "text", "analyzer": "english_analyzer" }, "del_yn": { "type": "keyword", "ignore_above": 32 }, "aprv_yn": { "type": "keyword", "ignore_above": 32 }, "inq_cnt": { "type": "integer" }, "dwnld_cnt": { "type": "integer" }, "frst_reg_dt": { "type": "date" }, "last_chg_dt": { "type": "date" }, "knlg_sclsf_cd": { "type": "keyword", "ignore_above": 128 }, "doc_clsf_cd": { "type": "keyword", "ignore_above": 128 }, "knlg_lclsf_cd": { "type": "keyword", "ignore_above": 128 }, "enfc_cn": { "type": "text", "analyzer": "english_analyzer" }, "page_cnt": { "type": "integer" }, "page_cn": { "type": "text", "analyzer": "english_analyzer" }, "dept_id": { "type": "keyword", "ignore_above": 256 }, "pvsn_inst_id": { "type": "keyword", "ignore_above": 256 } } } }
[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD -XPUT https://localhost:9200/sample -H "Content-Type: application/json" -d '{ "settings": { "queries.cache.enabled": "true", "max_ngram_diff": 8, "max_shingle_diff": 8, "refresh_interval": "60s", "number_of_shards": 1, "number_of_replicas": 1, "analysis": { "filter": { "ngram_filter": { "type": "ngram", "min_gram": 2, "max_gram": 8, "token_chars": [ "letter", "digit" ] }, "shingle_filter": { "type": "shingle", "min_shingle_size": 2, "max_shingle_size": 8 } }, "analyzer": { "english_analyzer": { "tokenizer": "standard", "filter": [ "lowercase", "ngram_filter", "shingle_filter" ] } } } }, "mappings": { "properties": { "@timestamp": { "type": "date" }, "@version": { "type": "text", "fields": { "keyword": { "type": "keyword", "ignore_above": 256 } } }, "join_field": { "type": "join", "relations": { "parent": "child" } }, "knlg_info_id": { "type": "keyword", "ignore_above": 128 }, "korn_nm": { "type": "text", "analyzer": "english_analyzer" }, "expln": { "type": "text", "analyzer": "english_analyzer" }, "smy_cn": { "type": "text", "analyzer": "english_analyzer" }, "pstg_yn": { "type": "keyword", "ignore_above": 32 }, "rls_cd": { "type": "keyword", "ignore_above": 32 }, "kwrd_ivlst": { "type": "text", "analyzer": "english_analyzer" }, "del_yn": { "type": "keyword", "ignore_above": 32 }, "aprv_yn": { "type": "keyword", "ignore_above": 32 }, "inq_cnt": { "type": "integer" }, "dwnld_cnt": { "type": "integer" }, "frst_reg_dt": { "type": "date" }, "last_chg_dt": { "type": "date" }, "knlg_sclsf_cd": { "type": "keyword", "ignore_above": 128 }, "doc_clsf_cd": { "type": "keyword", "ignore_above": 128 }, "knlg_lclsf_cd": { "type": "keyword", "ignore_above": 128 }, "enfc_cn": { "type": "text", "analyzer": "english_analyzer" }, "page_cnt": { "type": "integer" }, "page_cn": { "type": "text", "analyzer": "english_analyzer" }, "dept_id": { "type": "keyword", "ignore_above": 256 }, "pvsn_inst_id": { "type": "keyword", "ignore_above": 256 } } } }'
{"acknowledged":true,"shards_acknowledged":true,"index":"sample"}

[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD -XPUT https://localhost:9200/sample -H "Content-Type: application/json

[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD -XPUT https://localhost:9200/_cat/indices

{"error":"Incorrect HTTP method for uri [/_cat/indices] and method [PUT], allowed: [GET]","status":405}

[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD -XGET https://localhost:9200/_cat/indices
yellow open sample mzrTNUfFTRW7SO1sSVZScg 1 1 0 0 227b 227b 227b

[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD -XGET https://localhost:9200/sample

{"sample":{"aliases":{},"mappings":{"properties":{"@timestamp":{"type":"date"},"@version":{"type":"text","fields":{"keyword":{"type":"keyword","ignore_above":256}}},"aprv_yn":{"type":"keyword","ignore_above":32},"del_yn":{"type":"keyword","ignore_above":32},"dept_id":{"type":"keyword","ignore_above":256},"doc_clsf_cd":{"type":"keyword","ignore_above":128},"dwnld_cnt":{"type":"integer"},"enfc_cn":{"type":"text","analyzer":"english_analyzer"},"expln":{"type":"text","analyzer":"english_analyzer"},"frst_reg_dt":{"type":"date"},"inq_cnt":{"type":"integer"},"join_field":{"type":"join","eager_global_ordinals":true,"relations":{"parent":"child"}},"knlg_info_id":{"type":"keyword","ignore_above":128},"knlg_lclsf_cd":{"type":"keyword","ignore_above":128},"knlg_sclsf_cd":{"type":"keyword","ignore_above":128},"korn_nm":{"type":"text","analyzer":"english_analyzer"},"kwrd_ivlst":{"type":"text","analyzer":"english_analyzer"},"last_chg_dt":{"type":"date"},"page_cn":{"type":"text","analyzer":"english_analyzer"},"page_cnt":{"type":"integer"},"pstg_yn":{"type":"keyword","ignore_above":32},"pvsn_inst_id":{"type":"keyword","ignore_above":256},"rls_cd":{"type":"keyword","ignore_above":32},"smy_cn":{"type":"text","analyzer":"english_analyzer"}}},"settings":{"index":{"max_ngram_diff":"8","routing":{"allocation":{"include":{"_tier_preference":"data_content"}}},"refresh_interval":"60s","number_of_shards":"1","provided_name":"sample","max_shingle_diff":"8","creation_date":"1731831768047","analysis":{"filter":{"shingle_filter":{"max_shingle_size":"8","min_shingle_size":"2","type":"shingle"},"ngram_filter":{"token_chars":["letter","digit"],"min_gram":"2","type":"ngram","max_gram":"8"}},"analyzer":{"english_analyzer":{"filter":["lowercase","ngram_filter","shingle_filter"],"tokenizer":"standard"}}},"number_of_replicas":"1","queries":{"cache":{"enabled":"true"}},"uuid":"mzrTNUfFTRW7SO1sSVZScg","version":{"created":"8518000"}}}}}

[vagrant@localhost elasticsearch]$ curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD -XGET https://localhost:9200/sample?pretty
{
  "sample" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        },
        "@version" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "aprv_yn" : {
          "type" : "keyword",
          "ignore_above" : 32
        },
        "del_yn" : {
          "type" : "keyword",
          "ignore_above" : 32
        },
        "dept_id" : {
          "type" : "keyword",
          "ignore_above" : 256
        },
        "doc_clsf_cd" : {
          "type" : "keyword",
          "ignore_above" : 128
        },
        "dwnld_cnt" : {
          "type" : "integer"
        },
        "enfc_cn" : {
          "type" : "text",
          "analyzer" : "english_analyzer"
        },
        "expln" : {
          "type" : "text",
          "analyzer" : "english_analyzer"
        },
        "frst_reg_dt" : {
          "type" : "date"
        },
        "inq_cnt" : {
          "type" : "integer"
        },
        "join_field" : {
          "type" : "join",
          "eager_global_ordinals" : true,
          "relations" : {
            "parent" : "child"
          }
        },
        "knlg_info_id" : {
          "type" : "keyword",
          "ignore_above" : 128
        },
        "knlg_lclsf_cd" : {
          "type" : "keyword",
          "ignore_above" : 128
        },
        "knlg_sclsf_cd" : {
          "type" : "keyword",
          "ignore_above" : 128
        },
        "korn_nm" : {
          "type" : "text",
          "analyzer" : "english_analyzer"
        },
        "kwrd_ivlst" : {
          "type" : "text",
          "analyzer" : "english_analyzer"
        },
        "last_chg_dt" : {
          "type" : "date"
        },
        "page_cn" : {
          "type" : "text",
          "analyzer" : "english_analyzer"
        },
        "page_cnt" : {
          "type" : "integer"
        },
        "pstg_yn" : {
          "type" : "keyword",
          "ignore_above" : 32
        },
        "pvsn_inst_id" : {
          "type" : "keyword",
          "ignore_above" : 256
        },
        "rls_cd" : {
          "type" : "keyword",
          "ignore_above" : 32
        },
        "smy_cn" : {
          "type" : "text",
          "analyzer" : "english_analyzer"
        }
      }
    },
    "settings" : {
      "index" : {
        "max_ngram_diff" : "8",
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        },
        "refresh_interval" : "60s",
        "number_of_shards" : "1",
        "provided_name" : "sample",
        "max_shingle_diff" : "8",
        "creation_date" : "1731831768047",
        "analysis" : {
          "filter" : {
            "shingle_filter" : {
              "max_shingle_size" : "8",
              "min_shingle_size" : "2",
              "type" : "shingle"
            },
            "ngram_filter" : {
              "token_chars" : [
                "letter",
                "digit"
              ],
              "min_gram" : "2",
              "type" : "ngram",
              "max_gram" : "8"
            }
          },
          "analyzer" : {
            "english_analyzer" : {
              "filter" : [
                "lowercase",
                "ngram_filter",
                "shingle_filter"
              ],
              "tokenizer" : "standard"
            }
          }
        },
        "number_of_replicas" : "1",
        "queries" : {
          "cache" : {
            "enabled" : "true"
          }
        },
        "uuid" : "mzrTNUfFTRW7SO1sSVZScg",
        "version" : {
          "created" : "8518000"
        }
      }
    }
  }
}
```
