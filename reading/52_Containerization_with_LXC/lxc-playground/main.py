import lxc
name = "python_container"
container = lxc.Container(name)

if not container.defined:
    if container.create("download", 0, {"dist": "ubuntu", "release": "jammy", "arch": "amd64"}):
        print("container created")
    else:
        print("Creation failed")
else:
    print("Container already exists")

container.start(useinit=False, daemonize=True)
container.running
container.state
container.init_pid
container.get_ips()
container.attach_wait(lxc.attach_run_command, ['ifconfig', 'eth0'])
container.attach_wait(lxc.attach_run_command, ['ls', '-al'], namespaces=(lxc.CLONE_NEWNS))
container.attach_wait(lxc.attach_run_command, ['ps', 'axfw'], namespaces=(lxc.CLONE_NEWNS + lxc.CLONE_NEWPID))
container.get_config_item('lxc.cgroup.memory.max')
container.set_config_item('lxc.cgroup.memory.max', '536870912')
container.append_config_item('lxc.cgroup.memory.max', '536870912')
container.save_config()
container.get_cgroup_item('memory.max')
container.set_cgroup_item('memory.max', '268435456')
container.get_cgroup_item('memory.max')
container.freeze()
container.state
container.unfreeze()
lxc.list_containers()
container.stop()
container.destroy()

