最近算法做的多了，程序很少自己动手，随便写着玩玩消遣一下，保持写代码的手感。

本文档是外星人入侵项目的开发记录文档
本项目采用git进行版本管理
本项目的文件结构如下

主程序及说明文档--------alien_invasion.py，alien_invasion.txt

设置文件及说明文档------settings.py，settings.txt

函数文件及说明文档------

类文件及说明文档--------ship.py, ship.txt记录飞船的类及其中的方法；alien.py,alien.txt记录外星人的类和方法；

                     bullet.py, bullet.txt记录子弹的类，属性和方法；button.py，button.txt记录开始按钮的类和方法。

                     scoreboard.py,scoreboard.txt记录积分系统的类和方法

资源文件夹--------------image文件夹

开发环境：
1.MacOS 10.15.5
2.Python 3.7.6

第三方模块：
1.pygame 2.0.0.dev6,及其依赖库SDL 2.0.10

开发错误记录：

1.安装环境的错误，开始使用的是pygame1.9.6版本，此版本是目前的公开稳定版，但是
由于MacOS的版本较新，此版本的存在一定的不兼容，出现的主要是问题是运行后屏幕空
白，并且不能更改背景颜色，只能显示一个白色窗口。
解决办法是安装pygame 2.0.0.dev6即可。安装命令pip3 install pygame==2.0.0.dev6


