import requests

def test_get_post():
      url="http://jsonplaceholder.typicode.com/posts/2"
      response=requests.get(url)
      assert response.status_code==200
      print("测试通过")

def test_get_post_not_exists():
      url="http://jsonplaceholder.typicode.com/posts/999999"
      response=requests.get(url)
      assert response.status_code==404
      print("测试通过")

def test_get_post_list():
      url="http://jsonplaceholder.typicode.com/posts"
      response=requests.get(url)
      assert response.status_code==200
      assert isinstance(response.json(),list)
      print("返回的数据条数：",len(response.json()))
