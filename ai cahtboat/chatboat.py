from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template=ChatPromptTemplate.from_messages([("system","you are {ai} talk with people within two sentences "),
                                                  ("user","{question}")])
llm=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

chain=prompt_template|llm|parser

ai=input("enter ai role :")
while True:
    question=input("question :")
    if question.lower=="exit":
        break

    response=chain.invoke({"ai":ai,"question":question})
    print(response,"\n if you want to stop conversation type 'exit' or continue to ask question")