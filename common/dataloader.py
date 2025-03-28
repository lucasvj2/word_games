import os
from PIL import Image, ImageOps
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from common.model import LetterCNN

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Pad(padding=3),
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

dataset = datasets.ImageFolder('data', transform=transform)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

model = LetterCNN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

print("🚀 Training...")
for epoch in range(10):
    total_loss = 0
    for inputs, labels in loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}/10 | Loss: {total_loss:.4f}")


def predict(img_path, model):
    model.eval()
    img = Image.open(img_path).convert('L')
    img = ImageOps.pad(img, (64, 64), color=255)
    tensor = transforms.ToTensor()(img).unsqueeze(0)
    with torch.no_grad():
        output = model(tensor)
        pred = torch.argmax(output, 1).item()
    return dataset.classes[pred]

torch.save(model.state_dict(), "model.pth")
