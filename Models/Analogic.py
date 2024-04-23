from MCP3008 import *

# Definition of the analogic protocol
class Analogic:
    __MCP3008_ADconverter: MCP3008
    __mcp_ch: int = 0
    def __init__(self, mcp_ch: int) -> None:
        self.__mcp_ch = mcp_ch
        self.__MCP3008_ADconverter = MCP3008(self.__mcp_ch)