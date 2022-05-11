# hw8 - Neural Network

## 1. load data

![image-20220430204637818](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430204637818.png)

![image-20220430204704707](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430204704707.png)

## 2. training

![image-20220430204806853](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430204806853.png)

## 3. predict

![image-20220430204835665](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430204835665.png)

准确率

![image-20220430204934368](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430204934368.png)

## 4. tuning

### 4.1 调整学习率

![image-20220430205048186](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430205048186.png)

把学习率从 1 调到 0.1, 步长更小会收敛到一个更准确的位置。

### 4.2 调整 hidden layer 的神经元个数

![image-20220430205238862](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430205238862.png)

增加了参数个数会提高拟合效果。

### 4.3 提高 max_iter

![image-20220430205858559](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220430205858559.png)

增加训练的最大轮数有机会收敛到一个更准确的位置。