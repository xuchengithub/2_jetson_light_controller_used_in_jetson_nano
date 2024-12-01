# us.pool.ntp.org is a pretty good pooled mirror for people in the US.
pool.ntp.org is a mirror that’s good worldwide.
Or you can pick on someone who can afford it and go to time.windows.com :-)

First, make sure you have ntpdate installed:

sudo apt install ntpdate
Then, put this in your startup scripts or login script or whatever:

sudo ntpdate us.pool.ntp.org
However, note that systemd will run its own NTP client/daemon, that’s not the default ntpd. (Just like systemd replaces DNS, and most other services you’d expect from a classic UNIX system …)

jwatte@jetson-nano:~$ systemctl status systemd-timesyncd.service
● systemd-timesyncd.service - Network Time Synchronization
   Loaded: loaded (/lib/systemd/system/systemd-timesyncd.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-06-26 17:39:08 PDT; 16h ago

The server used is configured in /etc/systemd/timesyncd.conf

Add a setting for

NTP=pool.ntp.org
and reload the service and it’ll sync from a service that exists and works.


# 安装 Chromium 浏览器
可以使用以下命令安装 Chromium 浏览器：

# bash
sudo apt-get install chromium-browser -y
