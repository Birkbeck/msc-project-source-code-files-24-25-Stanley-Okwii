# Adversarial training with ResNet-50
Researching influence of adversarial training on AI model performance

TODO: Push code to personal repository, since I can't fork from BBK

## To Run
- Clone repository
- Download data from imagenet - 2015
- In the root directory, run `python -m venv .venv ` to create a virtual environment
- `source .venv/bin/activate`
- Run `pip install -r requirements.txt -q`
- In VS code, select the kernel as the venv created earlier


https://obscure-space-guacamole-vpjj677559xcpwpr-8888.app.github.dev/tree/?token=954d884b00e481a18407a258d43af5f6c42639e8a20a25db

Run notebook in the background: jupyter execute src/adversarial_data_generation.ipynb  &> jupyter_server.log & disown
