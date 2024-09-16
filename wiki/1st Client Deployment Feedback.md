# 1st Client Deployment Feedback

Overall, excellent client deployment.

## Summary

- No User stories mentioned directly but discussed throughout.
- Diagrams of high-level project was good.
- said people were pixelated and blurry, but then said resolution was too high.
- Utilising the roboflow datasets (perform better).
- YOLOv8n model
- Predictions on Enlaps data much better than FMG site (1st model)
  - second model was much better (YOLOv8n) trained on roboflow data
  - thrid model very bad on FMG, kind of alright on Enlaps.
  - fourth model:  similar results
- Dataset potentially a problem.
- looking at learning rate.
- Strengths and weaknesses discussed in detail.
- Testing:
  - Model Inference
  - Unit testing
  - CI/CD pipeline for code standards, etc.


- Some of the ML/AI work needed to train a model is now done, which is great.  As stated in demo, your team needs to quickly shift focus over to safety equipment now rather than the just people.



## Questions
1. How did you come up with the value of 1020 pixels as the image size?
2. Do you have any theories why the model picked up a person in the dataset at 99% accuracy?
3. Are you tracking model training on Weights and Biases?
4. What additional datasets has your team found that can help with this project?
5. Your datasets seen during the demo mentioned that the names mattered. e.g. Helment vs Hardhat were not compadible.  My understanding was it used the IDs rather than the string for training. Could you elaborate on this a little bit please?


## Code review feedback
This is based purely on the feedback provided by the paired team.  It has been santised and paraphrased here for your convenience.

The documentation was very clear for installing and setting up the application.  There could be improvements made to how to run the software and letting users know where the results will be found.

The Notebook structure is very clean and easy to follow.  The README on the GitHub homepage was great.  

Adding how to run the software on a local machine would be helpful, along with documentation on setting the correct permissions for the image files.



Overall, great job with the deployment.