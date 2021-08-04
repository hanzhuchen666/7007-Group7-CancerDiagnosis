因为咱们这个网站买服务器,没有上线,所以需要用自己的电脑当服务器.所以电脑里需要安装django框架 我的版本是2.2.12. 和 mysql数据库 并且创建一个叫user_interface的数据库 要用utf-8格式

解压后进入到文件夹里看到manage.py文件后用 python3 manage.py runserver启动服务器

之后再用 python3 manage.py makemigrations 和 python3 manage.py migrate 来生成数据库里面的数据表


启动服务器正常后就可以打开浏览器(建议用chrome),输入网址 http://127.0.0.1:8000/user/login就可以到网页里去了


