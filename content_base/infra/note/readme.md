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
