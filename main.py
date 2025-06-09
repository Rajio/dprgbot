from fastapi import FastAPI, HTTPException
from models import PodcastEpisode, AlternativeRequest
from database import add_episode, get_all_episodes, get_episode_by_id
from llm_client import generate_alternative
from webhook_handler import handle_webhook
from rss_reader import fetch_rss

app = FastAPI()

# Level 1 — CRUD
@app.post("/episodes")
def create_episode(episode: PodcastEpisode):
    episode_id = add_episode(episode)
    return {"id": episode_id, **episode.dict()}

@app.get("/episodes")
def read_episodes():
    return get_all_episodes()

# Level 2 — LLM alternative generation
@app.post("/episodes/{episode_id}/generate_alternative")
async def generate_episode_alternative(episode_id: int, alt_request: AlternativeRequest):
    episode = get_episode_by_id(episode_id)
    if not episode:
        raise HTTPException(status_code=404, detail="Episode not found.")

    if alt_request.target not in ["title", "description"]:
        raise HTTPException(status_code=400, detail="Target must be 'title' or 'description'.")

    field_value = getattr(episode, alt_request.target)
    try:
        alternative = await generate_alternative(field_value, alt_request.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "original_episode": episode.dict(),
        "target": alt_request.target,
        "prompt": alt_request.prompt,
        "generated_alternative": alternative
    }

# Level 4 — Webhook
@app.post("/webhook/event")
def webhook_event(episode: PodcastEpisode):
    episode_id = handle_webhook(episode.dict())
    return {"status": "episode added", "id": episode_id}

# Level 5 — RSS Feed Integration
@app.get("/rss")
def get_rss(feed_url: str = "https://feeds.npr.org/510289/podcast.xml"):
    return fetch_rss(feed_url)
