# LLM Base Prompt with RAG Context

## User Query:
{{user_query}}

---

## Context (Retrieved Chunks):

### 1. Relevant Context:
{{formatted_chunks}}

---

## Chain of Thought Steps:

1. **Understand the User’s Query**:
    - First, carefully analyze the user's question to identify the core topic. This could involve:
      - What specific information or process is the user asking about? (e.g., refunds, coverage, limitations, membership)
      - Does the user ask for a specific detail or condition regarding a service, benefit, or rule?

2. **Identify Relevant Information in Context**:
    - Based on the question, extract key pieces of information from the context:
      - Look for sections that directly address the user’s concern (e.g., refund policies, treatment coverage, exclusions).
      - If the query is about a specific benefit, treatment, or plan, identify which part of the context explains those details.

3. **Analyze the Information**:
    - Evaluate how the relevant details from the context answer the user’s query:
      - Are there conditions, exceptions, or limits attached to the information (e.g., partial refunds, coverage caps)?
      - What actions or requirements need to be met for the user to benefit from the discussed service or policy (e.g., membership status, timeframes)?

4. **Check for Ambiguities**:
    - Consider if there is any ambiguity in the context that might lead to a different interpretation of the query:
      - Are there conflicting statements or unclear details that need clarification?
      - Does the context provide an exhaustive answer, or should additional information be inferred or requested from the user?

5. **Formulate the Answer**:
    - Synthesize a clear and concise response that directly addresses the user’s query based on the relevant context:
      - Provide a comprehensive answer that considers all factors (e.g., conditions, exclusions, caps, etc.).
      - If necessary, break down complex information into simpler, understandable terms.

6. **Conclude with Clarity**:
    - Ensure the answer is direct and easy to follow, ensuring the user understands both the process and any limitations that may apply.
    - If appropriate, suggest any next steps or actions the user should take based on the context.

---

## Task:
Using the chain of thought and the provided context, generate a response to the user's query that is accurate, complete, and considers all relevant details. Ensure the response is clear and directly addresses the user’s needs based on the information available.
