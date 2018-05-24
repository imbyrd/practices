## 类UNIX版本

使用方法
=====

1:全局变量定义
------------
```
git config --global user.name "imbyrd"
git config --global user.email "ibyrd@sohu.com"
git config --global color.ui true
```
*2:Create a new repository*
------------
```
git clone git@github.com:imbyrd/practices.git 
cd practices
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```
*3:Existing folder or Git repository*
------------
```
cd existing_folder
git init
git remote add origin git@github.com:imbyrd/practices.git
git add .
git commit
git push -u origin master
```
*4:拉取-提交*
------------
```
git pull origin master    #将数据拉回本地
git push -u origin master    #将数据提交到gitlab
```
*5:其他命令*
```
git add readme.txt    #将文件放入暂存区
git commit -m "hello,world"    #文件提交说明
git diff readme.txt    #比较当前修改和仓库文件对比
git reset --hard HEAD^    #回退一个版本git reset --hard HEAD^^ 几个^表示几个版本
git reflog     #可以查看所有分支的所有操作记录
git reset --hard 2b91b7b    #回退到某个固定修改
git checkout readme.txt    #git checkout -- readme.txt    未提交的可以checkout
git branch    #查看分支
git branch <name>    #创建分支
git checkout <name>    #切换分支
git checkout -b <name>    #创建+切换分支
git merge <name>    #合并某分支到当前分支
git branch -d <name>    #删除分支
```
