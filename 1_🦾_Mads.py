from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import OpenAI, LLMChain
from langchain import OpenAI, LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, load_tools
from langchain.chat_models import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
from langchain import LLMMathChain
import streamlit as st
from stream_lit_config import styles,animate_intro
from langchain_community.utilities import OpenWeatherMapAPIWrapper

openai_api_key = os.getenv("OPENAI_API_KEY")
serpapi_api_key = os.getenv("SERPAPI_API_KEY")
weather_map_api_key = os.getenv("OPENWEATHERMAP_API_KEY")


def main():
    #title and p tag
    h1_text = "Mads the personal AI desktop assistant"
    p_text = "Hello, welcome to this cool new desktop AI, using OpenAI, langchain, and a bunch of neat tools I am able to do a lot of cool functions, I can create appointments for you, play music, move files on your local machine, tell you the weather, complete basic math problems, and soon I will use text-to-speech to complete your requests"
    
    styles()
    animate_intro(h1_text, p_text)
    
    load_dotenv()
   

    llm = ChatOpenAI(temperature=0.8)
    search = DuckDuckGoSearchRun()
    calculator = LLMMathChain.from_llm(llm=llm, verbose=True)
    weather = OpenWeatherMapAPIWrapper()

    #current tools mads is using.
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Useful for when you need to answer questions about current events. "
                        "You should ask targeted questions."
        ),
        Tool(
            name="Calculator",
            func=calculator.run,
            description="Useful when you need to do math operations or arithmetic."
        ),
        Tool(
            name="Weather",
            func=weather.run,
            description="You can get the weather based off of my searches."
        )
    ]

    prefix = """Your name is Mads and you are a desktop AI agent. You can do many things such as create files, play music, check the weather and so on.
    If you cannot complete an action based on the questions I give you, then tell me so in a nice and respectful manner explaining why you cannot complete the request at this moment in time."""
    suffix = """Begin!"

    {chat_history}
    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools,
        prefix=prefix,
        suffix=suffix,
        input_variables=["input", "chat_history", "agent_scratchpad"],
    )
    memory = ConversationBufferMemory(memory_key="chat_history")

    # Generate a unique key for the text input widget
    question_key = "question"
    response_key = 'response_output'

    question = st.text_input("Ask a question:", key=question_key)

    llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory, handle_parsing_errors=True)

    if question:
        response = (agent_chain.run(input=question))
        st.write("Thinking...")
        print(question)
        print(response)
        st.write(response, key=response_key)

if __name__ == "__main__":
    main()
