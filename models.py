from pydantic import BaseModel

class PodcastEpisode(BaseModel):
    title: str
    description: str
    host: str

class AlternativeRequest(BaseModel):
    target: str  # 'title' or 'description'
    prompt: str
