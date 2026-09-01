import json
import pytest
import os

def load_json(filename):
    """从 agent_data 文件夹加载 JSON 文件"""
    filepath = os.path.join("agent_data", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def test_user_data():
    """验证用户数据"""
    data = load_json("user.json")
    assert "name" in data
    assert "age" in data
    assert "email" in data
    assert data["age"] > 0
    assert "@" in data["email"]
    print(f"✅ 用户数据验证通过: {data}")

def test_order_data():
    """验证订单数据"""
    data = load_json("order.json")
    assert "order_id" in data
    assert "amount" in data
    assert "status" in data
    assert data["amount"] > 0
    print(f"✅ 订单数据验证通过: {data}")

def test_post_data():
    """验证帖子数据"""
    data = load_json("post.json")
    assert "id" in data
    assert "title" in data
    assert "content" in data
    print(f"✅ 帖子数据验证通过: {data}")