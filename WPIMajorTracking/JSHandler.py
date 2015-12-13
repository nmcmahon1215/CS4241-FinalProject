import BaseHandler
import os

class JSHandler(BaseHandler.BaseHandler):
    def get(self, *args, **kwargs):
        resultString = ""
        jsDir = "js/common"
        libsDir = "jsLibs"

        for fileName in sorted(os.listdir(libsDir)):
            resultString += getFileContents(fileName, libsDir);

        for fileName in sorted(os.listdir(jsDir)):
            resultString += getFileContents(fileName, jsDir)

        self.response.content_type = 'text/javascript'
        self.response.write(resultString)

def getFileContents(fileName, directory):
    fileDescriptor = open(os.path.join(directory, fileName))
    return fileDescriptor.read() + "\n"