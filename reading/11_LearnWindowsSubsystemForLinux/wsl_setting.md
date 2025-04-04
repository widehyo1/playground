WinKey + store 검색
windows terminal rjator
설치


윈도우 어플리케이션용 명령 줄 설치 프로그램 초콜레티(Chocolatey)로 설치
NuGet 패키징으로 설치함

1. 관리자 권한으로 파워셸 콘솔 시작
2. 파워셸 명령줄을 이용한 설치를 위한 권한 설정
Set-ExecutionPolicy Bypass -Scope Process -Force
3. 다음 명령 실행(초콜레티 설치)
$URL = 'https://chocolatey.org/install.ps1'
$Script = (New-Object System.Net.WebClient).DownloadString($URL)
Invoke-Expression -Command $String
4. 파워셸 콘솔 재시작 및 설치확인 choco --version
5. choco install microsoft-windows-terminal
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): "A"

윈도우 터미널 이용

wsl.exe -u root -d ubuntu-18.04

<C-S-,>로 설정파일 열기

```json
{
    "$help": "https://aka.ms/terminal-documentation",
    "$schema": "https://aka.ms/terminal-profiles-schema",
    "actions": 
    [
        {
            "command": 
            {
                "action": "splitPane",
                "split": "auto",
                "splitMode": "duplicate"
            },
            "id": "User.splitPane.A6751878"
        },
        {
            "command": "find",
            "id": "User.find"
        }
    ],
    "copyFormatting": "none",
    "copyOnSelect": false,
    "defaultProfile": "{51855cb2-8cce-5362-8f54-464b92b32386}",
    "keybindings": 
    [
        {
            "id": "User.splitPane.A6751878",
            "keys": "alt+shift+d"
        },
        {
            "id": null,
            "keys": "ctrl+shift+f"
        }
    ],
    "newTabMenu": 
    [
        {
            "type": "remainingProfiles"
        }
    ],
    "profiles": 
    {
        "defaults": {},
        "list": 
        [
            {
                "commandline": "%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "hidden": false,
                "name": "Windows PowerShell"
            },
            {
                "commandline": "%SystemRoot%\\System32\\cmd.exe",
                "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
                "hidden": false,
                "name": "\uba85\ub839 \ud504\ub86c\ud504\ud2b8"
            },
            {
                "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
                "hidden": false,
                "name": "Azure Cloud Shell",
                "source": "Windows.Terminal.Azure"
            },
            {
                "bellStyle": "none",
                "closeOnExit": "always",
                "colorScheme": "One Half Dark",
                "font": 
                {
                    "size": 12
                },
                "guid": "{51855cb2-8cce-5362-8f54-464b92b32386}",
                "hidden": false,
                "name": "Ubuntu",
                "source": "CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc"
            },
            {
                "guid": "{2c4de342-38b7-51cf-b940-2309a097f518}",
                "hidden": true,
                "intenseTextStyle": "none",
                "name": "Ubuntu",
                "source": "Windows.Terminal.Wsl",
                "useAcrylic": true
            }
        ]
    },
    "schemes": [],
    "themes": []
}
```

여기서 Ctrl-V를 해제한다!!!!!!!!

sudo apt update && sudo apt upgrade -y

파워셸로 WSL 설치하기
Enable-WindowsOptionFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

컴퓨터 재시작

winkey + store 검색

terminus

is available

[PS]
wsl.exe -list

wsl.exe --distrubution Ubuntu

wsl -u root -d ubuntu
passwd username

sudo apt update && sudo apt upgrade

sudo apt install


 1743  2024-09-27 01:06:25 ll
 1744  2024-09-27 01:06:30 find . -type f -name "*history*"
 1745  2024-09-27 01:06:41 grep install ./2024/04/07/history_20240407.txt
 1746  2024-09-27 01:06:56 hostnamectl
 1747  2024-09-27 01:07:39 sudo apt install vim-gtk3
 1748  2024-09-27 01:08:26 sudo apt install vim-gtk3 --fix-missing
 1749  2024-09-27 01:08:41 sudo apt install vim-gtk
 1750  2024-09-27 01:08:54 apt update
 1751  2024-09-27 01:09:00 sudo apt update
 1752  2024-09-27 01:09:13 sudo apt upgrade
 1753  2024-09-27 01:10:46 sudo apt install vim-gtk
 1754  2024-09-27 01:11:00 vim --version
 1755  2024-09-27 01:11:19 pwd
 1756  2024-09-27 01:11:21 ls

짤팁
history 설정

export HISTTIMEFORMAT="%Y-%m-%d %H:%M:%S "
export HISTFILESIZE=1000000


