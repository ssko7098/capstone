# Meeting Minutes

**Date:** Monday 9 September 2024

**Time:** 5:40 pm

**Location:** Discord

**Attendees:**

* Client Name (Cian)
* Team Member 1 (Sebastian Skontos)
* Team Member 3 (Ryan Tanevski)

**Apologies**
* Team Member 2 (Daniel Geng)
* Team Member 4 (Dmitry Khachumov)
* Team Member 5 (Ethan Acevski)
* Team Member 6 (Nicko Heberden)
* Team Member 7 (Otavio Wood)



## Agenda

* Item 1 - Q&A
* Item 2 - Sprint Plan
* Item 3 - General Business

Meeting open at: 16:00




## Item 1: Q&A

**Question: is it possible if we could upload our own datasets to strong compute, those involving images more closely related to our project (i.e. those with safety equipment).**

*Answer: Yes.

There are two ways to do this:
- Just download them into the container with wget or similar
- Send Cian the dataset in a ZIP file and he can put them up*

**Question: Is our final deliverable just everyones different models?**
*Yes, all we will be provided to give our models and the code featured in our GitHub.*


## Item 2: Sprint Plan

| Name | Unikey | Video Link |
|--|--|--|
| Sebastian Skontos | ssko7098 | Join and have a look at the weights and biases tool to track our models results, continue to train models by changing parameters |
| Daniel Geng | rgen7310 | Train a model in strong compute |
| Ryan Tanevski | rtan4242 | Train a model in strong compute, Find pre labelled data, start labelling data for helmet colours and vests ourselves with the data we found in previous weeks |
| Dmitry Khachumov | dkha5410 | Train a model in strong compute, Find pre labelled data, start labelling data for helmet colours and vests ourselves with the data we found in previous weeks |
| Otavio Pereira Wood | oper7179 | Join and have a look at the weights and biases tool to track our models results, continue to train models by changing parameters |
| Ethan Acevski | eace4343 | Train a model in strong compute, Find pre labelled data, start labelling data for helmet colours and vests ourselves with the data we found in previous weeks |
| Nicko Heberden | nheb2621 | Join and have a look at the weights and biases tool to track our models results, continue to train models by changing parameters |

## Item 3 - General Business

* We need to make a list of classes that we will all be using in our models, to make sure everyone is consistent with these.

* To label coloured helmets, we could write a cv script, looking at the area inside the helmet label, and average out the colour to do automatic labelling.

* Cian might be offering money for some teams to label data, this will be in a few weeks if it does happen.

Meeting closed at:  17:55
