---
title: "2024 11 22 No Module Named XX Problem"
date: 2024-11-22T09:51:42+08:00
author: "武道源"
slug:
draft: false
toc: false
---

我在import Selenium时,反复报错提示No Module named "Selenium"。尝试了几个Stackoverflow上的解决办法后，终于清楚了是安装了多个Python的原因，已安装的Selenium没在Jupternotebook调用的版本中。有同样问题的，可以按照以下路径排查问题：
1. 检查已安装的包
    > 
