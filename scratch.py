settings = {
  'token': 'MTEyOTgyMjYyMDc3MTE3NjQ3OQ.Gc1XG1.w8fzPOJkUFOGeExuuV7o4BxzX_kj45y0nWGvxY',
  'bot': 'ViceM',
  'id': 1129822620771176479,
  'prefix': '!'
}
import discord
from discord import app_commands, SelectMenu, SelectOption
from discord.ext import commands
from shmotki import shmot

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())
embed=discord.Embed()



@bot.event
async def on_ready():
  print('Я готов ебашить')
  try:
      synced = await bot.tree.sync()
      print(f'Вот стока комманд: {len(synced)}')
  except Exception as e:
      print(e)

@bot.tree.command(name='search')
@app_commands.describe(item = 'Название вещи')
async def zapros(interaction: discord.Interaction, item: str):
  oba = item.title()
  g = list(shmot.keys())
  class MySelect(discord.ui.View):
    f = [g[i] for i in range(len(g)) if oba in g[i]]
    for i in range(len(f)):
      f[i] = SelectOption(label=f[i], value=str(i))
    @discord.ui.select(placeholder='Выберите вещь', options=f[:25])


    async def select_callback(self, select, interaction):
      interaction.disabled = True
      f = [g[i] for i in range(len(g)) if oba in g[i]]
      for o in range(len(f)):
          if interaction.values[0] == str(o):
            em=discord.Embed()
            em=discord.Embed(colour=0xFF8C00, title=str(f[o]), description=str(shmot[f[o]]))
            em.set_author(name='SEAGERS', icon_url='https://static-cdn.jtvnw.net/jtv_user_pictures/fb8d36f0-260e-4155-a65a-6d6a584cadb5-profile_image-70x70.png', url='https://www.youtube.com/@seagers')
            em.set_image(url='https://cdn.discordapp.com/attachments/900057340349407322/1205576760318763089/1.gif?ex=65d8dfda&is=65c66ada&hm=0f4b152135adc29a54afa9151bed7a8a759963376f79dcc17ec044b4fb12e4bd&')
            await select.response.send_message(embed=em, ephemeral=True)
  p = str(g)
  x = p.find(oba)
  if x == -1:
    await interaction.response.send_message(content='Вещей по запросу не найдено', ephemeral=True)
  elif len(item) < 3: await interaction.response.send_message(content='Нужно 3 или более символов для поиска вещи', ephemeral=True)
  else:
    view = MySelect()
    await interaction.response.send_message(view=view, ephemeral=True)

bot.run(settings['token'])
