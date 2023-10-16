import pandas as pd
from torch.utils.data import Dataset

class MyDfDataset(Dataset):
    def __init__(self, root, train=True):
        self.dataframe = pd.read_csv(root)
        # 切割
        split_point = int(len(self.dataframe) * 0.6)
        if train:
            self.dataframe = self.dataframe.iloc[:split_point]
        else:
            self.dataframe = self.dataframe.iloc[split_point:]

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        features = str(self.dataframe.iloc[idx]["受理内容"])
        label = int(self.dataframe.iloc[idx]["情绪等级标注结果"])
        return features, label


if __name__ == "__main__":
    pass