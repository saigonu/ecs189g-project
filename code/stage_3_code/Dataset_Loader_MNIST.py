import torch.utils.data

from code.base_class.dataset import dataset
import pickle
import torchvision.transforms as transforms
import numpy as np

class Dataset_Loader_MNIST(dataset):
    data = None
    dataset_source_folder_path = None
    dataset_source_file_name = None

    def __init__(self, dName=None, dDescription=None):
        super().__init__(dName, dDescription)

    def load(self):
        print('loading data...')
        f = open(self.dataset_source_folder_path + self.dataset_source_file_name, 'rb')
        data = pickle.load(f)
        f.close()
        train_data = []
        # print(data['train'][0]['image'])
        transform_norm = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
        for sample in data['train']:
            # image_path = np.array(sample['image'])
            # image_path = image_path.astype(np.float32)
            # normal_image = transform_norm(image_path)
            sample['image'] = transform_norm(sample['image']).to(torch.float32)
        for sample in data['test']:
            # image_path = np.array(sample['image'])
            # image_path = image_path.astype(np.float32)
            # normal_image = transform_norm(image_path)
            sample['image'] = transform_norm(sample['image']).to(torch.float32)

        # print(data['train'][0])
        # print(data['train'][0]['image'].shape)
        train_data = torch.utils.data.DataLoader(data['train'], shuffle=True, batch_size=32)
        test_data = torch.utils.data.DataLoader(data['test'], shuffle=False, batch_size=32)
        return {'train_data': train_data, 'test_data': test_data}