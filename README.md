# PhyCalc
python编写的简单物理计算器

## 下载
### Windows
```powershell
cd ~
#依赖，视情况下载
pip install kivy
curl -O https://github.com/tc0512/PhyCalc/archive/refs/tags/v0.1.0.zip #约14.83MB
Expand-Archive -Path v0.1.0.zip -DestinationPath v0.1.0
Add-Content $PROFILE "Set-Alias PhyCalc python $HOME\PhyCalc\PhyCalc.py"
. $PROFILE
#运行
PhyCalc
```
### Linux
```bash
cd ~
pip install kivy
curl -O https://github.com/tc0512/PhyCalc/archive/refs/tags/v0.1.0.zip
unzip v0.1.0.zip
echo "alias PhyCalc='python $HOME/PhyCalc-0.1.0/PhyCalc.py'" >> .bashrc
source ~/.bashrc
#运行
PhyCalc
```
### MacOs
```zsh
cd ~
pip install kivy
brew install git
curl -O https://github.com/tc0512/PhyCalc/archive/refs/tags/v0.1.0.zip
unzip v0.1.0.zip
echo "alias PhyCalc='python $HOME/PhyCalc-0.1.0/PhyCalc.py'" >> .zshrc
source ~/.zshrc
PhyCalc
```
### Android(Termux)
```bash
cd ~
pkg install x11-repo
pkg install libpng libjpeg-turbo libfreetype libglvnd sdl2 sdl2-image sdl2-mixer sdl2-ttf
#禁用一些会出乱子的属性
export USE_SDL2=1
export USE_GLEW=1
pip install cython
pip install kivy
pkg install git
curl -O https://github.com/tc0512/PhyCalc/archive/refs/tags/v0.1.0.zip
unzip v0.1.0.zip
echo "alias PhyCalc='python $HOME/PhyCalc-0.1.0/PhyCalc.py'" >> .bashrc
source ~/.bashrc
PhyCalc
```

## 核心功能
### 物理计算
- 支持简单数学表达式
- 支持变量
### 单位换算
#### 长度单位
- 米m 千米km 毫米mm
- 厘米cm 英尺ft 英寸inch
- 英里mile 码yd
#### 质量单位
- 千克kg 克g 毫克mg
- 磅pound 盎司oz 吨t
- 斤(500g)
#### 时间单位
- 小时h 分钟min 秒s
- 天day 周week

## 使用方法
### `物理计算`使用方法
1. 点击`物理计算`
2. 输入表达式
3. 点击`计算`
4. 得到结果
### `单位换算`使用方法
1. 点击`单位换算`
2. 选择单位类型
3. 选择起点单位并输入数值
4. 选择转换到的单位
5. 点击`转换`
6. 得到结果

## 注意事项
** `物理计算`中，变量名只能包含大小写字母、下划线、数字和中文，不能以数字开头**
