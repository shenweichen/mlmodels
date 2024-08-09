# DeepCTR

[![Python Versions](https://img.shields.io/pypi/pyversions/deepctr.svg)](https://pypi.org/project/deepctr)
[![TensorFlow Versions](https://img.shields.io/badge/TensorFlow-1.4+/2.0+-blue.svg)](https://pypi.org/project/deepctr)
[![Downloads](https://pepy.tech/badge/deepctr)](https://pepy.tech/project/deepctr)
[![PyPI Version](https://img.shields.io/pypi/v/deepctr.svg)](https://pypi.org/project/deepctr)
[![GitHub Issues](https://img.shields.io/github/issues/shenweichen/deepctr.svg
)](https://github.com/shenweichen/deepctr/issues)
<!-- [![Activity](https://img.shields.io/github/last-commit/shenweichen/deepctr.svg)](https://github.com/shenweichen/DeepCTR/commits/master) -->


[![Documentation Status](https://readthedocs.org/projects/deepctr-doc/badge/?version=latest)](https://deepctr-doc.readthedocs.io/)
![CI status](https://github.com/shenweichen/deepctr/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/shenweichen/DeepCTR/branch/master/graph/badge.svg)](https://codecov.io/gh/shenweichen/DeepCTR)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d4099734dc0e4bab91d332ead8c0bdd0)](https://www.codacy.com/gh/shenweichen/DeepCTR?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=shenweichen/DeepCTR&amp;utm_campaign=Badge_Grade)
[![Discussion](https://img.shields.io/badge/chat-wechat-brightgreen?style=flat)](./README.md#DiscussionGroup)
[![License](https://img.shields.io/github/license/shenweichen/deepctr.svg)](https://github.com/shenweichen/deepctr/blob/master/LICENSE)
<!-- [![Gitter](https://badges.gitter.im/DeepCTR/community.svg)](https://gitter.im/DeepCTR/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) -->


DeepCTR is a **Easy-to-use**, **Modular** and **Extendible** package of deep-learning based CTR models along with lots of
core components layers which can be used to easily build custom models.You can use any complex model with `model.fit()`
，and `model.predict()` .

- Provide `tf.keras.Model` like interfaces for **quick experiment**. [example](https://deepctr-doc.readthedocs.io/en/latest/Quick-Start.html#getting-started-4-steps-to-deepctr)
- Provide  `tensorflow estimator` interface for **large scale data** and **distributed training**. [example](https://deepctr-doc.readthedocs.io/en/latest/Quick-Start.html#getting-started-4-steps-to-deepctr-estimator-with-tfrecord)
- It is compatible with both `tf 1.x`  and `tf 2.x`.

Some related projects:

- DeepMatch: https://github.com/shenweichen/DeepMatch
- DeepCTR-Torch: https://github.com/shenweichen/DeepCTR-Torch

Let's [**Get Started!**](https://deepctr-doc.readthedocs.io/en/latest/Quick-Start.html)([Chinese
Introduction](https://zhuanlan.zhihu.com/p/53231955)) and [welcome to join us!](./CONTRIBUTING.md)

## Models List

|                 Model                  | Paper                                                                                                                                                           |
| :------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  Convolutional Click Prediction Model  | [CIKM 2015][A Convolutional Click Prediction Model](http://ir.ia.ac.cn/bitstream/173211/12337/1/A%20Convolutional%20Click%20Prediction%20Model.pdf)             |
| Factorization-supported Neural Network | [ECIR 2016][Deep Learning over Multi-field Categorical Data: A Case Study on User Response Prediction](https://arxiv.org/pdf/1601.02376.pdf)                    |
|      Product-based Neural Network      | [ICDM 2016][Product-based neural networks for user response prediction](https://arxiv.org/pdf/1611.00144.pdf)                                                   |
|              Wide & Deep               | [DLRS 2016][Wide & Deep Learning for Recommender Systems](https://arxiv.org/pdf/1606.07792.pdf)                                                                 |
|                 DeepFM                 | [IJCAI 2017][DeepFM: A Factorization-Machine based Neural Network for CTR Prediction](http://www.ijcai.org/proceedings/2017/0239.pdf)                           |
|        Piece-wise Linear Model         | [arxiv 2017][Learning Piece-wise Linear Models from Large Scale Data for Ad Click Prediction](https://arxiv.org/abs/1704.05194)                                 |
|          Deep & Cross Network          | [ADKDD 2017][Deep & Cross Network for Ad Click Predictions](https://arxiv.org/abs/1708.05123)                                                                   |
|   Attentional Factorization Machine    | [IJCAI 2017][Attentional Factorization Machines: Learning the Weight of Feature Interactions via Attention Networks](http://www.ijcai.org/proceedings/2017/435) |
|      Neural Factorization Machine      | [SIGIR 2017][Neural Factorization Machines for Sparse Predictive Analytics](https://arxiv.org/pdf/1708.05027.pdf)                                               |
|                xDeepFM                 | [KDD 2018][xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems](https://arxiv.org/pdf/1803.05170.pdf)                         |
|         Deep Interest Network          | [KDD 2018][Deep Interest Network for Click-Through Rate Prediction](https://arxiv.org/pdf/1706.06978.pdf)     |
|                AutoInt                 | [CIKM 2019][AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks](https://arxiv.org/abs/1810.11921)                              |
|    Deep Interest Evolution Network     | [AAAI 2019][Deep Interest Evolution Network for Click-Through Rate Prediction](https://arxiv.org/pdf/1809.03672.pdf)                                            |
|                FwFM                    | [WWW 2018][Field-weighted Factorization Machines for Click-Through Rate Prediction in Display Advertising](https://arxiv.org/pdf/1806.03514.pdf)                |
|                  ONN                  | [arxiv 2019][Operation-aware Neural Networks for User Response Prediction](https://arxiv.org/pdf/1904.12579.pdf)                                                |
|                 FGCNN                  | [WWW 2019][Feature Generation by Convolutional Neural Network for Click-Through Rate Prediction ](https://arxiv.org/pdf/1904.04447)                             |
|     Deep Session Interest Network      | [IJCAI 2019][Deep Session Interest Network for Click-Through Rate Prediction ](https://arxiv.org/abs/1905.06482)                                                |
|                FiBiNET                 | [RecSys 2019][FiBiNET: Combining Feature Importance and Bilinear feature Interaction for Click-Through Rate Prediction](https://arxiv.org/pdf/1905.09433.pdf)   |
|                FLEN                    | [arxiv 2019][FLEN: Leveraging Field for Scalable CTR Prediction](https://arxiv.org/pdf/1911.04690.pdf)   |
|                 BST                   | [DLP-KDD 2019][Behavior sequence transformer for e-commerce recommendation in Alibaba](https://arxiv.org/pdf/1905.06874.pdf)                           | 
|                IFM                 | [IJCAI 2019][An Input-aware Factorization Machine for Sparse Prediction](https://www.ijcai.org/Proceedings/2019/0203.pdf)   |
|                DCN V2                    | [arxiv 2020][DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems](https://arxiv.org/abs/2008.13535)   |
|                DIFM                 | [IJCAI 2020][A Dual Input-aware Factorization Machine for CTR Prediction](https://www.ijcai.org/Proceedings/2020/0434.pdf)   |
|   FEFM and DeepFEFM                    | [arxiv 2020][Field-Embedded Factorization Machines for Click-through rate prediction](https://arxiv.org/abs/2009.09931)                                         |
|              SharedBottom               | [arxiv 2017][An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/pdf/1706.05098.pdf)  |
|   ESMM                    | [SIGIR 2018][Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate](https://arxiv.org/abs/1804.07931)                       |
|   MMOE                    | [KDD 2018][Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts](https://dl.acm.org/doi/abs/10.1145/3219819.3220007)                   |
|   PLE                    | [RecSys 2020][Progressive Layered Extraction (PLE): A Novel Multi-Task Learning (MTL) Model for Personalized Recommendations](https://dl.acm.org/doi/10.1145/3383313.3412236)                   |
|   EDCN                   | [KDD 2021][Enhancing Explicit and Implicit Feature Interactions via Information Sharing for Parallel Deep CTR Models](https://dlp-kdd.github.io/assets/pdf/DLP-KDD_2021_paper_12.pdf)                   |

## Citation

- Weichen Shen. (2017). DeepCTR: Easy-to-use,Modular and Extendible package of deep-learning based CTR
  models. https://github.com/shenweichen/deepctr.

If you find this code useful in your research, please cite it using the following BibTeX:

```bibtex
@misc{shen2017deepctr,
  author = {Weichen Shen},
  title = {DeepCTR: Easy-to-use,Modular and Extendible package of deep-learning based CTR models},
  year = {2017},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/shenweichen/deepctr}},
}
```

## DiscussionGroup

- [Github Discussions](https://github.com/shenweichen/DeepCTR/discussions)
- Wechat Discussions

|公众号：浅梦学习笔记|微信：deepctrbot|学习小组 [加入](https://t.zsxq.com/026UJEuzv) [主题集合](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MzY4NzE3MA==&action=getalbum&album_id=1361647041096843265&scene=126#wechat_redirect)|
|:--:|:--:|:--:|
| [![公众号](./docs/pics/code.png)](https://github.com/shenweichen/AlgoNotes)| [![微信](./docs/pics/deepctrbot.png)](https://github.com/shenweichen/AlgoNotes)|[![学习小组](./docs/pics/planet_github.png)](https://t.zsxq.com/026UJEuzv)|

## Main contributors([welcome to join us!](./CONTRIBUTING.md))

<table border="0">
  <tbody>
    <tr align="center" >
      <td>
        ​ <a href="https://github.com/shenweichen"><img width="70" height="70" src="https://github.com/shenweichen.png?s=40" alt="pic"></a><br>
        ​ <a href="https://github.com/shenweichen">Shen Weichen</a> ​
        <p>
        Alibaba Group  </p>​
      </td>
      <td>
         <a href="https://github.com/zanshuxun"><img width="70" height="70" src="https://github.com/zanshuxun.png?s=40" alt="pic"></a><br>
         <a href="https://github.com/zanshuxun">Zan Shuxun</a> ​
        <p>Alibaba Group  </p>​
      </td>
      <td>
        ​ <a href="https://github.com/pandeconscious"><img width="70" height="70" src="https://github.com/pandeconscious.png?s=40" alt="pic"></a><br>
        ​ <a href="https://github.com/pandeconscious">Harshit Pande</a>
        <p> Amazon   </p>​
      </td>
      <td>
        ​ <a href="https://github.com/morningsky"><img width="70" height="70" src="https://github.com/morningsky.png?s=40" alt="pic"></a><br>
        ​ <a href="https://github.com/morningsky">Lai Mincai</a>
        <p> ByteDance </p>​
      </td>
      <td>
        ​ <a href="https://github.com/codewithzichao"><img width="70" height="70" src="https://github.com/codewithzichao.png?s=40" alt="pic"></a><br>
        ​ <a href="https://github.com/codewithzichao">Li Zichao</a>
        <p> ByteDance   </p>​
      </td>
      <td>
        ​ <a href="https://github.com/TanTingyi"><img width="70" height="70" src="https://github.com/TanTingyi.png?s=40" alt="pic"></a><br>
         <a href="https://github.com/TanTingyi">Tan Tingyi</a>
         <p>  Chongqing University <br> of  Posts and <br> Telecommunications   </p>​
      </td>
    </tr>
  </tbody>
</table>
