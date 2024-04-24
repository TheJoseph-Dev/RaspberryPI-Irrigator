from gpiozero import MCP3008

# Definition of the analogic protocol
class Analogic:
    __MCP3008: MCP3008 # AD Converter
    __mcp_ch: int = 0
    def __init__(self, mcp_ch: int) -> None:
        self.__mcp_ch = mcp_ch
        self.__MCP3008 = MCP3008(self.__mcp_ch)