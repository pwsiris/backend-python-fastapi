import random
from datetime import datetime
from typing import List

import httpx
from fastapi import APIRouter, Query, Response
from utils.config import cfg
from utils.in_memory_data import in_memory_data

router = APIRouter()


@router.get("/timecode")
async def timecode(title: str, uptime: str, user_name: str):
    async with httpx.AsyncClient() as ac:
        json = {
            "embeds": [
                {
                    "title": title,
                    "fields": [
                        {"name": "Timecode", "value": uptime, "inline": True},
                        {"name": "Sender", "value": user_name, "inline": True},
                    ],
                }
            ]
        }
        answer = await ac.post(cfg.DISCORD_HOOK_URL, json=json)
    message = "Timecode saved to discord"
    if answer.status_code < 200 or answer.status_code >= 300:
        print(answer.status_code)
        print(answer.content)
        message = (
            f"Failed to send stream timecode to discord (code {answer.status_code})"
        )
    return Response(content=message, media_type="text/html")


@router.get("/save_please")
async def save_please():
    return Response(
        content=random.choice(in_memory_data.SAVE_CHOICES), media_type="text/html"
    )


@router.get("/bite")
async def bite_someone(sender: str, targets: List[str] = Query()):
    random.seed(datetime.now().timestamp())
    action = random.choice(in_memory_data.BITE["actions"])
    place = random.choice(in_memory_data.BITE["places"])
    body_part = random.choice(in_memory_data.BITE["body_parts"])

    target = "Iris_ti"
    for variant in targets:
        if variant.lower().rstrip().lstrip() not in in_memory_data.BITE["bots"]:
            target = variant
            break

    if in_memory_data.BITE["cheats"] and sender == "mirakzen":
        target = "Iris_ti"

    message = f"Однажды тёмной ночью {sender} {action} в {place} к {target} и кусьнул за {body_part}"
    if in_memory_data.BITE["cheats"] and target == "mirakzen":
        message = f"Однажды тёмной ночью {sender} {action} в {place} к {target} и получил леща"

    return Response(content=message, media_type="text/html")
