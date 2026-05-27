from coze import TokenAuth, Coze

# 替换成你的信息
SPACE_ID = "7644179050802069510"  # 你的空间ID
BOT_ID = "7644180500185513993"              # 你的Bot ID
TOKEN = "pat_64HooqwbPg07HncXheMUQGb90v0xGXQhKalMSR96IBwQsi3uy42Jw3dMGKgkz3BM"      # 你的token

# 创建客户端
auth = TokenAuth(token=TOKEN)
coze = Coze(auth=auth)

# 调用 Agent
response = coze.chat(
    space_id=SPACE_ID,
    bot_id=BOT_ID,
    user_id="test_user",
    additional_messages=[
        {
            "role": "user",
            "content": "用户",
            "content_type": "text"
        }
    ]
)

print(response)