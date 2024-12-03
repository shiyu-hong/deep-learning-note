# -*- coding:utf-8 -*-
import torch
import torch_directml


class ImageTrainer:
    def __init__(self, data_dir: str, image_size: tuple[int, int] = (224, 224)):
        self.data_dir = data_dir
        self.image_size = image_size

    def _initialize_variables(self):
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # NVIDIA 显卡
        self.device = torch_directml.device()  # AMD 显卡 (DX12)
