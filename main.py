from flask import Flask, render_template, request
from discord_webhook import DiscordWebhook, DiscordEmbed

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order_info = request.form
        orders = {'iron': order_info['ironblox'], 'ems': order_info['emstack'], 'helm': order_info['helm'],
                  'chestplates': order_info['chestplate'], 'leggings': order_info['legs'], 'boots': order_info['boots'],
                  'swords': order_info['sword'], 'pickaxe': order_info['pick'], 'shovel': order_info['shovel'],
                  'axe': order_info['axes'], 'discname': order_info['discord'], 'IGN': order_info['IGN']}
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/865489020036055041/Kzm9Cluk6GCwBhk8psRx2DWVUYoiWXs_D_GFVf4-i11CLJQFn6iyTrZYRXuCUy-35L92",
            username='NEW ORDER')
        embed = DiscordEmbed(title="new order", description="There is a new order to fulfil :(", color=0x00FFFF)
        newline = "\n"
        order_string = f"```{newline.join(['' + k + ': ' + str(v) for k,v in orders.items() if k not in ['IGN', 'discname']])}```"
        embed.add_embed_field(name="Items", value=order_string, inline=False)
        embed.add_embed_field(name="DISCORD NAME", value=orders['discname'], inline=True)
        embed.add_embed_field(name="IGN", value=orders['IGN'], inline=True)
        webhook.add_embed(embed)
        webhook.execute()
        return render_template('thanks.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5687, host='0.0.0.0')
