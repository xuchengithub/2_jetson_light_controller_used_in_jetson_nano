2_jetson_light_controller
参考链接
Jetson Nano: Keeping Time Updated After Reboot

时间同步设置说明
选项：使用更好的 NTP 服务器

推荐的 NTP 服务器：

us.pool.ntp.org：适合美国用户。
pool.ntp.org：全球通用的 NTP 服务器。
time.windows.com：微软提供的时间服务器。
步骤：

确保已安装 ntpdate：

bash
复制代码
sudo apt install ntpdate
在启动脚本或登录脚本中添加以下命令：

bash
复制代码
sudo ntpdate us.pool.ntp.org
注意：

systemd 默认运行其内置的 NTP 客户端/守护程序，而不是经典的 ntpd。

可以通过以下命令检查系统的时间同步服务状态：

bash
复制代码
systemctl status systemd-timesyncd.service
输出示例：

yaml
复制代码
● systemd-timesyncd.service - Network Time Synchronization
   Loaded: loaded (/lib/systemd/system/systemd-timesyncd.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-06-26 17:39:08 PDT; 16h ago
配置 /etc/systemd/timesyncd.conf 文件： 在文件中添加以下行：

conf
复制代码
NTP=pool.ntp.org
重新加载服务以使配置生效：

bash
复制代码
sudo systemctl restart systemd-timesyncd.service
安装 Chromium 浏览器
通过以下命令安装 Chromium 浏览器：

bash
复制代码
sudo apt-get install chromium-browser -y

