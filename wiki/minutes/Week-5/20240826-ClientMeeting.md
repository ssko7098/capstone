# Meeting Minutes

**Date:** Monday 26 August 2024

**Time:** 4:00 pm

**Location:** Discord

**Attendees:**

* Client Name (Cian)
* Team Member 2 (Daniel Geng)
* Team Member 3 (Ryan Tanevski)
* Team Member 4 (Dmitry Khachumov)
* Team Member 5 (Ethan Acevski)
* Team Member 6 (Nicko Heberden)
* Team Member 7 (Otavio Wood)

**Apologies**
* Team Member 1 (Sebastian Skontos)


## Agenda

* Item 1 - Q&A
* Item 2 - Sprint Plan
* Item 3 - General Business

Meeting open at: 16:00




## Item 1: Q&A

**Question: What can the team do to find more distinct roles**

*Answer: Everyone should be able to train a model. Some members can have a go at training YOLOv10 model instead and assess results to see if the model is better than YOLOv8. Different members can work on different datasets to get a wide range of AI training. We can have decdicated members responsible for augmenting datasets. This includes blurring, flipping rotating, zooming, etc. on images to provide more data to train on. 

User the model outputs liek average precision score to see if more training will actually improve the model. Message Calvin on discord if you are having trouble understanding the results. Try using bigger YOLO models for better results, like YOLOv10.*

**Question: Should we segment models into day and night models?**
*Yes excellent idea. Spoke to AI experts and they said that this is the standard and a must for accuracy.*

**Question: Will ISC be used for deployment?**

*No, ISC is just for training. The model will be deployed on Cian's own system.*

**Question: How can we better diversify our roles?**

*Perhaps 3 small teams:
1 for Data, researching, collating, reformatting to be used in yolo formats.No labelled data set has been provided so it will be a big problem going forward unless we find them open source. 1 for Augmentation: Doubling, tripling, the size of data through flipping, rotating, zooming, etc etc !! Big job. 1 for Training and analysing results, data labelling*

**Question: Have other teams got isc working**

*Answer: As far as Cian knows, no other teams have been able to train a model using ISC at this moment. This is something that we look to achieve this week.*


## Item 2: Sprint Plan

| Name | Unikey | Video Link |
|--|--|--|
| Sebastian Skontos | ssko7098 | Create ISC tutorial. Gain metrics relating to the the models detection of safety equipment |
| Daniel Geng | rgen7310 | Train a model on ISC with various datasets, Alter existing datasets to create more data |
| Ryan Tanevski | rtan4242 | Train a model on ISC with various datasets, experiemnt with a YOLOv10 model |
| Dmitry Khachumov | dkha5410 | Train a model on ISC with various datasets, Alter existing datasets to create more data |
| Otavio Pereira Wood | oper7179 | Train a model on ISC with various datasets, Alter existing datasets to create more data |
| Ethan Acevski | eace4343 | Train a model on ISC with various datasets, experiemnt with a YOLOv10 model |
| Nicko Heberden | nheb2621 | Train a model on ISC with various datasets, Gain metrics relating to the the models detection of safety equipment |

## Item 3 - General Business

* Annotating the live public data sets is not a priority for our team, as we are focusing more on the clothing and gear rather than the cosntruction site as a whole.

* Look into getting our own annotations and data for images with construction gear.

* By Wednesday Cian would like trained models going able to identify people. We must gain some data relating to safety equipment metrics. Cian would like a working pipeline and outputted results by Wednesday.

* Look at model outputs to see if more training can make the model better. If so, train more. Send charts and outputs to isc chat so the technical can identify this if we are struggling. 

Meeting closed at:  16:20
