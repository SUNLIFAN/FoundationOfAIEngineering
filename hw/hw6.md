## hw6

## 1. linear decision boundary : data overview

![image-20220403194944536](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403194944536.png)

## 2.  C's influence on result

C = 1

![image-20220403195149546](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403195149546.png)

这是 C = 1 时的决策边界，可以看出效果还算比较好

C = 10

![image-20220403195259322](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403195259322.png)

C = 10 时决策边界开始有点倾向平缓了，有过拟合的趋势

C = 1000

![image-20220403195438534](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403195438534.png)

C = 1000， 这时已经出现比较严重的过拟合了

## 3. non linear decision boundary : data overview

![image-20220403195726436](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403195726436.png)



## 4. about parameters

![image-20220403201157018](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403201157018.png)

## 5. decision boundary

![image-20220403201242201](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403201242201.png)

## 6. grid search

![image-20220403201354825](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403201354825.png)

![image-20220403201417250](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403201417250.png)

## 7. spam email : data overview

![image-20220403201628488](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403201628488.png)

## 8. train and test

![image-20220403201803413](C:\Users\steven\AppData\Roaming\Typora\typora-user-images\image-20220403201803413.png)

通过调整 C 和 gamma 使测试集上的准确率提高到了 99.1 % 