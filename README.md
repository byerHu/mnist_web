# mnist_web

- 使用tensorflow框架，构建回归和CNN两种模型，对手写数字体进行识别
- 数据集为mnist
- 整合web框架Flask

前端本来想使用echarts做图表展示，但是在main.js中,ajax成功的函数里使用var myChart = echarts.init($('#regression'));报错，没有解决只好以table展示结果。
