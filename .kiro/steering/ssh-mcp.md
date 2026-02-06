---
inclusion: auto
---

# SSH MCP 使用注意事项

## 环境变量问题

SSH MCP 连接使用非登录 shell，不会加载 `/etc/profile`。服务器上 JAVA_HOME 等环境变量配置在 `/etc/profile` 中。

执行需要 java、mvn 等依赖 PATH 的命令时，必须先 source 环境：

```bash
source /etc/profile && <你的命令>
```

## 服务器信息

- 测试服：ssh-test-121.43.118.214
- 正式服：ssh-prod-8.147.58.127

## geo-server 重启方式

```bash
source /etc/profile && cd /opt/java && bash run_app.sh restart prod   # 正式服
source /etc/profile && cd /opt/java && bash run_app.sh restart test   # 测试服
```
