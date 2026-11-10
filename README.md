# Django-Web

在线教育平台后端，基于 Django 4.2、Django REST framework 和 MySQL。提供课程、讲师、免费课程、学习计划、用户、问答和订单等 REST API；仓库不包含前端项目。

## 运行环境

- Python 3.10～3.12（项目使用 Django 4.2.3）
- MySQL 8.x
- Windows PowerShell（以下命令以此为例）

## 本地启动

1. 在仓库根目录创建虚拟环境并安装依赖：

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

   如果使用其他受支持的 Python 版本，请相应调整 `py -3.12`。

2. 登录 MySQL，创建数据库：

   ```powershell
   mysql -u root -p
   ```

   ```sql
   CREATE DATABASE edu_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   EXIT;
   ```

3. 核对 `edu_project/edu_project/settings.py` 中的 `DATABASES` 配置。当前连接到 `127.0.0.1:3306` 的 `edu_db`，数据库用户和密码写在配置文件中；本地 MySQL 的账号、密码或端口不同时，需要按实际环境调整。

4. 创建表并启动服务：

   ```powershell
   cd edu_project
   python manage.py migrate
   python manage.py check
   python manage.py runserver
   ```

   API 基础地址为 `http://127.0.0.1:8000/api/`，Django 管理后台地址为 `http://127.0.0.1:8000/admin/`。

## 示例数据

`data/` 中的 SQL 文件只有示例数据插入语句，不负责建表。执行 `migrate` 后，如需看到课程等示例内容，可在**仓库根目录**运行 `mysql -u root -p edu_db`，再按下面的顺序在 MySQL 客户端中执行：

```sql
SOURCE data/1course.sql;
SOURCE data/2stage.sql;
SOURCE data/3chapter.sql;
SOURCE data/4section.sql;
SOURCE data/5teacher.sql;
SOURCE data/6free.sql;
SOURCE data/7rotationchart.sql;
SOURCE data/8featureService.sql;
SOURCE data/9plan.sql;
SOURCE data/10classtype.sql;
SOURCE data/11updateCourse.sql;
```

示例数据只需导入一次，重复执行可能产生重复记录。`data/12_mysection.sql` 引用了用户 ID 1、2；只有创建了相应用户并确认 ID 后才导入。

## 常用接口

以下路径均以 `/api/` 为前缀：

| 功能 | 路径 | 方法 |
| --- | --- | --- |
| 注册、登录 | `register/`、`login/` | POST |
| 课程、阶段、章节、课时 | `courses/`、`stages/`、`chapters/`、`sections/` | GET |
| 讲师、免费课程 | `teachers/`、`free_courses/` | GET |
| 首页轮播、特色服务 | `rotation_charts/`、`feature_services/` | GET |
| 学习计划、班型 | `plans/`、`class_types/` | GET |
| 课程更新 | `update_courses/` | GET |
| 个人课程、订单 | `user_courses_list/`、`user_orders/` | GET |
| 问答 | `get_questions/`、`user_questions/`、`user_answers/` | 见各接口实现 |
| 下单、支付回调 | `user_pay_courses/`、`pay_callback/` | POST |

例如，导入示例数据后可在另一个 PowerShell 窗口查看课程列表：

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/courses/
```

`courses/` 支持 `page`、`size` 分页参数；阶段、章节和课时列表分别可按 `course`、`stage`、`chapter` 过滤。登录成功后，`/api/user/<id>/` 的请求需在 `Authorization` 请求头中直接传入返回的 JWT token（不加 `Bearer` 前缀）。

## 项目结构

```text
data/                         示例数据 SQL
edu_project/manage.py         Django 命令入口
edu_project/edu_project/      全局配置和路由
edu_project/*_app/            各业务模块
edu_project/key/              支付宝沙箱密钥文件
requirements.txt              Python 依赖
```

## 配置提示

当前配置包含固定的数据库凭据、Django/JWT 密钥和支付宝沙箱配置，仅适合本地学习与开发。支付通知地址固定为 `http://127.0.0.1:8000/api/pay_callback/`，外部支付宝服务无法访问本机回环地址，因此本地启动并不代表支付回调可用。对外部署前需重新设计密钥和凭据管理、关闭不安全配置，并使用可访问的回调地址。
