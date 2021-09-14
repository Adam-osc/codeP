from typing import Tuple, List, Callable, Dict, NamedTuple
import json

class Meme(NamedTuple):
    postLink: str
    subreddit: str
    title: str
    url: str
    nsfw: bool
    spoiler: bool
    author: str
    ups: int
    preview: List[str]

class Memes(NamedTuple):
    count: int
    memes: List[Meme]

def get_best_meme(memes: List[Meme], filter: Callable[[Meme], bool]) -> Meme:
    pass

def get_subreddit_memes_ratings(memes: List[Meme], subreddit: str) -> List[int]:
    pass

def get_all_subreddits(memes: List[Meme]) -> List[str]:
    pass

def load_memes(fileName: str) -> List[Meme]:
    List = []
    with open(fileName) as file:
        obj = json.load(file)
        print(obj)

        #print(obj["memes"])
        List = obj["memes"]

        print("List")
        print(List)

        return(List)

    pass

def analyze_memes(fileName: str) -> Tuple[str, str, str]:
    return ("", "", "")

load_memes("//root/codeP//si//Json/memese.json")