if grep -w HISTTIMEFORMAT /etc/profile
then :
else
    echo "setting histtimeformat"
    echo 'HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "' >> /etc/profile
fi
