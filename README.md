# FlaskWebApp
练习flask的项目  
2018-01-12 新增虚拟环境  
用python自带的venv创建虚拟环境  
```python -m venv virtualenv```  
创建虚拟环境时带入实际环境中的第三方包  
```python -m venv virtualenv --system-site-packages```  

激活虚拟环境的方式  
```F:\MyPython\FlaskWebApp\virtualenv\Scripts\activate```   
或者  
执行Scripts下的activate.bat  

退出虚拟环境
```deactivate```  

把已安装的第三方包写入xx.txt  
```pip freeze > re.txt```   
安装txt里的第三方包  
```pip install -r re.txt```  

>视图认证，没有认证就反馈登陆