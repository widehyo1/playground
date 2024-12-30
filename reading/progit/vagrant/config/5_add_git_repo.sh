CONF_DIR="/root/config"
SSH_DIR="/home/git/.ssh"
if [ -d /home/git ]
then
    echo "user git exists"
else
    useradd -m -p $(perl -e 'print crypt($ARGV[0], "password")' 'gitgit') git
    mkdir /home/git/.ssh
    touch /home/git/.ssh/authorized_keys
    chown -R git:git /home/git/.ssh
    chmod 700 /home/git/.ssh
    chmod 600 /home/git/.ssh/authorized_keys
    chsh -s $(which git-shell) git
    mkdir -p /opt/git/demo_proj.git
    cd /opt/git/demo_proj.git
    git init --bare --shared
    PASSWD=$(openssl passwd -apr1 "test")
    echo "git:$PASSWD" > /opt/git/.htpasswd
    chown -R git:git /opt/git
    chmod -R 775 /opt/git/demo_proj.git/objects
    cat "$CONF_DIR/repo_owner_gitconfig" >> /home/git/.gitconfig
    chown git:git /home/git/.gitconfig
fi

