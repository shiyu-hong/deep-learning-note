# Miniforge 配置深度学习环境

- Miniforge 下载链接：https://github.com/conda-forge/miniforge/releases
- Conda 换源教程：
  - 清华源：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
- PyPI 换源教程：
  - 清华源：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
- DirectML 教程：
  - 在 Windows 上通过 DirectML 搭建 PyTorch 环境教程：https://learn.microsoft.com/zh-cn/windows/ai/directml/pytorch-windows


## PyTorch

## 搭建 DirectML PyTorch 环境
```bash
# 创建 pytorch 虚拟环境
(base) C:\Windows\System32>conda create --name pytorch python=3.12

# 切换到 pytorch 虚拟环境
(base) C:\Windows\System32>conda activate pytorch

# 使用 pip 安装 torch 相关库
(pytorch) C:\Windows\System32>python -m pip install --upgrade pip
(pytorch) C:\Windows\System32>pip install torch-directml
(pytorch) C:\Windows\System32>pip install ipykernel
(pytorch) C:\Windows\System32>pip install matplotlib

# 删除 pytorch 虚拟环境 (虚拟环境出现异常时，再执行该指令)
(base) C:\Windows\System32>conda remove --name pytorch --all
```