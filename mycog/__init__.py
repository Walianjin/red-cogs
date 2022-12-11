from .mycog import horoscope

def setup(bot):
    bot.add_cog(MyCog(bot))
