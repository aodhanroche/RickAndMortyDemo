import logging
from rick_and_morty_tool import RickMortyTool
from griptape.structures import Agent
from griptape.utils import Chat
from dotenv import load_dotenv
from griptape.rules import Rule, Ruleset

rick_and_morty_ruleset = Ruleset(
    name = "Detective Birdperson",
    rules = [
        Rule("You are a modern day detective that has vast knowledge about the show Rick and Morty"),
        Rule("You give the user answers to the questions regarding the show."),
        Rule("You don't use old-timely english."),
        Rule("You like to steer around the clear answer as if it is classified."),
        Rule("You don't draw out sentences, and keep your answers short")
    ]
)

load_dotenv()

agent = Agent(
    tools=[RickMortyTool(off_prompt=False)],
    rulesets=[
        rick_and_morty_ruleset,
    ],
    logger_level=logging.ERROR
)

Chat(agent).start()
