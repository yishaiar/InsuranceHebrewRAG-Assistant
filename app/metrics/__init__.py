from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

def bertSimilarity(sentence1,sentences2):
    # BERT Similarity = Semantic Similarity using BERT embeddings (model such as RoBERTa)
    #Load the multilingual XLM-RoBERTa model and tokenizer
    model_name = "xlm-roberta-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Encode sentences in Hebrew
    inputs = tokenizer([sentence1,sentences2], return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)

    # Compute cosine similarity
    similarity = cosine_similarity(embeddings)
    return similarity[0][1]#return similarity between sentence1 and sentence2 not the full matrix
