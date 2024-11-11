from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.retriever import retriever
from src.llm import llm
from src.templates import template

prompt = ChatPromptTemplate.from_template(template=template)
parser = StrOutputParser()

chain = { "context": retriever, "question": RunnablePassthrough()} | prompt | llm | parser
