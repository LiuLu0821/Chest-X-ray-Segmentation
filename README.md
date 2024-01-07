东北大学自然语言处理课程期末作业

使用文本Prompt改进胸部X射线图像中感染区域的分割

 	Environment:
	python=3.8  
	torch=1.12.1  
	torchvision=0.13.1  
	pytorch_lightning=1.9.0  
	torchmetrics=0.10.3  
	transformers=4.24.0  
	monai=1.0.1  
	pandas  
	einops 

	Datasets:
 	QaTa-COV19: [https://www.kaggle.com/datasets/aysendegerli/qatacov19-dataset](https://www.kaggle.com/datasets/aysendegerli/qatacov19-dataset)

	训练:  ```python train.py```  
 	验证：```python evaluate.py```
