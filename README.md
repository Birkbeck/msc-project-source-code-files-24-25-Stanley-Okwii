# Adversarial training with ResNet-50
Researching influence of adversarial training on AI model performance

## To Run
- Clone this repository
- Download data from Imagenet2012(https://www.image-net.org)
- In the root directory, run `python -m venv .venv ` to create a virtual environment.
- Activate the virtual environment by running `source .venv/bin/activate`
- Run `pip install -r requirements.txt -q`
- In VS code, select the kernel as the `venv`
- Run each of the notebooks in the order below:-
    - data_processing.ipynb - Preprocess the data, shows the dataset class distribution and generates adversarial data
    - resnet_50_base_metrics - Evaluates the base resnet-50 against adversarial and standard test dataset
    - adversarial_model_training - Use adversarial data to retrain the model, generating a robust model as the result
    - performance_evaluation - Evaluates performance of adversarially trained resnet-50 model.
