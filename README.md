\# 我的测试开发学习作品集



\## 项目简介

这是一个用于学习测试开发的个人项目，包含接口自动化测试、Agent 应用等内容。



\## 技术栈

\- Python 3.13

\- pytest + requests（接口自动化测试）

\- pytest-html（测试报告）

\- Coze Agent（AI 测试数据生成）



\## 项目结构

my\_first\_test/

├── test\_demo.py           # 主测试文件（10+个测试用例）

├── test\_summary.py        # 知识点总结

├── test\_with\_agent\_data.py # Agent数据整合示例

├── report.html            # pytest-html测试报告

└── README.md              # 项目说明





\## 核心能力



\### 1. 接口自动化测试

\- 使用 pytest + requests 编写接口测试

\- 参数化测试多组数据

\- fixture 管理测试前后置

\- 生成 HTML 测试报告



\### 2. 接口关联

\- 从第一个接口提取数据（如 token、id）

\- 作为第二个接口的输入参数

\- 模拟登录、创建用户等场景



\### 3. Agent 应用（AI 测试数据生成）

\- 在 Coze 平台搭建测试数据生成 Agent

\- 通过提示词控制输出格式

\- 能生成用户、帖子、订单、商品、地址等 JSON 测试数据

\- Agent 生成的数据可直接用于接口测试



\## 运行方式



```bash

\# 安装依赖

pip install pytest requests pytest-html



\# 运行测试

pytest test\_demo.py -v



\# 生成测试报告

pytest --html=report.html

