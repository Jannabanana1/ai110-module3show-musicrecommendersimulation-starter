from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and returns a list of dictionaries.
    """
    songs = []

    # Open the CSV file in read mode
    with open(csv_path, "r", newline="", encoding="utf-8") as file:

        # Read each row as a dictionary using column names as keys
        reader = csv.DictReader(file)

        # Loop through each row in the CSV file
        for row in reader:

            # Add the song dictionary to the songs list
            songs.append(row)

    # Return the list of song dictionaries
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a song against user preferences.
    Returns a total score and a list of reasons.
    """

    # Start with a score of 0 and an empty list of reasons
    score = 0.0
    reasons = []

    # 1. Check if the song's genre matches the user's favorite genre
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # 2. Check if the song's mood matches the user's favorite mood
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # 3. Calculate energy similarity (maximum 1.5 points)
    song_energy = float(song["energy"])
    target_energy = float(user_prefs["target_energy"])

    energy_similarity = 1 - abs(song_energy - target_energy)
    energy_points = energy_similarity * 1.5

    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # 4. Calculate tempo similarity (maximum 0.5 points)
    song_tempo = float(song["tempo_bpm"])
    target_tempo = float(user_prefs["target_tempo_bpm"])

    tempo_similarity = max(0, 1 - abs(song_tempo - target_tempo) / 200)
    tempo_points = tempo_similarity * 0.5

    score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    # 5. Calculate valence similarity (maximum 0.5 points)
    song_valence = float(song["valence"])
    target_valence = float(user_prefs["target_valence"])

    valence_similarity = 1 - abs(song_valence - target_valence)
    valence_points = valence_similarity * 0.5

    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    # 6. Calculate danceability similarity (maximum 0.5 points)
    song_danceability = float(song["danceability"])
    target_danceability = float(user_prefs["target_danceability"])

    danceability_similarity = 1 - abs(song_danceability - target_danceability)
    danceability_points = danceability_similarity * 0.5

    score += danceability_points
    reasons.append(f"danceability similarity (+{danceability_points:.2f})")

    # 7. Calculate acousticness similarity (maximum 0.5 points)
    song_acousticness = float(song["acousticness"])
    target_acousticness = float(user_prefs["target_acousticness"])

    acousticness_similarity = 1 - abs(song_acousticness - target_acousticness)
    acousticness_points = acousticness_similarity * 0.5

    score += acousticness_points
    reasons.append(f"acousticness similarity (+{acousticness_points:.2f})")

    # Return the total score and explanations
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
