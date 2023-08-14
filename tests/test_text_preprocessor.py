from preprocessors.text_preprocessor import TextPreprocessor

def test_url_decode():
    decoded_text = TextPreprocessor.url_decode("Hello%25252520world%25252521")
    assert decoded_text == "Hello world!"

def test_remove_urls():
    preprocessed_text = TextPreprocessor.remove_urls("Check it at test.com or at https://www.test.com or test.com.")
    assert preprocessed_text == "Check it at :url: or at :url: or :url:."

def test_preprocess():
    preprocessed_text = TextPreprocessor.preprocess("Hello%25252520world%25252521")
    assert preprocessed_text == "Hello world!"
