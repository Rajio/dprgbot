from models import PodcastEpisode

episodes_db = {}
next_id = 1

def add_episode(episode_data: PodcastEpisode):
    global next_id
    episodes_db[next_id] = episode_data
    next_id += 1
    return next_id - 1

def get_all_episodes():
    return [{**episode.dict(), "id": eid} for eid, episode in episodes_db.items()]

def get_episode_by_id(episode_id: int):
    return episodes_db.get(episode_id)
