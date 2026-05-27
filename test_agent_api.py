import requests

# 1. 请替换以下两个值
API_KEY = "pat_64HooqwbPg07HncXheMUQGb90v0xGXQhKalMSR96IBwQsi3uy42Jw3dMGKgkz3BM"   # 以 pat_ 开头的字符串
BOT_ID = "7644180500185513993"              # 纯数字的字符串

# 2. Coze API 的准确地址（不要加额外的斜杠）
url = "https://api.coze.cn/v1/chat"

# 3. 请求头（格式必须完全一致）
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 4. 请求体（结构必须完全一致）
data = {
    "bot_id": BOT_ID,
    "user_id": "test_user_123",          # 可以随便改，用来区分不同用户
    "additional_messages": [              # 注意是列表，里面包含字典
        {
            "role": "user",               # 角色是 user
            "content": "用户",            # 这里是发给 Agent 的内容
            "content_type": "text"        # 内容类型是文本
        }
    ],
    "auto_save_history": True             # 建议加上这一行，保存对话历史
}

# 5. 发送请求
response = requests.post(url, headers=headers, json=data)

# 6. 打印结果（打印文本格式更容易看错误信息）
print("状态码:", response.status_code)
print("返回内容:", response.text)

# 7. 如果状态码是 200，再尝试解析 JSON
if response.status_code == 200:
    result = response.json()
    # Coze 返回的内容在 choices[0].message.content 里
    agent_reply = result.get("choices", [{}])[0].get("message", {}).get("content", "")
    print("Agent 回答:", agent_reply)