import requests
import pytest

#从Agent复制过来的测试数据
user_data={
       "name":"赵六",
       "age":28,
       "email":"zhaoliu@example.com",
       "phone":"13700137000"
}

post_data={
       "id":1003,
       "title":"技术分享：JSON 数据生成技巧",
       "content":"本文详细介绍了如何根据需求快速生成符合规范的 JSON 测试数据，包含多种常见类型的例。",
       "author":"李技术"
}

order_data={
         "order_id":"OD20240520001",
         "amount":299.9,
         "status":"已完成",
         "user_name":"陈七"
}

def test_use_agent_user_data():
       """使用Agent生成的用户数据测试接口"""
       #模拟用用户数据去注册或创建用户
       print(f"使用Agent生成的用户数据:{user_data}")
       assert user_data["name"]=="赵六"
       assert user_data["age"]==28
       assert "@" in user_data["email"]
       print("用户数据验证通过")

def test_use_agent_post_data():
       """使用Agent生成的帖子数据测试接口"""
       print(f"使用Agent生成的用户数据:{post_data}")
       assert post_data["id"]>0
       assert len(post_data["title"])>0
       assert len(post_data["content"])>0
       print("帖子数据验证通过")

def test_use_agent_order_data():
       """使用Agent生成的订单数据测试接口"""
       print(f"使用Agent生成的订单数据:{order_data}")
       assert order_data["amount"]>0
       assert order_data["status"]  in ["已完成","待支付","已取消"]
       print("订单数据验证通过")
