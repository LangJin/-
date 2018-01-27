# -*- coding:utf-8 -*-
'''
时间：2018-01-28
作者：浪晋
说明：locust测试
'''
from locust import HttpLocust, TaskSet, task


class TestHttp(TaskSet):

    def test(self):
        data = "hello locust!!!"
        headers = {
            'content-type': "text/plain",
            'cache-control': "no-cache",
            'postman-token': "cd23245e-1698-be3e-d184-8f3034622811"
            }
        r = self.client.post('/post', headers=headers, data=data)
        res = r.json()
        return res['data']

    @task
    def post(self):
        data = "hello locust!!!"
        headers = {
            'content-type': "text/plain",
            'cache-control': "no-cache",
            'postman-token': "cd23245e-1698-be3e-d184-8f3034622811"
            }
        self.client.post('/post', headers=headers, data=data)

    @task
    def get(self):
        self.client.get('/headers')


class WebsiteUser(HttpLocust):
    task_set = TestHttp
    min_wait = 500
    max_wait = 500
