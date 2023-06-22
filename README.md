# FIA & NAA on Tensorflow2.x

本代码仓库用于作为网络与信息安全实验的附件。代码参考于下方两篇文章的代码：

**[Feature Importance-aware Transferable Adversarial Attacks](https://arxiv.org/pdf/2107.14185.pdf) (ICCV 2021)**

**[Improving Adversarial Transferability via Neuron Attribution-Based Attacks](https://arxiv.org/pdf/2204.00008.pdf)  (CVPR 2022)**

## 环境依赖

- Python 3.6.8
- Keras 2.6.0
- Tensorflow 2.6.2
- Numpy 1.19.5
- Pillow 8.4.0
- Scipy 1.2.1
- tf-slim 1.1.0

## 实验

由于模型过大，不便上传，运行代码前，请从 https://github.com/tensorflow/models/tree/master/research/slim 和 https://github.com/tensorflow/models/tree/archive/research/adv_imagenet_models) 中下载预训练模型。 然后将下载好的 checkpoint 文件放到 `./models_tf`。代码中所使用的预训练模型在 `./models_tf/url.txt` 中有说明。

#### 介绍


- `NAA.py` : NAA 生成对抗样本。

- `attacks.py` : 可使用包括 NAA 在内的各攻击算法生成对抗样本。

- `verify.py` : 评估各攻击算法的可迁移性。

#### 攻击层设置

- inception_v3: InceptionV3/InceptionV3/Mixed_5b/concat

- inception_v4: InceptionV4/InceptionV4/Mixed_5e/concat

- inception_resnet_v2: InceptionResnetV2/InceptionResnetV2/Conv2d_4a_3x3/Relu

- resnet_v2_152: resnet_v2_152/block2/unit_8/bottleneck_v2/add
  

#### 数据集

原文作者使用的数据集在 `./dataset/images/`，我构建的数据集在 `./dataset/images_ILSVRC2012/`。

若想自行构建新的数据集，可运行 `./dataset/tackle_imagenet.py` ，运行前请先下载 ILSVRC2012验证集，根据 https://github.com/pytorch/examples/tree/main/imagenet 解压数据集，并修改代码中的各路径。

注意，本实验所用代码中并未设置数据集大小的参数传递api端口，如有需要，请自行修改代码，并替换 `./labels.txt`。

#### 使用示例

##### 生成对抗样本:

- NAA

```
python NAA.py --model_name inception_v3 --attack_method NAA --layer_name InceptionV3/InceptionV3/Mixed_5b/concat --ens 30 --input_dir ./dataset/images_ILSVRC2012/ --output_dir ./adv/NAA/
```

- NAA-PD

```
python NAA.py --model_name inception_v3 --attack_method NAAPIDI --layer_name InceptionV3/InceptionV3/Mixed_5b/concat --ens 30 --amplification_factor 2.5 --gamma 0.5 --Pkern_size 3 --prob 0.7 --output_dir ./adv/NAAPIDI/
```

- PIM:

```
python NAA.py --model_name inception_v3 --attack_method PIM --amplification_factor 2.5 --gamma 0.5 --Pkern_size 3 --output_dir ./adv/PIM/
```

- NRDM

```
python attacks.py --model_name inception_v3 --attack_method NRDM --layer_name InceptionV3/InceptionV3/Mixed_5b/concat --output_dir ./adv/NRDM/
```

参数设置详见实验报告。

##### 评估攻击成功率:

```
python verify.py --ori_path ./dataset/images_ILSVRC2012/ --adv_path ./adv/NAA/ 
```

#### 实验结果

实验结果存储于 `./log.csv`。其中有本实验的实验结果记录。
