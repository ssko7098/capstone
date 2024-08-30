# SOFT3888_TU08_01

**Project Title:**  P02C - Construction Safety AI  
**Project Team:** SOFT3888_TU08_01  
**Tutor:** Joshua Pople (<joshua.pople@sydney.edu.au>)  

## Project Description

This project aims to leverage AI to enhance safety on construction sites by detecting whether workers are using safety equipment correctly. The project involves developing a computer vision system capable of recognizing various safety gear, such as helmets, vests, and gloves, and ensuring they are worn properly by workers. The goal is to reduce accidents and ensure compliance with safety regulations.

## Team Members

| Name | Discord Name | Bitbucket Username | Primary Email |
|--|--|--|--|
| Sebastian Skontos | P02C Sebastian Skontos | ssko7098 | <ssko7098@uni.sydney.edu.au> |
| Daniel Geng | P02C Daniel Geng | abacus7491 | <rgen7310@uni.sydney.edu.au> |
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
| Meeting Minutes | [30/08/2024](wiki/minutes/README.md) |
| User Stories | [22/08/2024](wiki/user-stories.md) |
| Assessment - Other Mini Group Reports | [XX/XX/2024]() |
| Assessment - Individual Reports | [XX/XX/2024]() |
| Assessment - First Project Report (Group) | [XX/XX/2024]() |
| Assessment - Final Project Report (Group) | [XX/XX/2024]() |
| Assessment - Final Individual Reports | [XX/XX/2024]() |



## Version Releases

| Model | Version | Python Script | Weights | Notes |
|--|--|--|--|--|
| Seb - YOLOv8s | v1.0.0 | [View](/model_training/Seb-Model-1.ipynb) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/ssko7098_uni_sydney_edu_au/Ed6bBdoA7JlPpAacTjC66CgBjV40WEpTZFYjura93LDCzQ?e=dVwtta) | Doesn't seem to be very good at detecting people far away. This was based off of images taken from one of the construction sites. |
| Nick - YOLOv8n | v1.0.0 | [View](/model_training/Nicko-Model-1.ipynb) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/nheb2621_uni_sydney_edu_au/EeOcqku4sdtNoEKYfIk9R_IBGczHtVI7L-U2qC26D96x1g?e=xpB7t3) | Trained using open-source dataset. High probability detecting most classes (including people - normalised 90% accuracy). Difficulty detecting: bare-arms and non-helmet. |
| Otavio - YOLOv8n | v1.0.0 | [View](/model_training/Otavio-Model-1.ipynb) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/oper7179_uni_sydney_edu_au/EcNysiCF_kZPuSIp-UPWrU4BYlF3YYwkj3_yfC9xhycVjA?e=RoSePV) | Trained using open-source dataset. High probability detecting most classes. Great success of >90% at detecting people and shoes, but struggled with non-helment (~70%), and especially bare-arms (~44%). Remainder of results fell between high 70s and 80s. |


