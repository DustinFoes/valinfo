import discord
import requests
from discord.ext import commands


headers = {
    'X-Riot-Token': 'YOUR_API_KEY'  # Replace with your Valorant API key
}

base_url = 'https://api.valorant.riotgames.com/v1/'


#################################################################################################


# // VALORANT COMMANDS //

class Main(commands.Cog):
    def __init__(self, client):  # this is a special method that is called when the cog is loaded
        self.client = client

    headers = {
        'X-Riot-Token': 'YOUR_API_KEY'  # Replace with your Valorant API key
    }

    base_url = 'https://api.valorant.riotgames.com/v1/'

    @discord.slash_command()
    async def get_player_info(ctx, player_name):
        """Get information about a Valorant player."""
        url = f'{base_url}players?name={player_name}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            player_data = response.json()
            embed = discord.Embed(title='Player Info',
                                  color=discord.Color.green())
            embed.add_field(name='Player Name', value=player_data['name'])
            # Add more fields as needed
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Error', description='Unable to fetch player information.', color=discord.Color.red())
            await ctx.send(embed=embed)

    @discord.slash_command()
    async def get_match_history(ctx, player_name):
        """Get the match history of a Valorant player."""
        url = f'{base_url}matches?name={player_name}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            match_history = response.json()
            embed = discord.Embed(title='Match History',
                                  color=discord.Color.green())
            embed.add_field(name='Player Name', value=player_name)
            # Add more fields as needed
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Error', description='Unable to fetch match history.', color=discord.Color.red())
            await ctx.send(embed=embed)

    @discord.slash_command()
    async def get_leaderboard(ctx):
        """Get the Valorant leaderboard."""
        url = f'{base_url}leaderboards'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            leaderboard_data = response.json()
            embed = discord.Embed(title='Leaderboard',
                                  color=discord.Color.green())
            # Process and add fields from the leaderboard data
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Error', description='Unable to fetch leaderboard.', color=discord.Color.red())
            await ctx.send(embed=embed)

    @discord.slash_command()
    async def get_agent_info(ctx, agent_name):
        """Get information about a Valorant agent."""
        url = f'{base_url}agents?name={agent_name}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            agent_data = response.json()
            embed = discord.Embed(title='Agent Info',
                                  color=discord.Color.green())
            embed.add_field(name='Agent Name', value=agent_data['name'])
            # Add more fields as needed
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Error', description='Unable to fetch agent information.', color=discord.Color.red())
            await ctx.send(embed=embed)

    @discord.slash_command()
    async def get_latest_patch(ctx):
        """Get information about the latest Valorant patch."""
        url = f'{base_url}patches'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            patch_data = response.json()
            latest_patch = patch_data[0]
            patch_notes_url = latest_patch['blogLink']
            embed = discord.Embed(
                title=f"Latest Patch: {latest_patch['name']}", url=patch_notes_url, description=latest_patch['details'], color=discord.Color.green())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Error', description='Unable to fetch patch information.', color=discord.Color.red())
            await ctx.send(embed=embed)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Main(bot))
