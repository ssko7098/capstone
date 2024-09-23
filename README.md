# SOFT3888_TU08_01

**Project Title:**  P02C - Construction Safety AI  
**Project Team:** SOFT3888_TU08_01  
**Tutor:** Joshua Pople (<joshua.pople@sydney.edu.au>)  

## Project Description

This project aims to leverage AI to enhance safety on construction sites by detecting whether workers are using safety equipment correctly. The project involves developing a computer vision system capable of recognizing various safety gear, such as helmets, vests, and gloves, and ensuring they are worn properly by workers. The goal is to reduce accidents and ensure compliance with safety regulations.

## Coding Style

Training scripts are to follow the PEP-8 style guide for python code. This is done to ensure consistency in the repository.


## Team Members

| Name | Discord Name | Bitbucket Username | Primary Email |
|--|--|--|--|
| Sebastian Skontos | P02C Sebastian Skontos | ssko7098 | <ssko7098@uni.sydney.edu.au> |
| Ryan Tanevski | P02C Ryan Tanevski | p02ryantanevski | <rtan4242@uni.sydney.edu.au> |
| Dmitry Khachumov | P02C Dmitry Khachumov | dmitrykhachumov_06339 | <dkha5410@uni.sydney.edu.au> |
| Otavio Pereira Wood | P02C Otavio Wood | oper7179 | <oper7179@uni.sydney.edu.au> |
| Ethan Acevski | P02C Ethan Acevski | eace4343_60612 | <eace4343@uni.sydney.edu.au> |
| Nicko Heberden | P02C Nicko Heberden | hebbooooo | <nheb2621@uni.sydney.edu.au> |

## Client Information

| Name | Email | Username
|--|--|--|
| Cian Byrne | <cian.byrne@coliemore.com.au> | wallarug |

## Table of Contents

| Section | Last Updated |
|--|--|
| Group Contract Weeks 2-5 | [10/08/2024](https://docs.google.com/document/d/18aAVpdywvQ0mdwcO19D_DLwmfNz0LkLy/edit?usp=sharing&ouid=103567359036304240364&rtpof=true&sd=true) |
| Meeting Minutes | [10/09/2024](wiki/minutes/README.md) |
| User Stories | [22/08/2024](wiki/user-stories.md) |
| 1st Client Deployment Feedback | [13/09/2024](/wiki/1st%20Client%20Deployment%20Feedback.md) |
| Demo Video Showcasing Models | [22/09/2024](https://drive.google.com/file/d/1NgjKxZ2MebZubTv0halGT6Sw38w8CbG1/view?usp=sharing) |



## Version Releases
### YOLOv8s
| Model | Version | Python Script | Dataset | Weights | Confusion Matrix | Notes |
|--|--|--|--|--|--|--|
| Seb Model 1 | v1.0.0 | [View](model_training/yolov8s/seb-model-1/seb-model-1.ipynb) | [Roboflow](https://universe.roboflow.com/akfa-beqxl/safety-rd-v1/dataset/1) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/ssko7098_uni_sydney_edu_au/Ed6bBdoA7JlPpAacTjC66CgBjV40WEpTZFYjura93LDCzQ?e=dVwtta) | [View]() | Doesn't seem to be very good at detecting people far away. This was based off of images taken from one of the construction sites. |
| Seb PPE Model 1 | v1.0.0 | [View](model_training/yolov8s/seb-model-1/PPE-model-1-train.py) | [Roboflow](https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6IndTNThqQTJWMnNSRU9SNElDM3d0MERUbFBJMzMiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoiZG1pdHJ5LmtoYWNodW1vdkBnbWFpbC5jb20iLCJpYXQiOjE3MjY5ODE2OTR9.Fn20fK_X09zucumvY8c3k_0-VQxnqQ7bZpzxAoHvVRw) | [Download](https://drive.google.com/file/d/1j4y6Qr86VGYcMqaxP-BNpth3VLKnZLxm/view?usp=sharing) | [View]() | Pretty good at detecting helmets, but not so much at detecting other PPE such as vests and shoes. |

### YOLOv8n
| Model | Version | Python Script | Dataset | Weights | Confusion Matrix | Notes |
|--|--|--|--|--|--|--|
| Nick Model 1 | v1.0.0 | [View](model_training/yolov8n/nicko-model-1/nicko-model-1.ipynb) | [Roboflow](https://universe.roboflow.com/akfa-beqxl/safety-rd-v1/dataset/1) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/nheb2621_uni_sydney_edu_au/EeOcqku4sdtNoEKYfIk9R_IBGczHtVI7L-U2qC26D96x1g?e=xpB7t3) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EZrskR_0N9RHl6GmgRe41dgBdiM9D18Zq34Xm7Y0p50Xzg?e=LDPElz) | Trained using open-source dataset. High probability detecting most classes (including people - normalised 90% accuracy). Difficulty detecting: bare-arms and non-helmet. |
| Otavio Model 1 | v1.0.0 | [View](model_training/yolov8n/otavio-model-1/otavio-model-1.ipynb) | [Roboflow](https://universe.roboflow.com/akfa-beqxl/safety-rd-v1/dataset/1) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/oper7179_uni_sydney_edu_au/EcNysiCF_kZPuSIp-UPWrU4BYlF3YYwkj3_yfC9xhycVjA?e=RoSePV) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EaILQV1-mP9FirQ8R9AekuoBI6DA3NOeb6mMfZk2P6Mbqw?e=Yrr11T) | Trained using open-source dataset. High probability detecting most classes. Great success of >90% at detecting people and shoes, but struggled with non-helment (~70%), and especially bare-arms (~44%). Remainder of results fell between high 70s and 80s. |
| Seb Model 2 | v1.0.0 | [View](model_training/yolov8n/seb-model-2/seb-model-2.py) | fmg_data2 | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/ssko7098_uni_sydney_edu_au/EaDTFjmQIhVCrwj6wdSA1SABvlqnRweiH815twrWVovzZw?e=ElDYwE) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EeTP-dYUz4hEg3IxaFJvmJcBI0RgH47rAVLOKApd_YSjXA?e=2A2CkR) | Trained using the fmg_data_2 dataset using images from the actual site. Achieved 82% normalized accuracy for detecting people. |
| Nicko Model 2 | v2.0.0 | [View](model_training/yolov8n/nicko-model-2/nicko-model-2.py) | fmg_data | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/nheb2621_uni_sydney_edu_au/ESSfuFbsNMxMo-1CRXtxDTEB9RAWboOxow-4IJF69oQnKw?e=PWJWO2) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EVFwLqjwj-dOtZG5wV-UNgYBdJkCcvJCoS5vUZpV4lj6QA?e=rR3rRT) | Trained on Strong Compute CPU's using the fmg_data dataset. Achieved 88% normalized accuracy when detecting people. |

### YOLOv8m
| Model | Version | Python Script | Dataset | Weights | Confusion Matrix | Notes |
|--|--|--|--|--|--|--|
| Nicko Model 3 | v1.0.0 | [View](model_training/yolov8m/nicko-model-3/nicko-model-3.py) | fmg_data |[Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/nheb2621_uni_sydney_edu_au/Ee6LvIjE9ohJrdNtMHDpRA0B2MkoZ4tuikwGm11E_8j5YA?e=skIDGC) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EXibqUfDnO5IjZ6lJ5BwqEgB24Hq3mTpGvoQX8kheda2MQ?e=5P9vJZ) | The initial YOLOv8m model achieved a 78% probability in detecting people. However, when tested on Cian's external images, the model only detected cranes, indicating potential issues with generalisation to unseen data. |
| Nicko Model 4 | v1.0.0 | [View](model_training/yolov8m/nicko-model-4/nicko-model-4.py) | fmg_data |[Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/nheb2621_uni_sydney_edu_au/EfBk98-MQVdGgK074_Oh2QIBC57nBIj7-d2PevLmPfTwOA?e=ndyUm9) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EVLPzWz2YXNHlqCwqG8GFtcBkOjcqcoZjXAzfMdWpdOong?e=bSEAx6) | Trained using a new custom Roboflow dataset focused on PPE as per clients instructions. High normalised detection accuracy for vests (96%), helmets (94%), boots (92%), and gloves (89%). Poor performance detecting goggles  (6%). |

## Model Inference
Please follow the [Model Inference](test/model-inference/model_inference.ipynb) guide.
Models are to be downloaded from the above releases.

An image set provided by Cian can be found [here](https://unisydneyedu-my.sharepoint.com/:f:/g/personal/nheb2621_uni_sydney_edu_au/EjdFBfYNE1dGjMsXUitEmf4BXxMpZs-qUwxqc_Fd7BuaPg?e=gS0XcN)