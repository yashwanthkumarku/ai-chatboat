from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template=ChatPromptTemplate.from_messages([("system","you are {game} comidian explain in 20 words "),
                                                  ("user","{question}")])
llm=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

chain=prompt_template|llm|parser

game=input("enter game name :")
while True:
    question=input("question :")
    if question.lower=="exit":
        break

    response=chain.invoke({"game":game,"question":question})
    print(response,"\n if you want to stop conversation type 'exit' ")