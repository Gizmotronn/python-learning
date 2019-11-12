import wikipedia
import wolframalpha

while True:
    pydainput = input("Ok Pyda!: ")

    if pydainput == "exit":
        break

    try:
        #wolframalpha
        app_id = "8A6LA2-ELRHR92Y88"
        client = wolframalpha.client(app_id)
        result = client.query(pydainput)
        answer = next(result.results).text
        print(answer)
    except:
        #wikipedia
        print(wikipedia.summary(pydainput))

        