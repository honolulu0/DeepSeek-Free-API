# geo-server 运维手册

## 服务器信息

| 环境 | IP | 用户 | Java 路径 | 服务目录 | Spring Profile |
|------|-----|------|-----------|----------|----------------|
| 正式服 | 8.147.58.127 | root | /opt/jdk-17.0.17/bin/java | /opt/java | prod |
| 测试服 | 121.43.118.214 | root | - | /opt/java | test |

## 启动命令

```bash
cd /opt/java

# 正式服
nohup /opt/jdk-17.0.17/bin/java -jar geo-server.jar --spring.profiles.active=prod > prod.log 2>&1 &

# 测试服
nohup java -jar geo-server.jar --spring.profiles.active=test > test.log 2>&1 &
```

## 停止命令

```bash
ps -ef | grep geo-server.jar | grep -v grep | awk '{print $2}' | xargs kill -9
```

## 重启（先停后启）

```bash
cd /opt/java
ps -ef | grep geo-server.jar | grep -v grep | awk '{print $2}' | xargs kill -9
sleep 2
nohup /opt/jdk-17.0.17/bin/java -jar geo-server.jar --spring.profiles.active=prod > prod.log 2>&1 &
```

## 使用脚本（正式服）

正式服有管理脚本 `/opt/java/run_app.sh`：

```bash
cd /opt/java
./run_app.sh start prod      # 启动
./run_app.sh stop             # 停止
./run_app.sh restart prod     # 重启
./run_app.sh status           # 查看状态
```

## 查看日志

```bash
tail -f /opt/java/log/geo-server.log
```

## 注意事项

- 正式服通过 sudo 执行时 java 不在 PATH 中，需使用绝对路径 `/opt/jdk-17.0.17/bin/java`
- 服务目录下有历史 jar 包备份（如 geo-server.jar.0206），按日期命名
