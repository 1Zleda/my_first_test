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


Agent驱动测试数据生成系统
运用agent可以加快测试进度，提高效率，若手工造数据，会浪费些时间去想，整理，agent可以几秒生成，还能自动的测试

实现步骤

1. 在 Coze 平台创建智能体

在 Coze 中创建一个“智能体”（Bot），命名为 测试数据生成助手。

2. 编写提示词（人设与回复逻辑）

在智能体的“人设与回复逻辑”中，输入以下内容：

```
你是一个测试数据生成助手。根据用户输入的内容，返回对应的 JSON 数据。

规则：
- 输入包含"用户" → 返回 {"name":"张三","age":25,"email":"zhangsan@test.com"}
- 输入包含"订单" → 返回 {"order_id":"ORD001","amount":99.9,"status":"已支付"}
- 输入包含"帖子" → 返回 {"id":1001,"title":"测试标题","content":"测试内容"}

如果以上都不包含 → 返回 {"error":"不支持的类型"}

重要：只返回纯 JSON，不要有任何解释文字。
```

3. 测试智能体

在右侧预览窗口输入“用户”、“订单”、“帖子”，验证返回的 JSON 数据是否正确。

示例：输入“用户”

```json
{"name":"张三","age":25,"email":"zhangsan@test.com"}
```

示例：输入“订单”

```json
{"order_id":"ORD001","amount":99.9,"status":"已支付"}
```

4. 将生成的数据保存到测试项目

将智能体生成的 JSON 数据分别保存为 user.json、order.json、post.json，存放在项目的 agent_data/ 目录下。

5. 编写 pytest 校验脚本

创建 test_agent_data.py，读取 JSON 文件并验证数据完整性：

```python
import json
import pytest
import os

def load_json(filename):
    filepath = os.path.join("agent_data", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def test_user_data():
    data = load_json("user.json")
    assert "name" in data
    assert "age" in data
    assert "email" in data
    assert data["age"] > 0
    assert "@" in data["email"]

def test_order_data():
    data = load_json("order.json")
    assert "order_id" in data
    assert "amount" in data
    assert "status" in data
    assert data["amount"] > 0

def test_post_data():
    data = load_json("post.json")
    assert "id" in data
    assert "title" in data
    assert "content" in data
```

6. 运行测试

```bash
pytest test_agent_data.py -v -s
```

所有测试通过，说明 Agent 生成的数据可以被自动化测试用例直接使用。

7. 成果

数据类型 校验结果 说明
用户  PASSED 字段完整：name、age、email
订单  PASSED 字段完整：order_id、amount、status
帖子  PASSED 字段完整：id、title、content

结论：Agent 生成的 JSON 数据格式正确、字段完整，可直接用于接口自动化测试。

GitHub链接：
GitHub - 1Zleda/my_first_test · GitHub

