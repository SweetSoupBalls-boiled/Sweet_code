---
typora-root-url: ./
---

# 1.常用命令

## a) rm

##### 功能: 删除文件或文件夹

rm 普通文件

rm 普通文件 -i        有提示,按y 确定删除

rm 普通文件 -f        强制删除,没有提示

rm 文件夹 -r            删除文件夹需要-r

## b) cp

cp 1.txt xxx.txt        给1.txt文件复制一份名字为xxx.txt

cp  test/  yyy  -r       给test文件夹复制一份名字为yyy

### c) mv

mv 1.txt ../               把1.txt移动到上一级目录

mv  test  ../yyy         把test文件移动到上一级目录,同时改名为yyy

mv  1.txt   mike.txt   同级目录, mv作用是改名,把1.txt改名为mike.txt

### d)查看文件内容

gedit, subl, pycharm, vi

cat  文件         一次性查看文件内容

cat   /user/include/stdio.h		可以翻页显示

### e) find

find	. /	-name	"mike.txt"	在当前路径下,  找名字为"mike.txt"的文件	

find . /	-name	"*.txt"		在当前路径下, 找后缀为.txt的文件

find  /bin   -size    + 100k			在/bin,找文件大小大于100k的文件

find  /bin   -size    +100k  -size  -200k  在/bin,找文件大小大于100k,小于200k的文件

find . /   -type f		在当前路径下,查找文件类型为普通文件的文件

find . /   -type d             在当前路径下,查找文件类型为文件夹的目录文件

### f) grep

grep  "m"   mike.txt    -n    只要带"m"关键字的内容都要, -n显示行号

-i  :  忽略大小写

-v :  取反

grep  "^m"  mike.txt   -n    只要以m开头的内容

grep  "ke$"  mike.txt   -n    只要以ke结尾的内容

### g)  管道

grep经常配合管道使用

ls  /bin  |   grep  mv   

ls   /bin  原来显示到屏幕的内容,塞进管道的一端 ,管道的另外一端取内容,过滤方式取只取带mv关键字的内容

### h) 压缩包管理

#### 1)  .tar.gz

压缩 : tar  -cvzf    xxx.tar.gz   需要压缩的文件或文件夹

  	   -可有可无,建议写上

​	  c :  create   创建压缩包

​	  v :   进度

​	  z :   调用gizp压缩工具进行压缩

​	  f :   file       后面跟的是压缩包文件名,f一定是放在选项的后面,前3个选项只要在f前面,顺序任意

  tar  -cvzf   ../xxx.tar.gz  需要压缩的文件或文件夹

解压:   tar  -xvf  xxx.tar.gz   -C(大写C)  指定路径

​             -可有可无,建议写上

​	    v :  进度

​	    f : file , 后面跟的是压缩包文件名,f一定是放在选项的后面

​	   x :   解压

#### 2)  .tar.bz2

压缩: tar -cvjf  xxx.tar.bz2  需要压缩的文件或文件夹

​             -可有可无,建议写上

​	    c :  create  创建压缩包

​	    v : 进度

​	   j : 调用bzip2压缩工具进行压缩

​	   f: file , 后面跟的是压缩包文件名,f一定是放在选项的后面, 前3个选项只要在f前面,顺序任意

解压 : tar  -xvf  xxx.tar.gz  -C(大写C)  指定路径

​             -可有可无,建议写上

​	   v : 进度

​	   f:  file,  后面跟的是压缩包文件名, f 一定是放在选项的后面

​	   x: 解压

#### 3)  .zip

压缩 :  zip  -r xxx.zip  需要压缩的文件或文件夹

解压 : unzip  xxx.zip  -d  指定路径

### i) 文件权限

   -rw-rw-r-- 1 python python   85 4月  14 09:47 mike.txt
​    

    -   rw- rw- r--
    第一组：文件所有者，谁创建文件，谁就是文件所有者，朋友圈发状态状态设置为私人的， u
    第二组：用户组，QQ群，朋友圈发状态状态可以设置为好友可见                         g
    第三组：其它用户，朋友圈陌生人可见10个状态                                       o
    
    python python
    第一个就文件所有者的名字
    第二个用户组的名字
    
    权限分类：
    r   只读
    w   只写
    x   可执行
    -   无权限
### j) chmod

字母法: 

chmod u+x demo.txt   user增加x权限

chmod g-w demo.txt   group减去w权限

chmod o=w demo.txt   other只有w权限

chmod  u-w,g+w,o+x  demo.txt

chmod  a=rwx demo.txt  所有用户具备rwx权限



数字法:

r        4

w       2

x        1

rwx     7

r-x       5

r--        4

--x        1

chmod 634 demo.txt

​      rw--wxr--

### k) 管理用户

sudo 临时提升到管理员权限,输入的密码是当前登陆用户密码

sudo  -s  简单切换到管理员用户

whoami   查看当前登陆用户

exit 退出当前用户,回到上一用户,如果当前用户是第一个用户,退出终端

### l)在线安装软件

sudo apt-get  update      更新列表

sudo  apt-get  install soft   安装软件

sudo apt-get  remove soft  删除软件

### m) 网络相关

ifconfig     查看网络信息

ping  测试网络是否联通



# vi模式

## 模式

1 命令模式===>> 编辑模式

i  出现插入,输入内容

2 编辑模式===>> 命令模式

Esc  可以输入命令,不可编辑

3 编辑模式===>>末行模式

先切换命令模式,输入  :wq  保存退出

### 最基本操作

1 如何新建文件,如何打开文件

vi xxx.txt

2 编辑文件

按i 切换到编辑模式后再编辑

3 保存退出

: wq

### 切换到文本输入模式

![命令](/命令.png)



### 