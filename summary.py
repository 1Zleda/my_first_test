"""
我的pytest学习总结
包含：基础测试、参数化、fixture
"""

import requests
import pytest

# ======== 1.基础测试 ========
def test_get_post():
       url="https://jsonplaceholder.typicode.com/posts/1"
       response=requests.get(url)
       assert response.status_code==200
       print("基础测试通过")

# ======== 2.参数化 ========
@pytest.mark.parametrize("post_id",[1,2,3,50,101])
def test_multiple_posts(post_id):
       url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
       response=requests.get(url)
       if post_id<=100:
           assert response.status_code==200
       else:
           assert response.status_code==404
       print(f"参数化测试：帖子{post_id}测试完成")

# ======== 3.fixture ========
@pytest.fixture
def prepare_data():
      print("\n测试前：准备数据")
      data={"name":"测试用户","age":18}
      yield data
      print("\n测试后：清理数据")

def test_with_fixture(prepare_data):
       assert prepare_data["name"]=="测试用户"
       assert prepare_data["age"]==18
       print("fixture测试通过")