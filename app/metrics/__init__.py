from transformers import AutoTokenizer, AutoModel
# from transformers import BertTokenizer, BertModel
from bert_score import BERTScorer

import torch
import numpy as np



def bertEmbedding(text, tokenizer, model):
    # Prepare the text for BERT
    # Feed the texts to the BERT model and obtain the representation vectors
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        embeddings = model(**inputs).last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings



def bertSimilarity(candidate, reference, tokenizer, model,scorer):
    # Get the embeddings for the candidate and reference texts
    embeddings1 = bertEmbedding(candidate, tokenizer, model)
    embeddings2 = bertEmbedding(reference, tokenizer, model)

    # Calculate cosine similarity
    Similarity = np.dot(embeddings1, embeddings2.T) / (np.linalg.norm(embeddings1) * np.linalg.norm(embeddings2))
    
    # calculate bertscores
    P, R, F1 = scorer.score([candidate], [reference])

    return P.mean(), R.mean(), F1.mean(), Similarity[0][0]

def loadBertModel(bert_model_name):
    #1. Load the pre-trained BERT model and tokenizer - used for calculating embeddings and similarity
    
    # a. Load the pre-trained BERT model and tokenizer - used for english
    # tokenizer = BertTokenizer.from_pretrained(bert_model_name)
    # model = BertModel.from_pretrained(bert_model_name)

    # b. in hebrew needs AutoTokenizer and AutoModel
    tokenizer = AutoTokenizer.from_pretrained(bert_model_name)
    model = AutoModel.from_pretrained(bert_model_name)
    
    # 2. load bertscorer used for calculating bert scores
    scorer = BERTScorer(model_type=bert_model_name)
    return tokenizer, model, scorer

# from transformers import AutoTokenizer, AutoModel
# import torch
# from sklearn.metrics.pairwise import cosine_similarity
# import os



# def bertSimilarity(sentence1,sentences2,bert_model_name):
#     # BERT Similarity = Semantic Similarity using BERT embeddings (model such as RoBERTa)
#     #Load the multilingual XLM-RoBERTa model and tokenizer
#     tokenizer = AutoTokenizer.from_pretrained(bert_model_name)
#     model = AutoModel.from_pretrained(bert_model_name)

#     # Encode sentences in Hebrew
#     inputs = tokenizer([sentence1,sentences2], return_tensors="pt", padding=True, truncation=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         embeddings = outputs.last_hidden_state.mean(dim=1)

#     # Compute cosine similarity
#     similarity = cosine_similarity(embeddings)
#     return similarity[0][1]#return similarity between sentence1 and sentence2 not the full matrix


def evaluateTask(precision, recall, f1, similarity,task_type=1):
    '''
    task_type: 1 for Similarity between LLM response and user query: all metrics except precision are relevant
    task_type: 2 for Comparison between LLM response and predefined expected response: all metrics except recall are relevant
    output ranges:
    1. (Cosine) Similarity (0 to 1); 1 - the two texts are identical ,0 - there is no similarity in meaning
    2. (bertScore) Precision (0 to 1); 1 - all tokens in candidate are in reference tokens, 0 - no token in candidate are in reference tokens
    3. (bertScore) Recall (0 to 1); 1 - all tokens in reference are in candidate tokens, 0 - no token in reference are in candidate tokens
    4. (bertScore) F1 (0 to 1); 1 - all tokens in candidate are in reference tokens and all tokens in reference are in candidate tokens, 
                                0 - no token in candidate are in reference tokens and no token in reference are in candidate tokens
    '''
    
    if task_type == 1:#Similarity between LLM response and user query
        print('Similarity between LLM response and user query')
        print(f"BERTScore (Precision: {precision:.4f}), Recall: {recall:.4f}, F1: {f1:.4f}, Similarity: {similarity:.4f}")
    if task_type == 2:#Comparison between LLM response and predefined expected response
        print('Comparison between LLM response and predefined expected response')
        print(f"BERTScore Precision: {precision:.4f}, (Recall: {recall:.4f}), F1: {f1:.4f}, Similarity: {similarity:.4f}")