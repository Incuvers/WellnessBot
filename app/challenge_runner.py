
import asyncio
import random
import discord
from .challenge import Challenge

class ChallengeRunner:
    """
    Runs challenges on a channel
    """
    intro = 'Wellness challenge'
    reactions = {
    'done':'🤸',
    'skipped':'😴'
    }

    def __init__(self, ctx, bot):
        self.ctx = ctx
        self.bot=bot
        self.message = None
        self.challenges = []

    def add_challenge(self, challenge):
        self.challenges.append(challenge)

    async def post(self):
        c = random.choice(self.challenges)
        payload = f'{ChallengeRunner.intro}. {c}'
        self.message = await self.ctx.send(payload)
        await self._add_reactions()
        await asyncio.sleep(c.get_timeout())
        users = await self._tally()
        return users

    def get_message(self):
        return self.message

    async def _tally(self):
        self.message = await self.ctx.fetch_message(self.message.id)

        if self.message is not None:
            r_done = discord.utils.find(lambda r: str(r.emoji) == ChallengeRunner.reactions['done'], self.message.reactions)

            payload="Challenge over, good job "
            async for u in r_done.users():
                if not u  == self.bot.user:
                    payload = payload +" "+ str(u)
            await self.message.delete()
            await self.ctx.send(payload)
            return r_done.users

    async def _add_reactions(self):
        if self.message is not None:
            await self.message.add_reaction(ChallengeRunner.reactions['done'])
