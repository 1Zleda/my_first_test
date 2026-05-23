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
      # 第一步：创建用户，获取用户id
      create_url="https://httpbin.org/post"
      user_data={
            "name":"张三",
            "job":"测试工程师"
      }
      create_resp=requests.post(create_url,json=user_data)
      assert create_resp.status_code==200
      sent_data=create_resp.json()["json"]
      print(f"发送的数据:{sent_data}")

      # 第二步：查询用户信息
      get_url=f"https://httpbin.org/get"
      get_resp=requests.get(get_url,params={"user_id":123})
      assert get_resp.status_code==200
      print(f"查询参数：{get_resp.json()['args']}")
