from discord.ui import (
    Button,
    Select,
    View,
    Item
)

from discord import (
    Emoji,
    PartialEmoji,
    ButtonStyle,
    ComponentType,
    ChannelType,
    SelectOption,
)

def is_button(dict:dict) -> bool:
    return dict["type"] == "button"

def is_select(dict:dict) -> bool:
    return dict["type"] == "select"

class Button(Button):
    def __init__(self, *, style: ButtonStyle = ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | Emoji | PartialEmoji | None = None, row: int | None = None):
        super().__init__(
            style=style, 
            label=label, 
            disabled=disabled, 
            custom_id=custom_id, 
            url=url, 
            emoji=emoji, 
            row=row
        )

    @classmethod
    def from_dict(self, dict:dict):
        self = self.__new__(self)

        stlye = {
            "success": ButtonStyle.success,
            "danger": ButtonStyle.danger,
            "link": ButtonStyle.link,
            "primary": ButtonStyle.primary,
            "grey": ButtonStyle.secondary,
        }

        self.__init__(
            row=dict.get("row"),
            style=stlye[dict.get("style","secondary")],
            label=dict.get("label"),
            emoji=dict.get("emoji"),
            custom_id=dict.get("custom_id")
        )

        return self

class Select(Select):
    def __init__(self, select_type: ComponentType = ComponentType.string_select, *, custom_id: str | None = None, placeholder: str | None = None, min_values: int = 1, max_values: int = 1, options: list[SelectOption] = None, channel_types: list[ChannelType] = None, disabled: bool = False, row: int | None = None) -> None:
        super().__init__(
            select_type=select_type, 
            custom_id=custom_id, 
            placeholder=placeholder, 
            min_values=min_values, 
            max_values=max_values, 
            options=options, 
            channel_types=channel_types, 
            disabled=disabled, 
            row=row
        )

    @classmethod
    def from_dict(self, dict:dict):

        select_define = {
            "string":ComponentType.string_select,
            "channel":ComponentType.channel_select,
            "mentionable":ComponentType.mentionable_select,
            "role":ComponentType.role_select,
            "user":ComponentType.user_select
        }

        self = self.__new__(self)

        self.__init__(
            select_type = select_define[dict.get("type")],
            custom_id = dict.get("custom_id"),
            placeholder = dict.get("placeholder"),
            min_values=dict.get("min_values", 0),
            max_values=dict.get("max_values", 1),
            options = [
                SelectOption(
                    label=option["label"], 
                    value=option["value"], 
                    emoji=option["emoji"]
                ) 
                for option in dict.get("options", [])
            ]
        )

        return self

class View(View):
    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)

    @classmethod
    def from_dict(self, data: dict):
        self = self.__new__(self)
        self.__init__(
            *(Button.from_dict(d) for d in data.get("buttons", [])),
            *(Select.from_dict(d) for d in data.get("selects", [])),
            timeout=data.get("timeout")
        )

        return self

if __name__ == "__main__":
    ... #test