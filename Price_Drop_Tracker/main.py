"""
Author: hypaman
Date: 2021-06-25
Description: Discord webhook that alerts whenever a PS5 is
             back in stock or if a RTX 3070 is back in 
             stock. 
"""

# Imports
from discord_webhook import DiscordWebhook, DiscordEmbed 
from requests_html import HTMLSession

class Bob():
    """Bot object"""
    
    def __init__(self):
        """Init function, declaring variables."""
        # Webhook URL
        self.WEBHOOK = DiscordWebhook(url="https://discord.com/api/webhooks/806990374996410368/QqilGNrBo652oBEnsuX-BMkU1e8_PGIO4ENiyiQF_V6qtuQLkT6Z_1-lFmzmatp9M8Mz")
        
        # Executing Function
        # self.ExecuteEmbed()
        
    def ExecuteEmbed(self):
        """This function will call the embed"""
        
        Embed = DiscordEmbed(title="Test Title 123", 
                             description="Test Description 321",
                             color="eb5e34") 
        Embed.set_timestamp()
        
        self.WEBHOOK.add_embed(Embed)
        Execute = self.WEBHOOK.execute()
    
    def PS5Tracker(self):
        track = session.get("https://www.nowinstock.net/ca/videogaming/consoles/sonyps5/") 
    
    def RTX3070(self):
        pass
    
# Starting class
StartBob = Bob()

    
    