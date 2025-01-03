CONF_DIR="/root/config"
setting_files=("1_install_package.sh" "2_global_setting.sh" "3_bashrc_setting.sh" "4_git_config_setting.sh" "5_add_git_repo.sh" "6_httpd_setting.sh")
for value in "${setting_files[@]}"; do
    sh "$CONF_DIR/$value"
done
