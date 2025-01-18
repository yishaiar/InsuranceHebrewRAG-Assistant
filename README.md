# InsuranceHebrewRAG-Assistant
[Python tool leveraging Retrieval-Augmented Generation (RAG) to analyze Hebrew insurance PDF documents and provide accurate responses to client inquiries]

```python
# some python code for reference..
project run from  main.ipynb



## 💻 Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
    ```shell
    pip install -r requirements.txt
    ```

## 📋 TODOs
- Install ollama on machine (required to load the llm model)


question examples:
שאלה: ממתי ניתן לקבל החזר על הטיפול באקופונקטורה  
שאלה: האם מקבלים החזר מלא על הטיפולים   
שאלה: כמה טיפולים מכוסים  

# Solution Overview

This solution demonstrates how to process a Hebrew PDF, extract and clean its content, perform text retrieval using a RAG (Retrieval Augmented Generation) approach, and finally query a Hebrew LLM (Language Model) to answer a user query. Additionally, the solution evaluates the model using various metrics.

## 1. Load the PDF and Parse It
- **Open PDF:** Load the PDF and extract text along with word-level metadata (e.g., position) from each page.
- **Track Word Positions:** Identify and map the position of the first word in each line.
- **Extract Line Metadata:** Extract metadata from each first word, which represents the start of each line.
- **Remove Header and Footer:** Exclude text located in the header and footer regions based on vertical position.
- **Format Text:** Adjust punctuation, reverse misaligned words, and ensure proper formatting for both English and Hebrew text.
- **Clean and Return Text:** After processing all pages, return the cleaned and formatted text, excluding headers and footers.

## 2. Create RAG (Retrieval Augmented Generation)
- **Split Text Into Chunks:** Use `RecursiveCharacterTextSplitter` from LangChain to split the text into manageable chunks.
- **Create RAG:** Build the RAG (in-memory) using FAISS, since the document is short.
- **Hebrew Embedding Model:** Use the `sentence-transformers-alephbert` model (a Hebrew model) for embedding generation.
- **Normalize Embeddings:** Normalize the embeddings to a range of 0-1 to threshold irrelevant chunks (threshold = 0.2).
- **Chunk Selection:** Retrieve only the top `k=5` most relevant chunks with similarity scores higher than the threshold.

## 3. Query the LLM Model
- **Create an LLM Prompt:** Create a prompt based on the user query and the retrieved chunks from RAG.
- **Context Insertion:** Insert the context into the prompt template, following the Chain of Thought guidelines.
- **LLM Model Used:** The model used is `dictalm2.0-instruct:f16`, which is the best small Hebrew LLM from the Hebrew leaderboard. (Note: My PC is without GPU, so this was the optimal choice for Hebrew text processing).
- **API Usage:** The LLM is queried using the OLLAMA API.

## 4. Metrics - BERT Similarity
- **Hebrew BERT Model:** Use the `xlm-roberta-base` model for BERT-based calculations.
- **Metric Calculation:** Using the `transformers` and `bert_score` libraries, the following metrics are calculated:
  - **Precision**
  - **Recall**
  - **F1**
  - **Similarity**
- **Validation Dataset:**
  - Created a validation dataset with reference answers (both correct and incorrect).
  - **Testing Approach 1:** Evaluate the similarity between the LLM response and the user query (using Recall, F1, and Similarity).
  - **Testing Approach 2:** Compare the LLM response with predefined correct and incorrect answers from the validation dataset (using Precision, F1, and Similarity).

## 5. Comparison of Results
- **Metrics Comparison:** The evaluation was based on a comparison between the predicted LLM responses and the correct or incorrect reference answers, assessing Precision, Recall, F1, and Similarity values.