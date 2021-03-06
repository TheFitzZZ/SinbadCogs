from typing import Any, List

import discord

from .context import Context

class Converter:
    async def convert(self, ctx: Context, argument: str) -> Any: ...

class IDConverter(Converter): ...

class MemberConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Member: ...

class UserConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.User: ...

class MessageConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Message: ...

class TextChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.TextChannel: ...

class VoiceChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.VoiceChannel: ...

class CategoryChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.CategoryChannel: ...

class ColourConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Colour: ...

class RoleConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Role: ...

class GameConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Game: ...

class InviteConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Invite: ...

class EmojiConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Emoji: ...

class PartialEmojiConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.PartialEmoji: ...

class clean_content(Converter):
    def __init__(
        self,
        *,
        fix_channel_mentions: bool = ...,
        use_nicknames: bool = ...,
        escape_markdown: bool = ...,
    ) -> None: ...
    async def convert(self, ctx: Context, argument: str) -> str: ...

Greedy = List
