from typing import Optional

import attr

from dis_snek.models.snowflake import Snowflake_Type
from dis_snek.models.base_object import DiscordObject
from dis_snek.utils.attr_utils import define, field


@define
class RoleTags:
    bot_id: Optional[Snowflake_Type] = attr.ib(default=None)
    integration_id: Optional[Snowflake_Type] = attr.ib(default=None)
    premium_subscriber: bool = attr.ib(default=False)  # TODO: detect null in process_dict


@define
class Role(DiscordObject):
    name: str = attr.ib()
    color: int = attr.ib()
    hoist: bool = attr.ib(default=False)
    position: int = attr.ib()
    permissions: str = attr.ib()  # TODO: permissions object
    managed: bool = attr.ib(default=False)
    mentionable: bool = attr.ib(default=True)
    tags: Optional["RoleTags"] = attr.ib(default=None)

    @property
    def is_bot_managed(self) -> bool:
        if self.tags is not None:
            return self.tags.bot_id is not None
        return False

    @property
    def is_integration(self) -> bool:
        if self.tags is not None:
            return self.tags.integration_id is not None
        return False

    @property
    def is_premium(self) -> bool:
        if self.tags is not None:
            return self.tags.premium_subscriber
        return False

    # TODO: is_default, requires guild_id == self.id
