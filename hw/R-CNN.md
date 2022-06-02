# R-CNN 

## 应用场景 ： 目标检测

![](https://img2022.cnblogs.com/blog/2302323/202205/2302323-20220522220534633-713459143.png)

- 输入 ： 图片
- 输出 ： 物体类标签，boundingbox (通过指出中心点坐标和boundingbox 的尺寸)



## 一种解决方法

- 物体类标签 ： 分类
- bounding box ： 回归
- 使用 CNN 来提取特征

## 困难 ： 一张图片中多个目标的检测

- 解决： 将图片分割成多个区域

- 选取区域的算法

  - Exhaustive searching : 滑动窗口，计算开销大，时间长  

  - Selective searching : 自底向上的贪心算法，减少选出冗余的区域



## R-CNN 的问题

- selective searching 仍然会选出 2000 个区域，计算开销仍然较大
- 计算时间较长，无法用于实时预测 
- 固定的搜索算法(selective searching): 可能选出不太良好的区域



## 对 R-CNN 的改进 ：Fast R-CNN

- 直接将图片输入卷积层, 再在feature map上找候选区域对应的区域，而不是把所有候选区域输入卷积层，减少了重复的卷积运算



![](https://img2022.cnblogs.com/blog/2302323/202205/2302323-20220522221719818-894270779.png)



![](https://img2022.cnblogs.com/blog/2302323/202205/2302323-20220522221743714-147712107.png)

## Fast R-CNN 的问题

仍然需要使用 selective searching 进行候选区域的选择，成为了整个过程的瓶颈

## 进一步改进 : Faster R-CNN

- 不使用 selective searching 来选择候选区域，整个过程都交给神经网络来完成
- 可以支持实时预测



![](https://img2022.cnblogs.com/blog/2302323/202205/2302323-20220522222056229-1311987282.png)

改进后的性能对比

![](https://img2022.cnblogs.com/blog/2302323/202205/2302323-20220522222039504-262405540.png)

## 参考

[1] J.R.R. Uijlings et al, Selective Search for Object Recognition

[2] Shaoqing ren et al, Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks