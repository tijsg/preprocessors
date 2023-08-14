import urllib.parse

class TextPreprocessor:
    @staticmethod
    def url_decode(input_text):
        decoded_text = input_text
        prev_decoded_text = ""
        while prev_decoded_text != decoded_text:
            prev_decoded_text = decoded_text
            decoded_text = urllib.parse.unquote(decoded_text)
            if decoded_text == prev_decoded_text:
                break
        return decoded_text
    
    @staticmethod
    def preprocess(input_text):
        input_text = TextPreprocessor.url_decode(input_text)
        preprocessed = input_text
        return preprocessed
