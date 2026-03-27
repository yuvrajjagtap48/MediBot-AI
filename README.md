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
    - conda activate medibot


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


# Cleanup duplicate download cache (Windows)
- If disk usage grows, clear pip cache:
    - Remove-Item "$env:LOCALAPPDATA\pip\Cache\*" -Recurse -Force