<div align="center">
<img src="assets/logo.jpg" alt="drawing" width="400"/> <br />


# House Price model deployment on AWS

![Badge](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Badge](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

![Badge](https://img.shields.io/github/languages/code-size/bryanlusse/HousePrices__DeployedModel)
![Badge](https://img.shields.io/github/languages/count/bryanlusse/HousePrices__DeployedModel)
![Badge](https://img.shields.io/github/last-commit/bryanlusse/HousePrices__DeployedModel)

[Overview](#scroll-overview)
•
[How to use](#chart_with_upwards_trend-model)
</div>

## :bookmark_tabs: Menu

- [Overview](#scroll-overview)
- [How to use](#chart_with_upwards_trend-model)
- [Requirements](#exclamation-requirements)
- [Folder Structure](#closedbook-results)
- [Author](#smiley_cat-author)

## :scroll: Overview

This folder hosts a Deep Learning model that is deployed as an Amazon Web Services (AWS) Lambda function. The model uses the [Dutch House Prices Dataset](https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset) and predicts the house price from a set of house characteristics. 

More information about the model and data can be found [here](https://github.com/bryanlusse/HousePrices__NetworkTraining)

This repository is part of my House Price series in which we create a dataset, train a prediction model, and deploy the model and an accompanying web app.

Use the code as an example on how to deploy a PyTorch model through AWS.

## :closed_book: How to use

Clone the repository by running the following command in terminal:

```console
$ git clone https://github.com/bryanlusse/HousePrices__DeployedModel.git
```

Or just download the zip file at the top of the page.

The Docker image can be built on your local device. First change your working directory and then use the Serverless Application Model (SAM) from AWS in order to build the Docker image

```console
$ cd pytorch-house-price
$ sam build
```

Additionally, you can deploy the image to AWS using

```console
$ sam deploy --guided --stack-name <custom_stack_name>
```

while filling in a custom stack name.

For more information, I've made a blog detailing the whole deployment process (Post and link in progress)

## :exclamation: Requirements

General requirements:
- [Amazon AWS Account](https://aws.amazon.com/)
- [SAM CLI](https://aws.amazon.com/serverless/sam/)
- [Docker](https://docs.docker.com/get-docker/)

Model Requirements:
- Found in [requirements.txt](https://github.com/bryanlusse/HousePrices__DeployedModel/blob/master/requirements.txt).

## :open_file_folder: Folder Structure

```
.
├── assets                                   # Folder containing image for README
├── app                                      # App folder, containing the main code
├── events                                   
├── template.yaml                            # Standard template for AWS-PyTorch functions
└── README.md
```

## :smiley_cat: Author

- [@bryanlusse](https://github.com/bryanlusse)

Made with &nbsp;❤️&nbsp;