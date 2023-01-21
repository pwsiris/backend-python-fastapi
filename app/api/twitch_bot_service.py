from fastapi import APIRouter
from schemas import twitch_bot_service
from utils.in_memory_data import get_categoty_list_object, in_memory_data

from . import HTTPanswer

router = APIRouter()


@router.put("/cheats")
async def cheating(cheats: twitch_bot_service.Cheats):
    in_memory_data.BITE.cheats = cheats.enable
    return HTTPanswer(200, "OK")


@router.get("/{category}")
async def get_all_items(category: str):
    list_object = get_categoty_list_object(category, in_memory_data)
    count, data = list_object.get_all_items()
    return HTTPanswer(200, {"count": count, "data": data})


@router.post("/{category}")
async def add_new_item(category: str, input: twitch_bot_service.NewItem):
    return HTTPanswer(
        201, get_categoty_list_object(category, in_memory_data).add_item(input.string)
    )


@router.put("/{category}")
async def update_item(category: str, input: twitch_bot_service.UpdateItem):
    get_categoty_list_object(category, in_memory_data).update_item(
        input.id, input.string
    )
    return HTTPanswer(200, "OK")


@router.delete("/{category}")
async def delete_item(category: str, input: twitch_bot_service.DeleteItem):
    get_categoty_list_object(category, in_memory_data).remove_item(input.id)
    return HTTPanswer(200, "OK")
