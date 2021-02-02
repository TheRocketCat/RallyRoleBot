from typing import Optional
from datetime import datetime
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


class CoinPrice(BaseModel):
    coinKind: str
    priceInUSD: str
    usd_24h_change: Optional[str] = None


class CoinPrices(BaseModel):
    id: Optional[int] = None
    timeCreated: datetime
    coinKind: str
    priceInUSD: str