CONF_DIR="/root/config"
TARGET_DIR="/home/vagrant"
SHELL_DIR="$TARGET_DIR/shell"
SHELL_FILE_NAME="git_commit_hist.sh"
GIT_CONF_FILE="$TARGET_DIR/.gitconfig"
if [ -d "$SHELL_DIR" ]
then
    echo "$SHELL_DIR" exists
else
    mkdir -p "$SHELL_DIR"
    cp "$CONF_DIR/$SHELL_FILE_NAME" "$SHELL_DIR/$SHELL_FILE_NAME"
    chown -R vagrant:vagrant "$SHELL_DIR"
    chmod +x "$SHELL_DIR/$SHELL_FILE_NAME"
fi
if [ -f "$GIT_CONF_FILE" ]
then
    echo "$GIT_CONF_FILE" exists
else
    cat "$CONF_DIR/dot_gitconfig" >> "$GIT_CONF_FILE"
fi
