from bridge.tomorin import *
import requests
from PIL import Image
import io

6
def saltpeek(session: SessionExtension):
        res = requests.get('http://127.0.0.1:1919/my/screen') #获取电脑屏幕（https://github.com/YoisakiKnd/ChieriBot_peek_API）
        # 转化成png
        png = Image.open(io.BytesIO(res.content))
        output = io.BytesIO()
        png.save(output, format='PNG')
        image_binary = output.getvalue()
        session.send(F'{h.quote(session.message.id)}ty0是笨蛋{h.image(image_binary)}')
