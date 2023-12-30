# tomorin-plugins
基于[TomorinBot](https://github.com/kumoSleeping/TomorinBot)制作的插件包
## 使用方法
- 克隆本项目，在本项目文件夹内运行`pip install -r requirements.txt`安装python依赖后将`plugins_ty0`文件夹塞入模板根目录
- 在模板内的`config.yml`中加入以下内容
``` yaml
    - path: 'plugins_ty0'
      priority: 1
```
## 鸣谢
- [TomorinBot](https://github.com/kumoSleeping/TomorinBot)