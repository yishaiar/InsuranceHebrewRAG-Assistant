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
- [ ] TODO 1
- [ ] TODO 2
- [ ] TODO 3


question examples:
שאלה: ממתי ניתן לקבל החזר על הטיפול באקופונקטורה  
שאלה: האם מקבלים החזר מלא על הטיפולים   
שאלה: כמה טיפולים מכוסים  



Describe an architectural concept, assuming that the process is carried out in a GCP or AWS environment, and the content of the system is:  
1.	Receiving multiple types of documents in DOC / DOCX / PDF / TXT / Json / JPEG / PNG / JIF format 
2.	Building 2 interfaces (Request \ Response)   
3.	Construction and updating of a generic schema  
4.	Receiving the required information from the screens for analysis (in JSON format) 
5.	Validation that the received information is in the desired structure   
6.	Free text analysis and structured information of the documents (the core capability of the AI model) 
7.	Building a uniform summary structure and creating an automatic summary of the findings of the information analysis
8.	Externalizing a service that receives the information required for analysis (in JSON format) and returns an answer object that includes the text of the summary and synchronously running the service (returning the error including an error code)

architecture
1.	Load the pdf and parse it
2.	Create rag
3.	Create function to ask questions (no need for UI)
4.	Function to Display question and answer
5.	Use chat gpt for questions and correct answers db for validation
6.	Verify correct answers from rag using bert similarity/embedding
