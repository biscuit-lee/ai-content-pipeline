from pydantic import BaseModel


class StoryRequest(BaseModel):
    prompt: str
    storyType: str

class AudioRequest(BaseModel):
    story: dict
    ttsProvider: str

class RegenerateRequest(BaseModel):
    existingScript:str
    userCritique: str

class VideoRequest(BaseModel):
    downloadUrl:str