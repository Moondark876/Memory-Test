import pygame
from pygame.locals import *
import asyncio
import random
from sys import exit
import aiohttp
import utils
from utils import Colours
import os
import utils
from utils.constants import NEWWORD_EVENT
from english_words import english_words_lower_alpha_set


class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.session = aiohttp.ClientSession()
        self.word = "start"
        self.need_word = False
        self.debugging = True
        self.score = 0
        self.seen = []
        pygame.display.set_caption('Memory Test')
        pygame.mixer.music.load(os.path.join('Assets', 'lobby music.wav'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.125)

    @staticmethod
    def pygamemethod(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    async def update():
        pygame.display.update()
        await asyncio.sleep(0.01)

    @pygamemethod
    async def get_word(self):
        return random.choice([*(list(english_words_lower_alpha_set)[i] for i in range(19)), random.choice(self.seen)])


    @pygamemethod
    async def see(self, seen):
        if seen not in self.seen:
            self.seen.append(seen)
        self.score += 1

    @pygamemethod
    async def blind(self):
        self.score = 0
        self.seen = []

    
    @pygamemethod
    async def coroutine(self):
        while self.need_word:
            self.word = await self.get_word()
            self.need_word = False


    @pygamemethod
    async def draw_window(self, word):
        self.screen.fill(utils.Colours.BLACK.rgb)
        self.screen.blit(utils.coin, utils.coin.get_rect(center=(30, 120)))
        self.screen.blit((x:=utils.FONT.render(str(self.score), True, Colours.WHITE.rgb)), x.get_rect(center=(90, 120)))
        pygame.draw.rect(self.screen, utils.Colours.WHITE.rgb, utils.rectangle)
        pygame.draw.rect(self.screen, utils.Colours.WHITE.rgb, utils.rectangle_2)
        self.screen.blit((x:=utils.BIGFONT.render("Memory Tester", True, utils.Colours.WHITE.rgb)), x.get_rect(center=(self.screen.get_width() / 2, 50)))
        self.screen.blit((x:=utils.FONT.render("Seen", True, Colours.BLACK.rgb)), x.get_rect(center=utils.rectangle.center))
        self.screen.blit((x:=utils.FONT.render("New", True, Colours.BLACK.rgb)), x.get_rect(center=utils.rectangle_2.center))
        self.screen.blit((x:=utils.BIGFONT.render(word, True, Colours.WHITE.rgb)), x.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2)))

    @pygamemethod
    async def main(self):
        pygame.event.post(pygame.event.Event(utils.NEWWORD_EVENT))
        while True:
            self.clock.tick()
            for event in pygame.event.get():
                if event.type == QUIT:
                    await self.blind()
                    await self.session.close()
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if utils.rectangle.collidepoint(*pygame.mouse.get_pos()):
                        if self.word not in self.seen:
                            await self.blind()
                            await self.session.close()
                            pygame.quit()
                            exit()
                        else:
                            self.need_word = True
                            await self.see(self.word)
                            pygame.event.post(pygame.event.Event(utils.NEWWORD_EVENT))
                    elif utils.rectangle_2.collidepoint(*pygame.mouse.get_pos()):
                        if self.word in self.seen:
                            await self.blind()
                            await self.session.close()
                            pygame.quit()
                            exit()
                        else:
                            self.need_word = True
                            await self.see(self.word)
                            pygame.event.post(pygame.event.Event(utils.NEWWORD_EVENT))

                elif event.type == NEWWORD_EVENT:
                    await asyncio.gather(self.coroutine())
                    

                    # if self.debugging == True:
                    #     if utils.rectangle.collidepoint(mousepos):
                    #         print("Clicked on rectangle")
                    #     elif utils.rectangle_2.collidepoint(mousepos):
                    #         print("Clicked on rectangle_2")
                    #     print(mousepos)
                # else:
                #     if self.debugging == True:
                #         print("event {event}".format(event=event))

            await self.draw_window(self.word)
            await self.update()
            

async def main():
    game = Game()
    await game.main()



if __name__ == "__main__":
    asyncio.run(main())
