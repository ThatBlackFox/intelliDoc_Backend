import docx2txt
from flask import request
import time
import os


class DocxHandler():
    def getText(request:request):
        data = request.files['file']
        data = docx2txt.process(data)
        print(data)
        return data
    def toFile(request:request,path=None):
        if not path:
            request.files['file'].save(f'temp/{int(time.time())}.docx')
        else:
            request.files['file'].save(os.path.join(path, f"{int(time.time())}.docx"))
