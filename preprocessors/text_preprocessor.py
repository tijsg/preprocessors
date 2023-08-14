import re
import urllib.parse

class TextPreprocessor:
    @staticmethod
    def url_decode(input_text):
        decoded_text = input_text
        prev_decoded_text = ""
        while prev_decoded_text != decoded_text:
            prev_decoded_text = decoded_text
            decoded_text = urllib.parse.unquote(decoded_text)
        return decoded_text
    
    @staticmethod
    def remove_urls(input_text):
        url_pattern = re.compile(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?')
        modified_text = url_pattern.sub(':url:', input_text)
        return modified_text
    
    @staticmethod
    def preprocess(input_text):
        input_text = TextPreprocessor.url_decode(input_text)
        preprocessed = input_text
        return preprocessed
