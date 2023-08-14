from preprocessors.text_preprocessor import TextPreprocessor

def test_url_decode():
    decoded_text = TextPreprocessor.url_decode("Hello%25252520world%25252521")
    assert decoded_text == "Hello world!"

def test_preprocess():
    preprocessed_text = TextPreprocessor.preprocess("Hello%25252520world%25252521")
    assert preprocessed_text == "Hello world!"
