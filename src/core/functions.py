import discord
import json
import os

import time

from datetime import (
    datetime,
    timezone, 
    timedelta
)

from typing import(
    Any
)

def load_extension(bot:  discord.Bot, folder:str, mode: str = "load", is_notice: bool = True) -> None:

    loading_method = {
        "load":bot.load_extension,
        "reload":bot.reload_extension,
        "unload":bot.unload_extension
    }

    if is_notice:
        print(f"Start {mode}ing {folder}")

    for Filename in os.listdir(f'src/{folder}'):
        if Filename.endswith(".py"):
            loading_method[mode](f"{folder}.{Filename[:-3]}")
            if is_notice:
                print(f'-- {mode}ed "{Filename}"')

    print(f"{mode}ing {folder} end")

    return None

def merge_dict(*dicts: dict) -> dict:
    raw = {}

    for d in dicts:
        raw.update(d)

    return raw

def read_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        try:
            data = json.loads(file.read())
        except Exception as ex:
            print(ex)
            data = None
        return data

def write_json(path: str, key: str, *value: dict, keeping: bool = True):
    new = original = read_json(path) if keeping else {}
    new[key] = merge_dict(original.get(key,{}),*value)

    with open(path, "w", encoding="utf-8") as file:
        return file.write(json.dumps(
            new,
            indent=4,
            separators=(",", ": "),
            ensure_ascii=False
        ))

def get_time(time: datetime = None, hours = 8):
    ori = datetime.now(timezone(timedelta(hours=hours))) if not time else time
    return datetime(ori.year, ori.month, ori.day, ori.hour, ori.minute, ori.second)

def get_time_map(time = None, hours = 8):
    ori = datetime.now(timezone(timedelta(hours=hours))) if not time else time
    return {
        "year": ori.year, 
        "month" : ori.month, 
        "day" : ori.day, 
        "hour" : ori.hour, 
        "minute" : ori.minute, 
        "second" : ori.second
    }

def rep_str(string: str,**kwargs):
    return [(string := string.replace("{%s}" % k, str(v))) for k, v in kwargs.items()][len(kwargs)-1]

def creat_unix(dt: datetime):
    return int(time.mktime(dt.timetuple()))

if __name__ == "__main__":
    str1 = "hello {name} {age}"
    print(rep_str(str1, name="Youtong", age=18))
