from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 第二个参数是套路
user_routes = Blueprint(
    'user', 
    __name__, 
    template_folder = 'templates',
    url_prefix='/user'
    )


@user_routes.route('/')
def index():
    return render_template('user_index.html')