import wikipedia
import wolframalpha

while True:
    input = input("Ok Pyda!: ")

    try:
        #wolframalpha
        app_id = "8A6LA2-ELRHR92Y88"
        client = wolframalpha.client(app_id)
        result = client.query(input)
        answer = next(result.results).text
        print(answer)
    except:
        #wikipedia
        print(wikipedia.summary(input))