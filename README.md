# Wheel_Legged_Gym

## 安装配置

### 系统要求

- **操作系统**：推荐使用 Ubuntu 20.04 或更高版本  
- **显卡**：Nvidia 显卡  
- **驱动版本**：建议使用 525 或更高版本  

### 创建虚拟环境

#### 1. 下载并安装 MiniConda
   
MiniConda 是 Conda 的轻量级发行版，适用于创建和管理虚拟环境。使用以下命令下载并安装：

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

安装完成后，初始化 Conda：

```bash
~/miniconda3/bin/conda init --all
source ~/.bashrc
```

#### 2. 创建并激活虚拟环境

使用以下命令创建并激活虚拟环境：

```bash
conda create -n wheel-legged python=3.8
conda activate wheel-legged
```

### 安装依赖

#### 1. 安装 PyTorch
   
PyTorch 是一个神经网络计算框架，用于模型训练和推理。使用以下命令安装：

```bash
conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 pytorch-cuda=12.1 -c pytorch -c nvidia
```

#### 2. 安装 Isaac Gym

从 Nvidia 官网下载 [Isaac Gym](https://developer.nvidia.com/isaac-gym)。

解压后进入 `isaacgym/python` 文件夹，执行以下命令安装：

```bash
cd isaacgym/python
pip install -e .
```

运行以下命令，若弹出窗口并显示 1080 个球下落，则安装成功：

```bash
cd examples
python 1080_balls_of_solitude.py
```

#### 3. 安装 Wheel_Legged_Gym

通过 Git 克隆仓库：

```bash
git clone https://github.com/kai698/Wheel_Legged_Gym.git
```

进入目录并安装：

```bash
cd Wheel_Legged_Gym
pip install -e .
```

---

## 使用指南

### 训练

运行以下命令进行训练：

```bash
python wheel_legged_gym/scripts/train.py --task=yuelu
```

使用 TensorBoard 监控训练过程：

```bash
tensorboard --logdir=./
```

#### 参数说明
- `--task`: 必选参数，默认为 yuelu
- `--headless`: 默认启动图形界面，设为 true 时不渲染图形界面（效率更高）
- `--resume`: 从日志中选择 checkpoint 继续训练
- `--experiment_name`: 运行/加载的 experiment 名称
- `--run_name`: 运行/加载的 run 名称
- `--load_run`: 加载运行的名称，默认加载最后一次运行
- `--checkpoint`: checkpoint 编号，默认加载最新一次文件
- `--num_envs`: 并行训练的环境个数
- `--seed`: 随机种子
- `--max_iterations`: 训练的最大迭代次数
- `--sim_device`: 仿真计算设备，指定 CPU 为 `--sim_device=cpu`
- `--rl_device`: 强化学习计算设备，指定 CPU 为 `--rl_device=cpu`

**默认保存训练结果**：`logs/<experiment_name>/<date_time>_<run_name>/model_<iteration>.pt`

### play

如果想要在 Gym 中查看训练效果，可以运行以下命令：

```bash
python wheel_legged_gym/scripts/play.py --task=yuelu
```

#### 说明

- Play 启动参数与 Train 相同。
- 默认加载实验文件夹上次运行的最后一个模型。
- 可通过 `load_run` 和 `checkpoint` 指定其他模型。
- Play 会导出 Actor 网络，保存于 `logs/{experiment_name}/exported/policies/policy_1.pt`。

---

## 故障排除

出现如下错误：`ImportError: libpython3.8.so.1.0: cannot open shared object file: No such file or directory`

1. 查找`libpython3.8.so.1.0`
   
    ```bash
    find / -name "*ibpython3.8.so.1.0*" 2>/dev/null
    ```

2. 添加动态链接库

    例：上面命令查找结果为：`/home/kai/miniconda3/envs/wheel-legged/lib/libpython3.8.so.1.0`

    则运行以下命令：

    ```bash
    echo 'export LD_LIBRARY_PATH=/home/kai/miniconda3/envs/wheel-legged/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
    source ~/.bashrc
    ```

---

## 开源参考

- [legged_gym](https://github.com/leggedrobotics/legged_gym)：腿式机器人强化学习框架。
- [rsl_rl](https://github.com/leggedrobotics/rsl_rl)：强化学习算法实现。
- [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym)：宇树机器人强化学习。
- [Wheel-Legged-Gym](https://github.com/clearlab-sustech/Wheel-Legged-Gym)：轮足机器人强化学习。