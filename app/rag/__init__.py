import faiss
import numpy as np



def create_RAG(chunks, embeding_model):
    # Step 1: Embed the chunks using SentenceTransformer
    chunk_embeddings = embeding_model.encode(chunks)
    


    # Step 2: Create a FAISS index for fast retrieval - use the Cosine distance metric for similarity search (values normalized 0-1)
    
    # Normalize the query embedding vector
    norm = np.linalg.norm(chunk_embeddings, axis=1, keepdims=True)
    chunk_embeddings = chunk_embeddings / norm  # Normalize to unit vectors
    #create the rag index
    dimension = chunk_embeddings.shape[1]  # Dimensionality of the embedding
    rag_index = faiss.IndexFlatIP(dimension)  # Use Inner Product for cosine similarity

    # Step 3: Add the embeddings to a rag index
    rag_index.add(np.array(chunk_embeddings))
    # print(chunk_embeddings[0])
    return rag_index

def retrieve_relevant_indexes(query,embedding_model,rag_index, k=3):
    '''
    retrieve the index of most relevent rag embeddings (most similar)
    '''
    query_embedding = embedding_model.encode([query])  # Get the embedding for the query
    
    # Normalize the query embedding
    query_norm = np.linalg.norm(query_embedding, axis=1, keepdims=True)
    query_embedding = query_embedding / query_norm
    
    similarities, indices = rag_index.search(np.array(query_embedding), k)  # Perform the search
    return similarities[0], indices[0]


def retrieve_relevant_chunks(chunks,similarities, indices,thresh=0.2):
    '''
    Retrieve the most relevant chunks based on the query
    distances: The distances of the retrieved chunks - ranges from 0 to 1
    thresh: The threshold for the similarity score - default is 0.2
    '''
    relevant_chunks = [chunks[i] for j,i in enumerate(indices) if similarities[j]>thresh ] # Retrieve the corresponding text chunks if the similarity is more than 0.5
    return relevant_chunks

def retrieve_context(query, chunks, embedding_model, rag_index, print_rag_results=True, k_chunks=10):
    # call the retrieval system (FAISS, can be replaced with any other retrieval system)
    similarities, indices = retrieve_relevant_indexes(query,embedding_model,rag_index, k=k_chunks)
    relevant_chunks  = retrieve_relevant_chunks(chunks,similarities, indices)
    if print_rag_results:
        print(f"Query: {query}\n")
        print("Relevant Chunks from RAG:\n")
        for chunk in relevant_chunks:
            print(chunk)
            print('-'*50)
    return relevant_chunks