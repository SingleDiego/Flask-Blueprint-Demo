from flask import Flask

# 引入各个路由的蓝图对象
from todo_app.views import todo_routes
from user_app.views import user_routes


app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'random string'


# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
# 比如：碰到 "/todo" 开头的 URL，就会用 todo_routes 的函数来处理
app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(user_routes, url_prefix='/user')


# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)