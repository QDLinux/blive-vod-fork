<div align="center">

<h1>Blive-Vod</h1>

<p><strong>阿B直播弹幕点歌机</strong></p>

<p>
  <a href="https://github.com/QDLinux/blive-vod-fork/releases/latest"><img src="https://img.shields.io/github/v/release/QDLinux/blive-vod-fork?style=flat-square&label=Release" alt="Latest release"></a>
  <a href="https://github.com/QDLinux/blive-vod-fork/releases/latest"><img src="https://img.shields.io/github/downloads/QDLinux/blive-vod-fork/total?style=flat-square&label=Downloads" alt="Downloads"></a>
  <a href="https://t.me/blive_vod"><img src="https://img.shields.io/badge/Telegram-%E5%8A%A0%E5%85%A5%E9%A2%91%E9%81%93-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram channel"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/QDLinux/blive-vod-fork?style=flat-square" alt="License"></a>
</p>

<p>
  <a href="https://github.com/QDLinux/blive-vod-fork/releases/latest"><strong>下载最新版</strong></a>
  ·
  <a href="https://t.me/blive_vod"><strong>Telegram 频道</strong></a>
  ·
  <a href="https://github.com/QDLinux/blive-vod-fork/issues"><strong>问题反馈</strong></a>
</p>

</div>

> [!IMPORTANT]
> 项目仍在开发测试阶段，建议具备一定计算机基础的用户使用。版本发布和 Windows EXE 下载通知会同步至 [Telegram 频道](https://t.me/blive_vod)。

## v2.15 发布说明

v2.15 将点歌机从控制台程序调整为 Windows 图形窗口程序。运行 `blive-vod.exe` 后不会再弹出 cmd 窗口，主窗口会显示运行状态、登录提示和点歌结果。

### 本版本更新

- 使用 Windows GUI 子系统打包，启动后不再显示 cmd 窗口。
- 新增原生运行窗口，集中显示监听状态和应用日志。
- 房间号输入、登录账号确认改为图形对话框。
- 点歌后显示歌曲搜索结果及提交到 LX Music 是否成功。
- 移除编码后的 LX Music URL 输出。
- 过滤未处理弹幕协议等无关日志，减少窗口噪声。
- 发布包为单文件 `blive-vod.exe`，无需安装 Python。

### 使用前提

- Windows 10/11 x64
- 已安装并运行 LX Music Desktop 2.8.0 或更高版本
- 首次运行需要完成 B 站扫码登录

下载发布包后，先启动 LX Music，再运行 `blive-vod.exe`。首次运行会在程序目录生成本地配置文件；`config.json`、Cookie 和歌曲黑名单属于本地数据，不应提交到 GitHub。

## 免责声明

本软件仅供学习交流使用，请于下载后24小时内删除，不得用于任何商业用途，否则后果自负。

## 功能特性

- [x] 实时监控直播间弹幕
- [x] 弹幕点歌（支持指定歌手）
- [x] 弹幕切歌（房管权限）
- [x] 歌曲黑名单过滤
- [x] **B站自动登录**（扫码登录 + Cookie持久化 + 自动刷新）
- [x] **多源音乐搜索**（酷狗 → 网易云 → QQ音乐，优先级依次降低）
- [x] **稍后播放模式**（点歌不打断当前播放，排队等待）
- [x] **房间号自动获取**（登录后自动获取账号直播间号）
- [x] 浏览器扫码登录页面（美观的二维码展示）
- [x] 异步点歌处理（不阻塞弹幕监听）
- [x] **打包为单个 EXE**（无需 Python 环境，开箱即用）
- [ ] 前端展示歌单
- [ ] 制作UI

## 快速开始

### 方式一：直接使用 EXE（推荐，无需 Python）

1. 启动 [落雪音乐桌面版](https://github.com/lyswhut/lx-music-desktop/releases) 2.8.0+（**必须先启动！**）
2. 双击 `blive-vod.exe` 运行
3. 首次启动：
   - 自动在浏览器中打开扫码登录页面
   - 用B站APP扫码登录（登录成功后页面自动关闭）
   - 自动获取登录账号的直播间号
4. 首次运行会自动生成 `config.json` 和 `.A歌曲黑名单.txt`（与 exe 同级目录）

### 方式二：源码运行

#### 环境要求
- Windows 10/11 x64
- Python 3.9+ ([下载地址](https://www.python.org/downloads/windows/))
- [落雪音乐桌面版](https://github.com/lyswhut/lx-music-desktop/releases) 2.8.0+

#### 安装步骤

1. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **下载并安装落雪音乐**
   - 前往 [LX Music Releases](https://github.com/lyswhut/lx-music-desktop/releases) 下载最新版本

3. **启动程序**
   - 先启动落雪音乐（**必须先启动！**）
   - 运行 `python main.py`
   - 首次启动：
     - 自动在浏览器中打开扫码登录页面
     - 用B站APP扫码登录（登录成功后页面自动关闭）
     - 自动获取登录账号的直播间号

### 自行打包 EXE

```bash
cd package-exe
python build.py
```

打包完成后，`package-exe/dist/blive-vod.exe` 即为单文件可执行程序，复制到任意 Windows 电脑即可运行（无需 Python 环境）。详见 [package-exe/README.md](package-exe/README.md)。

### 使用说明

#### 弹幕点歌
在直播间发送弹幕：
- `点歌 青花瓷` - 搜索并播放"青花瓷"
- `点歌 青花瓷 周杰伦` - 指定歌手，更精确

点歌不会打断当前播放的歌曲，会排队等待当前歌曲播放完毕后再播放。

搜索优先级：酷狗 → 网易云 → QQ音乐，找到即播放，无需等待所有源返回。

#### 弹幕切歌（房管专属）
拥有房管权限的用户发送：`下一首`

#### 登录管理
- 首次启动自动弹出浏览器扫码页面
- 再次启动时检测已保存账号，询问是否继续使用
- 选择"否"则重新扫码登录新账号
- Cookie自动刷新，无需频繁登录

#### 歌曲黑名单
编辑 `.A歌曲黑名单.txt` 文件，一行一个歌名，在黑名单中的歌曲不会被点播。
**注意**：修改后需重启程序生效。

#### 命令行参数
```bash
# 直接指定房间号启动
python main.py 房间号
```

## 文件说明

```
blive-vod-fork/
├── main.py              # 主程序入口
├── app_dir.py           # 应用目录工具（兼容打包/源码运行）
├── bili_login.py        # B站登录模块（扫码/Cookie管理）
├── qr_page.py           # 二维码展示页面（本地HTTP服务器）
├── kg_search.py         # 酷狗音乐搜索模块
├── wy_search.py         # 网易云音乐搜索模块
├── tx_search.py         # QQ音乐搜索模块
├── song_handler.py      # 搜索结果处理（统一播放接口）
├── lxmusic.py           # LX Music Scheme URL封装
├── config.py            # 配置文件 / 黑名单自动生成
├── blivedm/             # B站直播弹幕客户端库
├── package-exe/         # EXE 打包脚本
├── config.json          # 配置文件（自动生成，含Cookie）
├── .A歌曲黑名单.txt     # 歌曲黑名单（自动生成）
└── requirements.txt     # Python依赖列表
```

## 常见问题

### Q: 落雪音乐无法播放歌曲？
A: 参考 [LX Music Issues #5](https://github.com/lyswhut/lx-music-desktop/issues/5#issuecomment-2099784225)

### Q: 弹幕用户名显示为打码状态？
A: 首次启动时扫码登录B站账号即可显示完整用户名。登录信息会自动保存，后续启动无需重新登录。

### Q: Cookie过期怎么办？
A: 程序会自动检测并刷新Cookie。如果刷新失败，会提示重新扫码登录。

### Q: 如何更换监听的直播间？
A: 修改 `config.json` 中的 `roomid` 字段，或删除该字段后重启程序重新输入。

## 问题反馈

- 使用问题与功能建议：[GitHub Issues](https://github.com/QDLinux/blive-vod-fork/issues)
- 版本发布与 EXE 同步：[Telegram 频道](https://t.me/blive_vod)

## 致谢

- 原项目：[xuan06zyx/blive-vod](https://github.com/xuan06zyx/blive-vod)
- B站直播弹幕库：[xfgryujk/blivedm](https://github.com/xfgryujk/blivedm)
- 音乐播放器：[lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop)

<br>
<div align="center">
  <strong>如果这个项目对你有帮助，欢迎点个 Star。</strong>
</div>
