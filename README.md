# Social Media Images in Earthquake Disaster Assessment 

Welcome to the repo of the Earthquake Infrastructure Damage (EID) assessment dataset. This repo provide an easy-to-use implementation for training and testing the EID dataset based on different deep learning models, allowing you to train it for other tasks effectively.
### [Paper](https://journals.sagepub.com/doi/10.1177/87552930251335649) |  [Dataset](https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published/PRJ-5748/#detail-0989c54e-4865-4b39-8c44-7d8a88ca8ebb)
# Data Download
Please find the EID dataset in DesignSafe: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.published/PRJ-5748/#detail-0989c54e-4865-4b39-8c44-7d8a88ca8ebb

## EID
The EID dataset is a novel 4-class Earthquake Infrastructure Damage (EID) assessment dataset compiled from a combination of images from several other social media image databases but with added emphasis on data quality. The labels description are as follows:

•	**Irrelevant or Non-Informative to Infrastructure Damage Assessment (DS0)**: No recognizable infrastructure exists in the image. For example, an image shows advertising, banners, logos, cartoons, or blurred.

•	**No damage (DS1)**: Images that show disaster-damage-free infrastructure belong to the No damage category. 

•	**Mild damage (DS2)**: Partially destroyed buildings, bridges, houses, and roads belong to the mild damage category. The infrastructure in the image shows disaster damage up to 50%. The infrastructure **remains life-safe and stable**.  

•	**Severe damage (DS3)**: Substantial destruction of an infrastructure belongs to the severe damage category. The infrastructure is **not life-safe and stable**. For example, a non-livable or non-usable building, a non-crossable bridge, or a non-drivable road, destroyed, burned crops are all examples of severely damaged infrastructures. 

For more information about the labeling guideline, please check our paper. 

## Installation

The training and evaluation requirements. Note that the code has only been tested on specific version on Linux environment. To setup all required dependencies of the training and evaluation, please follow the steps below: 

1. Create a conda environment and install dependencies:

   ```
    conda create --name EID
   ```

2. Activate the conda environment:

   ```
   conda activate EID
   ```
3. Install required packages

   ```
   pip install -r requirements.txt
   ```


## Calssification Usage

The EID dataset is placed in the `data/` directory. We also provide the train, test, and validation images&labels information in the `data/labels` folder. You can `cd` to src folder, run the training script with:

```
python train_models.py
```

Note: This will use the default model to use any other, you can change this part in the train_models.py code.
```
parser.add_argument('--arch', default='resnet18', type=str,
                    help='model architecture [resnet18, resnet50, resnet101, alexnet, vgg, vgg16, squeezenet, densenet,mobilenet_v2,vits,vitb,vitl,swinsv2,swinbv2,swintv2'
                         'inception, efficientnet-b1, efficientnet-b7] (default: resnet18)')
```

Note: We provide code and test results for ResNet, VGG16, Inception, EfficientNet, DenseNet, SqueezeNet, ViT, and Swin Transformer V2. Thanks to Alam et al. [1] provide amazing code to start. 


## Baseline Results
The performance of baseline model are listed below. The model parameters are initialized with those learned from ImageNet and load with PyTorch using the transfer learning strategy. 


| Model Name       | Accuracy (%) | F1 Score (%) |
|------------------|--------------|--------------|
| ResNet18         | 86.6         | 86.1         |
| ResNet50         | 86.8         | 86.1         |
| ResNet101        | 86.6         | 86.1         |
| VGG16            | 87.6         | 86.8         |
| Inception        | 87.5         | 86.6         |
| Efficientnetb1   | 87.4         | 87.0         |
| Efficientnetb7   | 84.9         | 84.1         |
| DenseNet         | 86.6         | 85.4         |
| SqueezeNet       | 83.0         | 82.4         |
| ViT-S            | 89.5         | 89.0         |
| ViT-B            | 90.3         | 89.7         |
| ViT-L            | 89.8         | 89.1         |
| SwinV2-T         | 90.8         | 90.5         |
| SwinV2-S         | 91.7         | 91.1         |
| SwinV2-B         | 91.0         | 90.5         |

## Checkpoint
Under construction...

## License

The EID dataset is published under CC BY-NC-SA 4.0 license, which means everyone can use this dataset for non-commercial research purpose: https://creativecommons.org/licenses/by-nc/4.0/.

## Contact

Huili Huang - huilihuang1997@gmail.com; hhuang413@gatech.edu

Please ⭐ if you find it useful so that I find the motivation to keep improving this. Thanks

## Reference
1. Firoj Alam, Tanvirul Alam, Md. Arid Hasan, Abul Hasnat, Muhammad Imran, Ferda Ofli, MEDIC: A Multi-Task Learning Dataset for Disaster Image Classification, 2021. arXiv preprint arXiv:2108.12828. https://github.com/firojalam/medic/
