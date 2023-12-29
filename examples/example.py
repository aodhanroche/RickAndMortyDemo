from griptape.structures import Agent
from rick_and_morty_tool import RickMortyTool


agent = Agent(tools=[RickMortyTool()])

agent.run("Use the ReverseStringTool to reverse 'Griptape'")
