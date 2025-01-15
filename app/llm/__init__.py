
from ollama import chat,generate,pull
import os



def format_chunks(chunks):
    formatted_context = "\n".join([f"{i+1}. {chunk.strip()}" for i, chunk in enumerate(chunks)])
    return formatted_context

# Function to load the markdown template and replace placeholders with actual data
def load_and_format_prompt(user_query, retrieved_chunks,template_path = 'app/llm/prompt_template.md'):
    # format the retrieved chunks
    formatted_chunks = format_chunks(retrieved_chunks)
        
    # Load the markdown template
    with open(template_path, 'r') as file:
        prompt_template = file.read()

    # Replace placeholders with actual data
    formatted_prompt = prompt_template.replace("{{user_query}}", user_query).replace("{{formatted_chunks}}", formatted_chunks)
    
    return formatted_prompt



def prompt_llm(llm_model_name,prompt):
  pull(llm_model_name)# download the model if not exists

  stream = chat(
      model=llm_model_name,
      messages=[{'role': 'user', 'content': prompt}],
      stream=True,
  )
  full_text = ''
  for chunk in stream:
    chunk_text = chunk['message']['content']
    full_text += chunk_text
    # print(chunk_text, end='', flush=True)
  return full_text

def print_prompt_and_response(user_query, llm_response):
    """
    This function prints out the user's input prompt and the final LLM response.
    
    Parameters:
    - user_query (str): The user's input free text query.
    - llm_response (str): The final response generated by the LLM.
    """
    
    print("===== User Input Query =====")
    print(user_query)
    print("\n===== Final LLM Response =====")
    print(llm_response)