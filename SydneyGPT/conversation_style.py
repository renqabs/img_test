from enum import Enum

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal
from typing import Optional


class ConversationStyle(Enum):
    creative = [
        "nlu_direct_response_filter", 
        "deepleo", 
        "disable_emoji_spoken_text", 
        "responsible_ai_policy_235", 
        "enablemm", 
        "dv3sugg", 
        "autosave", 
        "iyxapbing", 
        "iycapbing", 
        "h3imaginative", 
        "clgalileo", 
        "gencontentv3", 
        "fluxsrtrunc", 
        "fluxtrunc", 
        "fluxv1", 
        "fluxv1short", 
        "rai278", 
        "replaceurl", 
        "weanow", 
        "logosv1", 
        "techeditgnd", 
        "eredirecturl"
        "nojbfedge",
    ]
    balanced = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "galileo",
        "dv3sugg",
        "responseos",
        "e2ecachewrite",
        "cachewriteext",
        "nodlcpcwrite",
        "travelansgnd",
    ]
    precise = [
        "nlu_direct_response_filter",
        "deepleo",
        "disable_emoji_spoken_text",
        "responsible_ai_policy_235",
        "enablemm",
        "galileo",
        "dv3sugg",
        "responseos",
        "e2ecachewrite",
        "cachewriteext",
        "nodlcpcwrite",
        "travelansgnd",
        "h3precise",
        "clgalileo",
    ]


CONVERSATION_STYLE_TYPE = Optional[
    Union[ConversationStyle, Literal["creative", "balanced", "precise"]]
]
