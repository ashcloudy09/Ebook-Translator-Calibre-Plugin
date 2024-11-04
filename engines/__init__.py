from .google import (
    GoogleFreeTranslate, GoogleBasicTranslate, GoogleBasicTranslateADC,
    GoogleAdvancedTranslate, GeminiTranslate)
from .openai import ChatgptTranslate
from .anthropic import ClaudeTranslate
from .deepl import DeeplTranslate, DeeplProTranslate, DeeplFreeTranslate
from .youdao import YoudaoTranslate
from .baidu import BaiduTranslate
from .microsoft import MicrosoftEdgeTranslate, AzureChatgptTranslate


builtin_engines = (
    GoogleFreeTranslate, GoogleBasicTranslate, GoogleBasicTranslateADC,
    GoogleAdvancedTranslate, ChatgptTranslate, AzureChatgptTranslate,
    GeminiTranslate, ClaudeTranslate, DeeplTranslate, DeeplProTranslate,
    DeeplFreeTranslate, MicrosoftEdgeTranslate, YoudaoTranslate,
    BaiduTranslate)
