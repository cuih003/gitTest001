#coding:utf-8

import unittest
import requests
import json
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.url = 'http://47.92.88.246:8087/x_springboot/sys/login'

    # 正常登录
    def test_login001(self):
        data={"username": "test","password": "test"}
        # json=:是json格式转换，直接转换为json格式，所以不用headers
        # data=:是字典格式，需要转换json.dumps(data),需要用headers
        r=requests.post(url=self.url,json=data)
        self.assertEqual(r.json()['msg'],'success',msg='正常登陆,登陆成功')
        print(r.text)
    # 用户名为空，登陆失败
    def test_login002(self):
        data={"username": "","password": "test"}
        headers={'content-type':'application/json'}
        r=requests.post(url=self.url,data=json.dumps(data),headers=headers)
        self.assertEqual(r.json()['msg'],'账号或密码不正确',msg='用户名为空，登陆失败')
        print(r.text)
    # 用户名为空格，登陆失败
    def test_login003(self):
        data={"username": " ","password": "test"}
        r=requests.post(url=self.url,json=data)
        self.assertEqual(r.json()['msg'],'账号或密码不正确',msg='用户名为空格，登陆失败')
        print(r.text)
    # 密码错误，登陆失败
    def test_login004(self):
        data={"username": "test","password": "test1111"}
        r=requests.post(url=self.url,json=data)
        self.assertEqual(r.json()['msg'],'账号或密码不正确',msg='密码错误，登陆失败')
        print(r.text)
    # 密码为空，登陆失败
    def test_login005(self):
        data = {"username": "test", "password": ""}
        r = requests.post(url=self.url, json=data)
        self.assertEqual(r.json()['msg'], '账号或密码不正确', msg='密码错误，登陆失败')
        print(r.text)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()