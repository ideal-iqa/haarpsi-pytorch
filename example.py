import haarpsi
import torch

#Please note that this implementation requires images scaled to [0,1].
ImgA=torch.ones(100, 100)
ImgB=torch.ones(100, 100)

#  Choose the parameter C in the range [5,100], suggested values:
#  Natural images: 30
#  Medical images: 5
C=5

#  Choose the parameter alpha in the range [2,8], suggested values:
#  Natural images: 4,2
#  Medical images: 5.8
alpha=5.8

(similarity_score, local_similarity, weights)=haarpsi(ImgA,ImgB,C,alpha)
