# 🐍 Python 数据科学起航项目 (Python_demo)

[![Learning Progress](https://img.shields.io/badge/Progress-Basic%20Syntax-green)](https://github.com/)
[![Field](https://img.shields.io/badge/Field-Data%20Science-blue)](https://github.com/)

欢迎来到我的 Python 实验室！这里是我作为“数据科学与大数据技术”专业学生，探索编程世界的起点。

## 🌟 核心技能清单
- [x] **基础交互**：利用 `input()` 获取用户信息并进行类型转换。
- [x] **异常处理**：使用 `try...except` 构建稳健的程序 (见 `BIrth.py`)。
- [x] **字符串工程**：精通切片 (Slicing)、步长 (Step) 及反转操作。
- [x] **规范命名**：遵循 PEP 8 命名准则（如 `frist_name`）。

## 📸 运行预览
<div align="center">
  <img src="./Prctures/Hello.png" alt="Hello World" width="400">
  <p><i>一切伟大的算法都始于 "Hello World!"</i></p>
</div>

## 📂 模块导航
| 文件 | 功能描述 | 核心知识点 |
| :--- | :--- | :--- |
| `BIrth.py` | 智能年龄计算器 | `try...except`, `int()` 转换 |
| `string.py` | 文本数据处理演示 | 字符串切片 `[start:end:step]` |
| `msg.py` | 动态消息生成 | f-string 格式化输出 |
| `kg.py` | 单位换算工具 | 基础算术运算与数据类型 |

## 🛠️ 常用语法速查 (Cheat Sheet)
> *数据清洗必备工具箱，代码示例参考 `string.py`*

| 类别 | 方法/操作 | 示例代码 | 功能说明 |
| :--- | :--- | :--- | :--- |
| **大小写转换** | `.upper()` | `course.upper()` | 全部转为大写（常用于标准化特征标签） |
| | `.lower()` | `course.lower()` | 全部转为小写 |
| | `.title()` | `course.title()` | 每个单词首字母大写 |
| **查找与替换** | `.find()` | `course.find('B')` | 返回字符索引位置（找不到返回 -1） |
| | `.replace()` | `s.replace('A','B')` | 替换字符串中的特定内容 |
| | `in` | `'Python' in course` | 检查是否包含某字符（返回布尔值） |
| **切片神器** | `[start:end]` | `course[0:6]` | 获取指定范围字符（**左闭右开**） |
| | `[::step]` | `course[::2]` | 设置步长取值 |
| | `[::-1]` | `course[::-1]` | **反转字符串**（数据预处理小技巧） |

## 💡 学习周记
作为未来的数据科学家，我意识到代码的健壮性（Robustness）至关重要。例如在 `BIrth.py` 中加入异常捕获，就是为了防止脏数据（Invalid Input）破坏分析流程。

---
*保持 Push 代码，记录成长的每一步！* 🚀