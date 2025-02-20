from src.interface import run_interface
import torch

if __name__ == '__main__':
    model_path = 'D:\\Users\\DELL\\Desktop\\.2\\trained-models\\model_final.pth'
    model = torch.load(model_path, map_location=torch.device('cpu')) # Update with the correct path
    run_interface(model_path, threshold=0.5)
