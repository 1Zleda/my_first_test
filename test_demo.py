import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    print("✅ 测试通过！")

def test_get_post_not_exists():
    url = "https://jsonplaceholder.typicode.com/posts/999999"
    response = requests.get(url)
    assert response.status_code == 404
    print("✅ 测试通过！")

def test_get_posts_list():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(),list)
    print("✅ 测试通过！")

import pytest

@pytest.mark.parametrize("post_id",[1,2,3,99,999])
def test_multiple_posts(post_id):
      url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
      response=requests.get(url)

      if post_id<=100:
            assert response.status_code==200
      else:
            assert response.status_code==404
      print(f"测试帖子{post_id}完成")

import pytest

@pytest.fixture
def prepare_data():
      print("\n准备测试数据...")
      data={"name":"张三","age":18}
      yield data
      print("\n清理测试数据...")

def test_with_fixture(prepare_data):
     print(f"使用测试数据：{prepare_data}")
     assert prepare_data["name"]=="张三"

def test_create_and_get_user():
    # 第一步：先获取用户列表，拿到第一个用户的 id
    user_list_url = "https://jsonplaceholder.typicode.com/users"
    user_list_resp = requests.get(user_list_url)
    assert user_list_resp.status_code == 200
    users = user_list_resp.json()
    first_user_id = users[0]["id"]
    print(f"第一个用户的ID: {first_user_id}")

    # 第二步：用获取到的用户 id 查询这个用户的帖子
    posts_url = f"https://jsonplaceholder.typicode.com/users/{first_user_id}/posts"
    posts_resp = requests.get(posts_url)
    assert posts_resp.status_code == 200
    posts = posts_resp.json()
    print(f"该用户共有 {len(posts)} 篇帖子")
    print(f"第一篇帖子的标题: {posts[0]['title']}")

def test_get_users_list():
    # 获取所有帖子，返回的是一个列表
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200
    
    posts = response.json()  # 这里直接返回列表
    print(f"共返回 {len(posts)} 条帖子")
    
    # 取第一条帖子的标题
    first_post_title = posts[0]["title"]
    print(f"第一条帖子的标题: {first_post_title}")
    
    # 遍历前3条帖子
    for post in posts[:3]:
        print(f"帖子 {post['id']}: {post['title'][:30]}...")

def test_token_auth():
    # 第一步：模拟登录，获取 token（用 httpbin 模拟返回 token）
    login_url = "https://httpbin.org/post"
    login_data = {
        "email": "test@example.com",
        "password": "123456"
    }
    login_resp = requests.post(login_url, json=login_data)
    assert login_resp.status_code == 200
    
    # httpbin 会原样返回你发送的数据，我们从中构造一个模拟 token
    sent_data = login_resp.json()["json"]
    token = f"mock_token_{sent_data['email']}"
    print(f"模拟获取到的 token: {token}")
    
    # 第二步：用 token 访问需要认证的接口
    user_url = "https://httpbin.org/get"
    headers = {"Authorization": f"Bearer {token}"}
    user_resp = requests.get(user_url, headers=headers)
    assert user_resp.status_code == 200
    print("带 token 的请求成功")
    
    # 打印发送的请求头，确认 Authorization 被正确传递
    print(f"请求头中的 Authorization: {user_resp.json()['headers']['Authorization']}")