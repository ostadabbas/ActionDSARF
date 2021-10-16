# A Bayesian Dynamical Approach for Human Action Recognition

This repository is a pytorch implementation of our paper:
A. Farnoosh, Z. Wang, S. Zhu, and S. Ostadabbas, “A Bayesian Dynamical Approach for Human Action Recognition,” Sensors, 2021.

Check out this [notebook](./DSARF Action Recognition.ipynb) for our implementation of the model.

#### Dependencies: 
Pytorch, Numpy, Scipy, Matplotlib, Sklearn

#### Datasets:

[NTU RGB+D 60](https://rose1.ntu.edu.sg/dataset/actionRecognition/)

[Human3.6M](http://vision.imar.ro/human3.6m/description.php)

You can use `process_36M.py` to preprocess Human3.6M dataset.

#### Citation

If you find our work useful in your research please consider citing our paper:
```
@article{farnoosh2021bayesian,
  title={A Bayesian Dynamical Approach for Human Action Recognition},
  author={Farnoosh, Amirreza and Wang, Zhouping and Zhu, Shaotong and Ostadabbas, Sarah},
  journal={Sensors},
  volume={21},
  number={16},
  pages={5613},
  year={2021},
  publisher={Multidisciplinary Digital Publishing Institute}
}
