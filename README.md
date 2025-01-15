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
1.	Load the pdf and parse it:
    a. Open PDF: Load the PDF and extract text and word-level metadata (e.g., position) from each page.
    b. Track Word Positions: Identify and map the position of the first word in each line.
    c. Extract the line metadata from each first word metadata
    e. Remove Header and Footer: Exclude text located in the header and footer regions based on vertical position.
    f. Format Text: Adjust punctuation, reverse misaligned words, and ensure proper formatting for English and Hebrew text.
    h. Clean and Return Text: After processing all pages, return the cleaned and formatted text, excluding headers/footers.

2.	Create rag 
    a.  split text into chunks
3.	Create function to ask questions (no need for UI)
4.	Function to Display question and answer
5.	Use chat gpt for questions and correct answers db for validation
6.	Verify correct answers from rag using bert similarity/embedding


Pgadmin with multiple collections schema , Pgadmin, elastic search, redis

Rabitmq, rest api for manual message, 
Container is service with 1 goal separation is by front end/backend
Question if this is used in multiple places
No reason to open multiple services which all for same usage
