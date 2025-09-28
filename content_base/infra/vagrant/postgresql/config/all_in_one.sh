CONF_DIR="/root/config"
setting_files=("1_install_package.sh" "2_global_setting.sh" "5_postgresql_setting.sh")
for value in "${setting_files[@]}"; do
    echo wokring on "$CONF_DIR/$value"...
    sh "$CONF_DIR/$value"
    echo done
    echo
done
