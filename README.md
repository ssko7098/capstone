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
| Complete Model Overview | [20/10/2024](model_training/overview.md)
| Final Client Deployment W&B Report | [23/10/2024](https://wandb.ai/sebastian-skontos-university-of-sydney/Ultralytics/reports/Final-Client-Deployment--Vmlldzo5ODQ2MTI4?accessToken=1d583be5ivrb5qcbscmaqcxg229y3mklo46007ngofs8sfgj1vnw4yc9zodj3pbe) |



## Best Models
| Model | Argument File | Dataset | Weights File | Confusion Matrix |
|--|--|--|--|--|
Best Person | [Download](model_training/yolov8n/seb-model-2/seb-model-2.py) | fmg_data_2 | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/ssko7098_uni_sydney_edu_au/EaDTFjmQIhVCrwj6wdSA1SABvlqnRweiH815twrWVovzZw?e=ElDYwE) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/nheb2621_uni_sydney_edu_au/EeTP-dYUz4hEg3IxaFJvmJcBI0RgH47rAVLOKApd_YSjXA?e=2A2CkR) |
Seb's Best PPE | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/ssko7098_uni_sydney_edu_au/EY-bxs8K-IJPuvlTwoBEqbcB9gDfWrPezFjKTOsPlYJ8hA?e=1PQZhN) | [Custom Roboflow](https://universe.roboflow.com/sharedcapstone/soft3888) | [Download](https://unisydneyedu-my.sharepoint.com/:u:/g/personal/ssko7098_uni_sydney_edu_au/EXoGeHja9M9MmVdcBtblWo8B-apuwxIr9gDW_xS0zEP8Cg?e=xXhJUJ) | [View](https://unisydneyedu-my.sharepoint.com/:i:/g/personal/ssko7098_uni_sydney_edu_au/EfuqxNBXuJpJtA51hpjk1TUBlMP1rSKTmjr5Kqytajt4VQ?e=9gohHS) |



## Model Inference
Please follow the [Model Inference](test/model-inference/model_inference.ipynb) guide.
Models are to be downloaded from the above releases.

An image set provided by Cian can be found [here](https://unisydneyedu-my.sharepoint.com/:f:/g/personal/nheb2621_uni_sydney_edu_au/EjdFBfYNE1dGjMsXUitEmf4BXxMpZs-qUwxqc_Fd7BuaPg?e=gS0XcN)
