# Covid Website
## What is the current problem?

  When someone comes to a hospital with symptoms of Covid-19 and/or Pneumonia it is vital that they get a timely and accurate diagnosis. A Covid-19 diagnosis requires either a saliva test, or a nasopharyngeal culture test, and Covid-19 Pneumonia requires an additional radiograph. For those with symptoms of Covid-19 Pneumonia, that prolonged time can affect treatment outcomes and the overall health of the patient. This time is crucial for those who are admitted in critical condition and need immediate care. 

## What is the goal of this project?

  The goal of this project is to create a machine learning algorithm that can detect and differentiate Covid-19 Pneumonia, versus bacterial pneumonia, versus a healthy patient through radiographs like the images above. This would provide a one-step diagnostic tool to diagnose Covid pneumonia, and eliminate the two step process of a PCR test followed by a chest radiograph. These two-steps would be consolidated into one radiograph detected by machine learning. It also dictates having the accuracy comparable to current FDA-approved Covid-19 testing[3] and radiological experts. It is expected that after training the algorithm will have a test accuracy of around 94%. Limited prior institutional research has been done with the novelty of the virus.

## Methods and Procedures
### Designing the AI

  To optimize the accuracy of the model, over 10,000 training images were pather through a deep convolutional neural network. Model Shown below:
  ![visualVGG-4](https://user-images.githubusercontent.com/35374275/112232877-97cde180-8bf6-11eb-9908-9f23523ed6ac.png)

  With the following parameters:
  
  
  
  <img width="400" alt="Screen Shot 2021-03-23 at 4 30 50 PM" src="https://user-images.githubusercontent.com/35374275/112233020-debbd700-8bf6-11eb-9066-9e8ad99da639.png">

### Testing the AI

Data was saved as “history” with a validation split of .2, and a batch size of 16. A test set will be created using a random set of 90 validation images. Final accuracy will be determined from the results of that set. Using matplotlib.pyplot and skimage.io images were displayed and saved to be analyzed for further data collection. Data collection includes, but is not limited to, the use of training and validation accuracy and loss graph, heat maps, a confusion matrix, the calculation of precision, recall, f1-score, and support values, a graph for the ROC (Receiver operating characteristic) or multi-class data, scatterplots showing the relationship between principal components, pixel importance graphs, and labeled actual and predicted images. The training was constructed using the TensorFlow backend and utilized GPU acceleration. The training utilized TensorFlow ModelCheckpoint and EarlyStopping. The optimizer chosen was Adam. The size of images used for training was 224 x 224. 

## Conclusion
The goal of this project was to create an algorithm that could detect Covid-19 Pneumonia based on an x-ray scan of the chest. It also needed to be able to differentiate Covid-19 Pneumonia, from Bacterial Pneumonia, and be able to differentiate a healthy lung. All of this was important to help speed up the detection of Covid-19 in patients, especially in an ICU setting, where patients need immediate and critical care for their illness. At the conclusion of testing, the algorithm met its target test accuracy of greater than 94%. After training the final test accuracy, and evaluted with over 1000 images, the algorithm had an accuracy of over 95%. 

