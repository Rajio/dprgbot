from database import add_episode
from models import PodcastEpisode

def handle_webhook(payload: dict):
    episode = PodcastEpisode(**payload)
    episode_id = add_episode(episode)
    return episode_id
