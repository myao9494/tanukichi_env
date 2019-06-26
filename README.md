# tanukichi_env
開発環境です


### jupyter_extentionsのインストール¶
#### install  
pip install jupyter_contrib_nbextensions  
jupyter contrib nbextension install --user  
jupyter nbextension enable codefolding/main  

pip install nbdime  
nbdime config-git --enable --global  

conda install -c conda-forge nodejs

#### set snippets(jupyter notebook)
copy snippets.json  
%userprofile%\AppData\Roaming\jupyter\nbextensions\snippets\snippets.json

if snippets can not work.
1. delete snippets.json at explorer
2. Reload at jupyter notebook
3. copy snippets.json again
4. Reload at jupyter notebook  


### Windows Binaries for Python Extension Packages
https://www.lfd.uci.edu/~gohlke/pythonlibs/



http://www.takitoshimi.shop/aircraft/aircraft_fea_jp.htm
