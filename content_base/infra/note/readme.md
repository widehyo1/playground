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

>Debian-based Linux distributions
>Add the following line to your /etc/apt/sources.list. For Debian 11 and older, replace '<mydist>' with 'bullseye', 'buster', or 'stretch'. For Ubuntu 22.04 and older, 'replace '<mydist>' with 'jammy', 'eoan', 'bionic', 'xenial',
>
>deb [arch=amd64 signed-by=/usr/share/keyrings/oracle-virtualbox-2016.gpg] https://download.virtualbox.org/virtualbox/debian <mydist> contrib
>The Oracle public key for verifying the signatures can be downloaded here. You can add these keys with
>
>sudo gpg --yes --output /usr/share/keyrings/oracle-virtualbox-2016.gpg --dearmor oracle_vbox_2016.asc
>or combine downloading and registering:
>
>wget -O- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --yes --output /usr/share/keyrings/oracle-virtualbox-2016.gpg --dearmor
>The key fingerprint for oracle_vbox_2016.asc is
>
>B9F8 D658 297A F3EF C18D  5CDF A2F6 83C5 2980 AECF
>Oracle Corporation (VirtualBox archive signing key) <info@virtualbox.org>
>To install VirtualBox, do
>
>sudo apt-get update
>sudo apt-get install virtualbox-7.1

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
>Oracle Linux
>Users of Oracle Linux 7, 8 and 9 can use the Oracle Linux yum repository and enable the ol7_developer channel for Oracle Linux 7, the ol8_developer channel for Oracle Linux 8, or the ol9_developer channel for Oracle Linux 9.
>
>This can be done with
>
>yum install oraclelinux-developer-release-*
>After that, do
>
>yum install VirtualBox-7.0
>to get the latest maintenance release of VirtualBox 7.0.x installed.

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
