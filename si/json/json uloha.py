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


def get_best_meme(memes: List[Meme]):  # filter: Callable[[Meme], bool])

    most_ups_meme = max(memes, key=lambda i: i['ups'])

    print("Highest rated meme from all subreddits: ")
    print(most_ups_meme["postLink"])

    return most_ups_meme["postLink"]
    pass


def get_best_meme_from_sub(memes: List[Meme], best_subred):
    memes_only_from_sub = []

    for meme in memes:
        if meme["subreddit"] == best_subred:
            memes_only_from_sub.append(meme)

    #print("Best subreddit: ")
    #print(memes_only_from_sub)

    print("Highest rated meme from the best sub: ")
    print(max(memes_only_from_sub, key=lambda i: i["ups"])["postLink"])

    return max(memes_only_from_sub, key=lambda i: i["ups"])["postLink"]
    pass


def get_subreddit_memes_ratings(memes: List[Meme],
                                subreddit: str) -> List[int]:
    pass


def get_all_subreddits(memes: List[Meme]) -> List[str]:
    list_of_subreds = []
    list_of_avg_ratings = []

    for meme in memes:
        if meme["subreddit"] in list_of_subreds:
            pass
        else:
            list_of_subreds.append(meme["subreddit"])

    #print("These are all the subreddits: ")
    #print(list_of_subreds)

    for subred in list_of_subreds:
        index = 0
        sum = 0
        for meme in memes:
            if meme["subreddit"] == subred:
                sum += meme["ups"]
                index += 1

        list_of_avg_ratings.append({"subreddit": subred,
                                    "average": (sum/index)})

    print(max(list_of_avg_ratings, key=lambda i: i["average"]))

    return max(list_of_avg_ratings, key=lambda i: i["average"])
    pass


def load_memes(fileName: str) -> List[Meme]:
    list_of_all_memes = []
    with open(fileName) as file:
        obj = json.load(file)
        #print(obj)

        # print(obj["memes"])
        list_of_all_memes = obj["memes"]

        #print("List")
        #print(list_of_all_memes)

        return(list_of_all_memes)

    pass


def analyze_memes(fileName: str) -> Tuple[str, str, str]:

    to_be_returned = (get_all_subreddits(load_memes(fileName))["subreddit"],
                      get_best_meme(load_memes(fileName)),
                      get_best_meme_from_sub(load_memes(fileName),
                                             get_all_subreddits(
                                                 load_memes(
                                                     fileName))["subreddit"]))

    return (to_be_returned)


#get_all_subreddits(load_memes("si//json//memese.json"))

#get_best_meme(load_memes("si//json//memese.json"))

#get_best_meme_from_sub(load_memes("si//json//memese.json"),
                       #get_all_subreddits(
                           #load_memes("si//json//memese.json"))["subreddit"])
                  
analyze_memes("si//json//memese.json")
