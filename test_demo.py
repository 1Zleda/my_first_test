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
