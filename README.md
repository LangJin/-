# FlaskWebApp
写一个个人博客
## 导入的包
flask  
flask-bootstrap  
flask-moment  
flask-wtf  
flask-script  
flask-sqlalchemy  
# 连接数据库报错解决
>(1146, "Table 'performance_schema.session_variables' doesn't exist") [SQL: "SHOW VARIABLES LIKE 'sql_mode'"]

mysql> set @@global.show_compatibility_56=ON;
