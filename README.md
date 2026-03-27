# process 
 - PDF(medical book) => Extract Docs of the book => Chunking => Embedding Model(hugging face) =>  Vector Embedding  =>  Pincone Vector DB(knowledge base) => it return some rank result 
 
 LLM(GPT Model)  <===>  it return actual result


# TechStack
 - Python

 - OpenAI GPT

 - LangChain

 - PineCone

 - Flask

 - AWS(CI/CD)


# Create virtual env
- conda create-n medibot python=3.10 -y

- Active this env

    - conda create -n medibot python=3.10 -y

    - conda activate medibot

- Install required files  =>   pip install -r requirements.txt


# AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.

2. Create IAM user for deployment
    #with specific access

        1. EC2 access : It is virtual machine

        2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

        1. Build docker image of the source code

        2. Push your docker image to ECR

        3. Launch Your EC2 

        4. Pull Your image from ECR in EC2

        5. Lauch your docker image in EC2

    #Select Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess
    
3. Create ECR repo to store/save docker image

4. Create EC2 machine (Ubuntu)


5. Open EC2 and Install docker in EC2 Machine:
    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one



7. Setup github secrets:(in github secrets and variables)

    - AWS_ACCESS_KEY_ID

    - AWS_SECRET_ACCESS_KEY

    - AWS_DEFAULT_REGION

    - ECR_REPO

    - PINECONE_API_KEY

    - OPENAI_API_KEY











# Install dependencies once (recommended)
- Use only one method to install dependencies.
- Preferred command:
    - pip install --no-cache-dir -r requirements.txt
- Avoid running both of these in the same environment:
    - pip install -r requirements.txt
    - pip install -e .


# Embeddings mode
- This project uses OpenAI embeddings (text-embedding-3-small).
- This avoids downloading large local ML packages (torch/transformers) and keeps environment size small.


