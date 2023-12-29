import logging
from rick_and_morty_tool import RickMortyTool
from griptape.structures import Agent
from griptape.utils import Chat
from dotenv import load_dotenv


load_dotenv()

agent = Agent(tools=[RickMortyTool(off_prompt=False)], logger_level=logging.ERROR)

Chat(agent).start()
