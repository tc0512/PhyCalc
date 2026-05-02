# PhyCalc
python编写的简单物理计算器

## 下载
### Windows
```cmd
#依赖，视情况下载
pip install kivy
winget install Git.Git
git clone https://github.com/tc0512/PhyCalc.git
#运行
python PhyCalc/PhyCalc.py
```
### Linux
```bash
pip install kivy
apt install git
git clone https://github.com/tc0512/PhyCalc.git
echo "alias PhyCalc='./PhyCalc/PhyCalc.py'" >> .bashrc
source ~/.bashrc
#运行
PhyCalc
```
### MacOs
```zsh
pip install kivy
brew install git
git clone https://github.com/tc0512/PhyCalc.git
echo "alias PhyCalc='python PhyCalc/PhyCalc.py'" >> .zshrc
source ~/.zshrc
PhyCalc
```
### Android(Termux)
```bash
pkg install x11-repo
pkg install opengl sdl2
pip install kivy
pkg install git
git clone https://github.com/tc0512/PhyCalc.git
echo "alias PhyCalc='./PhyCalc/PhyCalc.py'" >> .bashrc
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
