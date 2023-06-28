import torch
from torchvision import datasets, transforms

dataset_path = "/mnt/f/valorant_VODs/ocr_dataset"

transform = transforms.ToTensor()

train_data = datasets.ImageFolder(root=dataset_path, transform=transform)
trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
