from __future__ import annotations
from griptape.artifacts import TextArtifact, ErrorArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity
from schema import Schema, Literal
from attr import define

@define
class RickMortyTool(BaseTool):

    @activity(
        config={
            "description": "Can be used to get information about a character.",
            "schema": Schema({
                Literal("character", description="The name of the character"): str
            })
        }
    )
    def get_character(self, params: dict) -> TextArtifact | ErrorArtifact:
        import ramapi

        character = params["values"].get("character")

        try:
            return TextArtifact(ramapi.Character.filter(name=f'{character}'))

        except Exception as e:
            return ErrorArtifact(str(e))

    @activity(
        config={
            "description": "Can be used to get information about an episode by its number.",
            "schema": Schema({
                Literal("episode number", description="The number of the episode"): int
            })
        }
    )
    def get_episode_by_number(self, params: dict) -> TextArtifact | ErrorArtifact:
        import ramapi

        episode = params["values"].get("episode number")

        try:
            return TextArtifact(ramapi.Episode.get(episode))

        except Exception as e:
            return ErrorArtifact(str(e))

    @activity(
        config={
            "description": "Can be used to get all of the name of a character based on their id",
            "schema": Schema({
                Literal("character id", description="The id of a character"): int
            })
        }
    )
    def get_character_by_id(self, params: dict) -> TextArtifact | ErrorArtifact:
        import ramapi

        character_id = params["values"].get("character id")

        try:
            return TextArtifact(ramapi.Character.filter(id=f"{character_id}"))

        except Exception as e:
            return ErrorArtifact(str(e))

    @activity(
        config={
            "description": "Can be used to sort characters by species",
            "schema": Schema({
                Literal("species", description="The species of the character"): int
            })
        }
    )
    def check_character_species(self, params: dict) -> TextArtifact | ErrorArtifact:
        import ramapi

        species = params["values"].get("species")

        try:
            return TextArtifact(ramapi.Character.filter(species=f"{species}"))

        except Exception as e:
            return ErrorArtifact(str(e))
