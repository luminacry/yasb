"""Small runtime translation helper for user-facing UI text."""

from __future__ import annotations

import locale
import os
import sys


def _windows_ui_language() -> str:
    if sys.platform != "win32":
        return ""
    try:
        import ctypes

        language_name = ctypes.create_unicode_buffer(85)
        length = ctypes.c_ulong(len(language_name))
        ok = ctypes.windll.kernel32.LCIDToLocaleName(
            ctypes.windll.kernel32.GetUserDefaultUILanguage(),
            language_name,
            length,
            0,
        )
        if ok:
            return language_name.value
    except Exception:
        return ""
    return ""


def _language() -> str:
    requested = (os.getenv("YASB_LANGUAGE") or os.getenv("YASB_LANG") or "auto").strip().lower()
    if requested in {"zh", "zh_cn", "zh-cn", "cn", "chinese", "simplified chinese"}:
        return "zh_CN"
    if requested and requested != "auto":
        return "en"

    probes = [
        os.getenv("LANGUAGE", ""),
        os.getenv("LANG", ""),
        locale.getlocale()[0] or "",
        locale.getlocale(locale.LC_CTYPE)[0] or "",
        locale.getencoding(),
        _windows_ui_language(),
    ]
    probe = " ".join(probes).lower()
    if any(marker in probe for marker in ("zh", "chinese", "中文")):
        return "zh_CN"
    return "en"


_ZH_CN = {
    "Welcome to {app}": "欢迎使用 {app}",
    "Let's get your bar set up. Some essential widgets are already included.\nYou can customise everything later in the config file.": "先把状态栏基础配置好。常用组件已经预先包含。\n以后你可以在配置文件里继续细调。",
    "Get Started": "开始设置",
    "Skip and create minimal configuration": "跳过并创建最小配置",
    "Fonts & Icons": "字体与图标",
    "YASB requires specific fonts for the bar and UI icons. Missing fonts will be downloaded and installed for your user account.": "YASB 需要特定字体来显示状态栏和界面图标。缺少的字体会下载并安装到当前用户。",
    "JetBrains Mono Nerd Font": "JetBrains Mono Nerd Font",
    "Segoe Fluent Icons": "Segoe Fluent Icons",
    "Bar font with 10,000+ icons from popular icon sets": "状态栏字体，包含 10,000+ 常用图标",
    "System icon font used for UI elements": "用于界面元素的系统图标字体",
    "Back": "上一步",
    "Next": "下一步",
    "Install": "安装",
    "Installed": "已安装",
    "Will be installed": "将安装",
    "Checking requirements...": "正在检查必要组件...",
    "Downloading JetBrains Mono Nerd Font...": "正在下载 JetBrains Mono Nerd Font...",
    "Installing JetBrains Mono Nerd Font...": "正在安装 JetBrains Mono Nerd Font...",
    "Downloading Segoe Fluent Icons...": "正在下载 Segoe Fluent Icons...",
    "Installing Segoe Fluent Icons...": "正在安装 Segoe Fluent Icons...",
    "Finalizing installation...": "正在完成安装...",
    "All fonts installed successfully.": "所有字体已成功安装。",
    "Installation cancelled.": "安装已取消。",
    "Font Installation Failed": "字体安装失败",
    "{message}\n\nYou can retry.": "{message}\n\n你可以重试。",
    "Retry": "重试",
    "OK": "确定",
    "Unable to connect. Check your internet connection and try again.": "无法连接。请检查网络后重试。",
    "Connection timed out. Please check your network and try again.": "连接超时。请检查网络后重试。",
    "Unable to download fonts. Check your internet connection and try again.": "无法下载字体。请检查网络后重试。",
    "Download failed ({error}). The file may no longer be available.": "下载失败（{error}）。文件可能已不可用。",
    "Permission denied. Close any apps using the font and try again.": "权限不足。请关闭正在使用该字体的应用后重试。",
    "A file system error occurred while installing fonts.": "安装字体时发生文件系统错误。",
    "An unexpected error occurred while installing fonts.": "安装字体时发生未知错误。",
    "Tiling Window Manager": "平铺窗口管理器",
    "A tiling window manager automatically arranges your windows.\nYASB can show workspaces and controls for Komorebi and GlazeWM. If you don't use one, select Skip.": "平铺窗口管理器会自动排列窗口。\nYASB 可以显示 Komorebi 和 GlazeWM 的工作区与控制项。如果你不用这类工具，选择“跳过”。",
    "Skip": "跳过",
    "I don't use a tiling window manager": "我不使用平铺窗口管理器",
    "Workspace switcher with per-workspace app icons and scroll support": "工作区切换器，支持每个工作区的应用图标和滚轮切换",
    "Workspace switcher - click to switch, scroll to cycle workspaces": "工作区切换器，点击切换，滚轮循环切换",
    "Virtual Desktops": "虚拟桌面",
    "Native Windows desktops - switch, rename, create and delete": "Windows 原生虚拟桌面：切换、重命名、创建和删除",
    "Optional Widgets": "可选组件",
    "Choose additional widgets to add to your bar. Essential widgets are included by default.": "选择要添加到状态栏的额外组件。基础组件默认已包含。",
    "Real-time CPU usage with histogram and popup graph": "实时 CPU 使用率，带直方图和弹出图表",
    "RAM usage percentage and free memory display": "显示内存占用百分比和可用内存",
    "Quick Launch": "快速启动",
    "Spotlight-style search for apps, files and more": "类似 Spotlight 的应用、文件等搜索入口",
    "Active Window": "当前窗口",
    "Title and icon of the currently focused window": "显示当前焦点窗口的标题和图标",
    "Systray": "系统托盘",
    "System tray icons pinned directly to the bar": "把系统托盘图标直接固定到状态栏",
    "Weather": "天气",
    "7-day forecast via Open-Meteo, no API key needed": "通过 Open-Meteo 显示 7 天天气预报，无需 API Key",
    "GitHub": "GitHub",
    "Unread count with popup grouped by repo and type": "按仓库和类型分组显示未读通知",
    "Microphone": "麦克风",
    "Mic mute and input level, scroll to adjust volume": "麦克风静音和输入音量，支持滚轮调节",
    "Media": "媒体",
    "Now playing track with popup playback controls": "显示正在播放的曲目，并提供弹出播放控制",
    "Quick Launch is configured to show on <b>Alt+Space</b>.": "快速启动已配置为按 <b>Alt+Space</b> 打开。",
    "Display & Effects": "显示与效果",
    "Choose which screen to show the bar on and configure visual effects.": "选择状态栏显示在哪个屏幕，并配置视觉效果。",
    "All screens": "所有屏幕",
    "Primary": "主屏幕",
    "Show bar on": "状态栏显示在",
    "Select which monitor displays the bar": "选择在哪个显示器上显示状态栏",
    "Bar style": "状态栏样式",
    "Floating": "悬浮",
    "Taskbar": "贴边",
    "Floating adds spacing around the bar, taskbar sits flush against the edge.": "悬浮样式会在状态栏周围留出间距，贴边样式会紧贴屏幕边缘。",
    "Enable blur effect": "启用模糊效果",
    "Applies a blur-behind effect to the background of the bar.": "给状态栏背景应用背景模糊效果。",
    "Bar opacity": "状态栏透明度",
    "Set the background opacity of the bar.": "设置状态栏背景透明度。",
    "On": "开",
    "Off": "关",
    "All Set!": "设置完成！",
    "Visit the documentation to learn more about customization and styling.": "查看文档，了解更多自定义和样式配置。",
    "Documentation": "文档",
    "Start YASB": "启动 YASB",
    "Configuration Error": "配置错误",
    "Failed to save configuration:\n{error}": "保存配置失败：\n{error}",
    "Update available": "有可用更新",
    "Update Available": "有可用更新",
    "Open Config": "打开配置",
    "Get Themes": "获取主题",
    "Reload YASB": "重载 YASB",
    "Start Komorebi": "启动 Komorebi",
    "Stop Komorebi": "停止 Komorebi",
    "Reload Komorebi": "重载 Komorebi",
    "Start GlazeWM": "启动 GlazeWM",
    "Stop GlazeWM": "停止 GlazeWM",
    "Reload GlazeWM": "重载 GlazeWM",
    "Disable Autostart": "关闭开机自启",
    "Enable Autostart": "开启开机自启",
    "Help": "帮助",
    "About": "关于",
    "Exit": "退出",
    "Bar: {name}": "状态栏：{name}",
    "Active Widgets": "活动组件",
    "No active widgets": "没有活动组件",
    "  No active widgets": "  没有活动组件",
    "{layout} Layout": "{layout} 区域",
    "Left": "左侧",
    "Center": "中间",
    "Right": "右侧",
    "Task Manager": "任务管理器",
    "Take Screenshot": "截取状态栏截图",
    "Enable Auto Hide": "启用自动隐藏",
    "Disable Auto Hide": "关闭自动隐藏",
    "Reload Bar": "重载状态栏",
    "About {app}": "关于 {app}",
    "Check for Updates": "检查更新",
    "Checking for Updates": "正在检查更新",
    "New Update Available": "发现新版本",
    "Updates disabled": "更新已禁用",
    "Automatic updates are disabled for PR build.": "PR 构建版本已禁用自动更新。",
    "Install YASB to enable automatic updates.": "安装 YASB 后可启用自动更新。",
    "Version {version}{arch} ({channel})": "版本 {version}{arch}（{channel}）",
    "View PR Details": "查看 PR 详情",
    "View Release Notes": "查看发布说明",
    "Themes": "主题",
    "Support the Project": "支持项目",
    "Contributors": "贡献者",
    "You're on the latest version": "已经是最新版本",
    "Update Check Failed": "检查更新失败",
    "You already have the latest version ({version})": "你已经在使用最新版本（{version}）",
    "GitHub returned an error while checking for updates.": "检查更新时 GitHub 返回错误。",
    "Couldn't reach GitHub. Check your internet connection and try again.": "无法连接 GitHub。请检查网络后重试。",
    "Check for Updates": "检查更新",
    "Download and Install": "下载并安装",
    "Close": "关闭",
    "Update Available": "有可用更新",
    "New Preview Build ({version})": "新的预览构建（{version}）",
    "Version {version}": "版本 {version}",
    "{version_display} - {arch}": "{version_display} - {arch}",
    "_No changelog provided._": "_没有提供更新日志。_",
    "Downloading...": "正在下载...",
    "Downloading update...": "正在下载更新...",
    "Cancelling download.": "正在取消下载。",
    "Download cancelled.": "下载已取消。",
    "Download failed: {details}": "下载失败：{details}",
    "Download failed: installer file is incomplete. Please try again.": "下载失败：安装包不完整。请重试。",
    "Unknown error": "未知错误",
    "Launching installer...": "正在启动安装程序...",
    "Download complete. Launching installer...": "下载完成。正在启动安装程序...",
    "Cancel": "取消",
    "YASB Themes": "YASB 主题",
    "Backup your config before installing a theme.": "安装主题前请先备份配置。",
    "Backup": "备份",
    "Backup complete!": "备份完成！",
    "Backup failed: {error}": "备份失败：{error}",
    "Restore": "恢复",
    "Restoring...": "正在恢复...",
    "Restore complete!": "恢复完成！",
    "Restore failed: backup files missing.": "恢复失败：缺少备份文件。",
    "Restore failed: {error}": "恢复失败：{error}",
    "Search themes...": "搜索主题...",
    "Report": "报告问题",
    "disabled": "已禁用",
    "This theme is temporarily disabled until the author fixes the problem.": "此主题已暂时禁用，等待作者修复问题。",
    "Theme not found": "未找到主题",
    "View on GitHub": "在 GitHub 查看",
    "Install Theme": "安装主题",
    "by {author}": "作者：{author}",
    "Install Theme": "安装主题",
    "Are you sure you want to install <b>{name}</b>?<br>This will overwrite your current config and styles files.<br>Note: Some themes require additional fonts.": "确定要安装 <b>{name}</b> 吗？<br>这会覆盖当前的配置和样式文件。<br>注意：部分主题需要额外字体。",
    "Failed to load themes.": "加载主题失败。",
    "Failed to install theme: {error}": "安装主题失败：{error}",
    "Error": "错误",
    "OK": "确定",
    "User Home": "用户主页",
    "Download": "下载",
    "Documents": "文档",
    "Pictures": "图片",
    "Lock": "锁定",
    "Sign out": "注销",
    "Sleep": "睡眠",
    "Hibernate": "休眠",
    "Restart": "重启",
    "Shut Down": "关机",
    "Search applications...": "搜索应用...",
    "notifications": "条通知",
    "Min": "最低",
    "Max": "最高",
    "Humidity": "湿度",
}


def tr(text: str, **kwargs: object) -> str:
    """Translate *text* for the active UI language, then format it."""

    template = _ZH_CN.get(text, text) if _language() == "zh_CN" else text
    if kwargs:
        return template.format(**kwargs)
    return template
