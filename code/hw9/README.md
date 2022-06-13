# README

数据集来自 https://data.ncl.ac.uk/articles/dataset/Handwritten_Chinese_Numbers/10280831/1

大概 10000 张图片，按照 6:2:2 划分训练集，验证集，测试集

超参数选择后用测试集加验证集的数据训练模型，在测试集上的准确率为 92.5%

training_part 里面存的是训练和保存模型的代码。

testing_part 里面存的是加载模型和测试的代码。