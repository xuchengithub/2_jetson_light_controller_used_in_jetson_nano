# 2_jetson_light_controller

## Reference
[Jetson Nano: Keeping Time Updated After Reboot](https://forums.developer.nvidia.com/t/jetson-nano-keeping-time-updated-after-reboot/72380/7)

---

## Time Synchronization Setup

### Use a Better NTP Server

Recommended NTP servers:
- **us.pool.ntp.org**: Great for users in the United States.
- **pool.ntp.org**: A globally reliable NTP mirror.
- **time.windows.com**: Microsoft's time server.

### Steps:
1. Install `ntpdate` if not already installed:
   ```bash
   sudo apt install ntpdate
