# !/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import boto3
    import tweepy
    translate = boto3.client(service_name='translate')

    def trans(text="Quindío representa bien la tragedia de la clase política tradicional.", SourceLanguageCode="es",
              TargetLanguageCode="en"):

        # print("Translating 'Amazon Family' from Espanol to English with no terminology...")
        response = translate.translate_text(Text=text, SourceLanguageCode=SourceLanguageCode,
                                            TargetLanguageCode=TargetLanguageCode)
        # print("Translated text: " + response.get('TranslatedText'))
        # print("\n")
        return response.get('TranslatedText')


    class TweetsListener(tweepy.StreamListener):

        def on_connect(self):
            print("Estoy conectado!")



        def on_status(self, status):
            print (status.id_str)
            print (trans(status.text))
            api.update_status(trans(status.text), in_reply_to_status_id=status.id_str , auto_populate_reply_metadata=True)

        def on_error(self, status_code):
            print("Error status code", status_code)

    id_fajardo = ["170103159"]#25185308
    #trans()
    consumer_key = "SZgvyXGaWwTspEB06t2Cl0dhN"
    consumer_secret = "ZbrWjnxWGvS52lzWoB6DvMyul0e5buEiSpa1qK8xe4297dgIvf"
    access_token = "1407827101194067969-QjbdxrxoULwCHUq9XfYZuleT7I5Rna"
    access_token_secret = "nzsEMghVKrS2dNuSbPLOHnq2Y1LjDWbOcQjLb4m4IBC72"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    stream = TweetsListener()
    streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
    streamingApi.filter(
        follow = id_fajardo,
        # track=["Coronavirus"],
        # locations=[-99.36492421,19.04823668,-98.94030286,19.59275713] # Ciudad de Mexico
    )
