Wild数据集中的徽标

#一般备注
该数据集由通过Google抓取的网络图像组成
图片搜索和根据标志注释。它是在
德国卡尔斯鲁厄的Fraunhofer IOSB。
有关数据集相关事宜，请联系Christian Herrmann:
christian.herrmann@iosb.fraunhofer.de。


#结构
每个文件夹包含原始Pascal VOC风格的xml注释文件和一个
url .txt文件，其中包含可以放置图像的url列表
下载。列表中的每一行都包含图像ID和URL
图像文件的。

一个文件夹包含了谷歌图片搜索的所有图片
这个品牌。因为图像可以显示出各种各样的标识之外的
关键词搜索，有很多不同品牌的标志在每个
文件夹，有时甚至在单个图像。
边界框名称表示每个徽标的实际品牌。当
必要时，在图形和文本标识之间进行分离
品牌名称的附加说明(例如:保时捷的商标,
“porsche-text”)。在视觉上，一个品牌的不同标志被分隔开
如果不可能以图形/文本进行区分，则进行枚举(例如:
“adidas1”、“adidas2”)。有一些拼写错误和不一致
使用原始注释文件中的标签和说明符。我们选择不这么做
更改注释组提供的原始文件，而是修复
由create_clean_dataset.py脚本(参见下面的脚本部分)解决问题。

已清理的说明符列表:
-“text”:纯文本标识
-“符号”:图形标识

原始注释中的附加说明符:
- 'partial'，'teilsichtbar':标志被明显遮挡，因此只有
部分可见，此信息仅包含在原始注释中
- 'schrift'，'schriftzug':与'text'相同
-“标志”:与“符号”相同


#脚本
为了简化处理，scripts文件夹包含一个Python脚本
预处理数据集。
Create_clean_dataset.py纠正标签错误并可以创建
不同版本的数据集:

1)。干净的Pascal VOC数据集结构，这是直接可读的
通过很多对象检测器框架。这是在所有情况下创建的:
Python create_clean_dataset.py——in ./data——out ./cleaned-data

2)。裁剪后的徽标分类到单独的品牌文件夹中。这个地址
分类或验证任务。参数:——roi。

3)。来自FlickrLogos32的Logo类可以从1)和2)via中排除
——wofl32。这允许在野外训练徽标和测试
FlickrLogos32如果品牌重叠是不希望的，如开放集
进行分析。


#如何开始
1)。从提供的url下载图像。
2)。执行create_clean_dataset.py脚本。

#数据集使用
如果您在工作中使用此数据集，请注明:

@INPROCEEDINGS {,
作者= {T{\"u}zk{\"o}， Andras and Herrmann, Christian and Manger, Daniel
J{\"u}rgen Beyerer}，
title = {{O}pen {S}et {L}ogo {D}检测{R}检索}
第十三届国际联合会议论文集
计算机视觉、成像与计算机图形学理论与应用:
VISAPP},
年份= {2018}}


#版权、许可和法律信息
看到license.txt。
 