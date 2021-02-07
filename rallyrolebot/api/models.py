from typing import Optional
from pydantic import BaseModel


class ChannelMapping(BaseModel):
    id: Optional[int] = None
    guildId: Optional[str] = None
    coinKind: str
    requiredBalance: str
    channel: str


class RoleMapping(BaseModel):
    id: Optional[int] = None
    guildId: Optional[str] = None
    coinKind: str
    requiredBalance: str
    roleName: str


class CoinMapping(BaseModel):
    guildId: Optional[str] = None
    coinKind: Optional[str] = None


class PrefixMapping(BaseModel):
    guildId: Optional[str] = None
    prefix: str


class Command(BaseModel):
    name: str
    description: str


class BotNameMapping(BaseModel):
    bot_name: str
    name_timeout: Optional[int] = None


class BotAvatarMapping(BaseModel):
    bot_avatar: str
    avatar_timeout: Optional[int] = None
    guildId: Optional[str] = None


class BotInstanceMapping(BaseModel):
    bot_instance: str


class BotActivityMapping(BaseModel):
    success: Optional[str] = None
    activity_type: Optional[str] = None
    activity_text: Optional[str] = None
