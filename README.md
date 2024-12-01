# 2_jetson_light_controller

本项目为 Jetson Nano 时间同步及相关设置的指南。

## 使用更好的 NTP 时间服务器

如果需要在 Jetson Nano 上设置更可靠的时间同步，可以考虑使用更好的 NTP（网络时间协议）镜像站：

- **美国用户**：`us.pool.ntp.org`
- **全球用户**：`pool.ntp.org`
- 或者使用微软的时间服务器：`time.windows.com`

### 安装 ntpdate

首先，请确保系统安装了 `ntpdate`：

```bash
sudo apt install ntpdate

添加到启动脚本
将以下命令添加到启动脚本或登录脚本中以自动同步时间：

bash
Copy code
sudo ntpdate us.pool.ntp.org
注意事项
需要注意的是，systemd 系统会运行自己的 NTP 客户端/守护进程，而不是默认的 ntpd。例如：

bash
Copy code
systemctl status systemd-timesyncd.service
示例输出：

yaml
Copy code
● systemd-timesyncd.service - Network Time Synchronization
   Loaded: loaded (/lib/systemd/system/systemd-timesyncd.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-06-26 17:39:08 PDT; 16h ago
   ...
服务器配置文件位于 /etc/systemd/timesyncd.conf 中。

在文件中添加以下设置以使用全球通用的 NTP 服务：

makefile
Copy code
NTP=pool.ntp.org
然后重新加载服务以生效：

bash
Copy code
sudo systemctl restart systemd-timesyncd.service
安装 Chromium 浏览器
可以使用以下命令安装 Chromium 浏览器：

bash
Copy code
sudo apt-get install chromium-browser -y
