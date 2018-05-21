
Ubuntu16.04 Liunx下同时安装Anaconda2与Anaconda3
https://www.cnblogs.com/zle1992/p/6720425.html
#这里是基于conda3安装conda2环境
bash Anaconda2-4.3.1-Linux-x86_64.sh 
bash Anaconda3-4.3.0-Linux-x86_64.sh -b -p $HOME/anaconda2/envs/py3
rm -f $HOME/anaconda3/envs/py2/bin/conda*
rm -f $HOME/anaconda3/envs/py2/conda-meta/conda-*
rm -f $HOME/anaconda3/envs/py2/bin/activate
rm -f $HOME/anaconda3/envs/py2/bin/deactivate
cd $HOME/anaconda3/envs/py2/bin
ln -s ../../../bin/conda .
ln -s ../../../bin/activate .
ln -s ../../../bin/deactivate .

conda info --envs   //查看conda安装环境
vim ~/.bashrc
#文件末尾输入
export PATH="/home/zle/anaconda2/bin:$PATH"

#切换python环境到python2
source activate py2
source deactivate py2

jupyter notebook --ip=0.0.0.0 #ip=10.103.240.172 是远程服务器地址

cp -r  old_file_name/  new_file_name  #递归复制文件


#定制登录
vim ~/.bashrc  （shift+g切换到文件末）
安装sshpass: sudo apt-get install sshpass
export=10.103.240.172（制定替换的文件）
export zym40='sshpass -p zy931228 ssh -X zy@10.103.240.172'
export  sscp='sshpass -p zy931228 scp -r zy@10.103.240.172:/home/zy'


