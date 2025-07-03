from langchain_openai import ChatOpenAI


class LLM:
    def get(model="gpt-4o"):
        return ChatOpenAI(model=model)

    def ask(prompt):
        llm = LLM.get()
        return llm.invoke(prompt).content
