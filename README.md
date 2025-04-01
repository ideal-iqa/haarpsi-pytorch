# HaarPSI PyTorch
This is the repository of the HaarPSI PyTorch implementation presented in the papers ["A study on the adequacy of common IQA measures for medical images"](https://arxiv.org/abs/2405.19224) and ["Parameter choices in HaarPSI for IQA with medical images"](https://arxiv.org/abs/2410.24098).

### Highlights:
1. A full-reference IQA measure with promising performance in several studies.
2. It allows adaption to different data sources by adapting the parameters $C$ and $\alpha$.
3. The original parameters for natural image data sets and new parameters for medical image data sets are provided.

HaarPSI is a Haar wavelet based full reference image quality assessment (FR-IQA) measure as presented in "A Haar wavelet-based perceptual similarity index for image quality assessment" by Rafael Reisenhofer, Sebastian Bosse, Gitta Kutyniok and Thomas Wiegand.

This repository contains a Python PyTorch HaarPSI implementation based on the original Python TensorFlow implementation written by David Neumann and on the original MATLAB implementation written by Rafael Reisenhofer.


If you use this HaarPSI implementation, please cite those two papers:

```
@InProceedings{breger2024study,
      title={A study on the adequacy of common IQA measures for medical images}, 
      author={Anna Breger and Clemens Karner and Ian Selby and Janek Gröhl and Sören Dittmer and Edward Lilley and Judith Babar and Jake Beckford and Timothy J Sadler and Shahab Shahipasand and Arthikkaa Thavakumar and Michael Roberts and Carola-Bibiane Schönlieb},
      year={2024},
      eventtitle={Medical Imaging and Computer-Aided Diagnosis (MICAD) 2024},
      series={Springer Lecture Notes in Electrical Engineering},
      venue={Manchester, UK}
}
```


```
@inproceedings{karner2025parameterchoiceshaarpsiiqa,
      title={Parameter choices in HaarPSI for IQA with medical images}, 
      author={Clemens Karner and Janek Gröhl and Ian Selby and Judith Babar and Jake Beckford and Thomas R Else and Timothy J Sadler and Shahab Shahipasand and Arthikkaa Thavakumar and Michael Roberts and James H. F. Rudd and Carola-Bibiane Schönlieb and Jonathan R Weir-McCall and Anna Breger},
      booktitle={2025 IEEE International Symposium on Biomedical Imaging (ISBI)},
      year={2025},
      organization={IEEE}
}
```

### Installation:

Tested with:
* Python 3.11.5
* Torch 2.5.1

Example:

```python
from haarpsi import haarpsi
import torch

#Please note that this implementation requires images scaled to [0,1].
ImgA=torch.ones(100, 100)
ImgB=torch.ones(100, 100)

#  Choose the parameter C in the range [5,100], suggested values:
#  Natural images: 30
#  Medical images: 5
C=5

#  Choose the parameter alpha in the range [2,8], suggested values:
#  Natural images: 4.2
#  Medical images: 4.9
Alpha=5.8

(Similarity_score, Local_similarity, Weights)=haarpsi(ImgA,ImgB,C,Alpha)
```
