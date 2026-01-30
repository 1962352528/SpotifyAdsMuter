# Spotify Ad Muter / Spotify 自动静音助手

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English

### Introduction
This is a lightweight Python script designed to automatically mute Spotify on Windows when advertisements are playing. It restores the volume once the music resumes.

### How It Works
The script operates on a "whitelist" principle by monitoring the Spotify window title:

1.  **Detection**: It continuously checks the title of the Spotify application window.
2.  **Logic**:
    *   **Music**: If the title contains " - " (standard format: `Artist - Song`), it is considered music.
    *   **Idle**: Specific titles like "Spotify" or "Spotify Free" are considered idle states.
    *   **Ads**: Any other title that doesn't match the above patterns is treated as an advertisement.
3.  **Action**:
    *   When an ad is detected, the script uses **pycaw** (Python Core Audio Windows Library) to set the volume of the specific `Spotify.exe` process to 0.
    *   When music resumes, it restores the volume to the level it was before the ad started.

### Requirements
*   Windows OS
*   Python 3.x
*   Dependencies: `pycaw`, `pywin32`, `psutil`, `comtypes`

### Usage
1.  Install dependencies:
    ```bash
    pip install pycaw pywin32 psutil comtypes
    ```
2.  Run the script:
    ```bash
    python spotify_muter.py
    ```

---

<a name="chinese"></a>
## 中文

### 简介
这是一个轻量级的 Python 脚本，旨在 Windows 平台上自动将被检测到的 Spotify 广告静音，并在音乐恢复播放时自动还原音量。

### 工作原理
该脚本通过监控 Spotify 的窗口标题，采用“白名单”机制来工作：

1.  **检测**: 脚本会持续轮询 Spotify 应用程序的窗口标题。
2.  **判断逻辑**:
    *   **音乐**: 如果标题中包含 " - "（标准格式：`歌手 - 歌名`），则被视为正常音乐播放。
    *   **空闲**: 特定的标题如 "Spotify" 或 "Spotify Free" 被视为空闲状态。
    *   **广告**: 任何不符合上述规则的其他标题，都被默认视为广告。
3.  **执行**:
    *   当检测到广告时，脚本使用 **pycaw** (Windows 核心音频库) 将 `Spotify.exe` 进程的音量单独设置为 0。
    *   当检测到音乐恢复时，会将音量恢复到广告开始前的数值。

### 环境要求
*   Windows 操作系统
*   Python 3.x
*   依赖库: `pycaw`, `pywin32`, `psutil`, `comtypes`

### 使用方法
1.  安装依赖:
    ```bash
    pip install pycaw pywin32 psutil comtypes
    ```
2.  运行脚本:
    ```bash
    python spotify_muter.py
    ```
