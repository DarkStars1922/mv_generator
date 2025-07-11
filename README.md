# 运行网页指南

## 配置`Django`：

- **创建虚拟环境（建议）**

  在项目主目录下运行`PowerShell`或`cmd`进入项目目录，执行以下指令（需安装`python`）：

  ```
  python -m venv venv
  ```

- **激活虚拟环境**

  ```
  .\venv\Scripts\Activate
  ```

- **在虚拟环境中（如果使用了虚拟环境）安装`Django`**

  ```
  pip install django
  ```

  验证是否安装成功：

  ```
  django-admin --version
  ```

  安装`Django`框架：

  ```
  pip install djangorestframework
  ```

- **在虚拟环境中创建`Django`项目和`app`**

  ```
  # 创建项目
  django-admin startproject graduation_mv .
  
  # 创建一个 app
  python manage.py startapp mvapp
  ```

## 启动服务器：

在虚拟环境中执行指令：

```
python manage.py runserver
```

出现

```
Starting development server at http://127.0.0.1:8000/
```

说明启动成功，访问该地址即可成功运行网页