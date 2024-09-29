# openEuler 系统跨版本升级工具

## 概述

本项目提供了一个 Bash 脚本，用于将 openEuler 操作系统从 22.03 LTS 版本升级到 24.03 LTS 版本。该脚本旨在简化升级过程，并确保用户能够顺利地完成系统升级。

## 功能

- 备份现有的仓库配置文件（除了 `openEuler.repo`）。
- 修改 `openEuler.repo` 文件，注释掉 `baseurl` 行。
- 更新软件包列表并执行系统升级。
- 将所有输出记录到日志文件中。
- 提供帮助信息。

## 用法

### 基本用法

```bash
sudo ./openeuler-upgrader [版本号]
```

- `[版本号]` 是可选参数，指定要升级到的版本（例如 `24.03LTS`）。如果未提供，则默认为 `24.03LTS`。

### 查看帮助信息

```bash
./openeuler-upgrader --help
```

或

```bash
./openeuler-upgrader -h
```

### 示例

```bash
sudo ./openeuler-upgrader 24.03LTS
```

## 日志文件

- 所有标准输出和错误输出将被重定向到 `/var/log/os-upgrade.log`。
- 调试信息将被记录到 `/var/log/os-upgrade.debug.log`。

## 注意事项

- 请确保以 root 用户身份运行此脚本。
- 在运行脚本之前，请确保有足够的磁盘空间（至少 5GB）。
- 脚本会检查网络连接，确保在运行脚本时网络是可用的。


## 脚本结构

### 主要函数

- `setup_logging`: 设置日志文件和调试日志文件。
- `print_info`, `print_success`, `print_warning`, `print_error`: 美化输出信息。
- `check_root_privileges`: 检查是否以 root 用户身份运行。
- `backup_and_modify_repos`: 备份和修改仓库配置文件。
- `update_system`: 更新系统到指定版本。
- `prompt_reboot`: 提示用户重启系统以应用更改。
- `check_network_connection`: 检查网络连接。
- `check_disk_space`: 检查磁盘空间。

### 日志文件

- `/var/log/os-upgrade.log`: 包含标准输出和错误输出。
- `/var/log/os-upgrade.debug.log`: 包含调试信息。

