import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="OddOrEven")
def OddOrEven(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get the 'number' from query string or request body
    number = req.params.get('number')
    if not number:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            number = req_body.get('number')

    if number:
        try:
            val = int(number)
            # Use modulus operator (%) to check even/odd logic
            result = "Even" if val % 2 == 0 else "Odd"
            return func.HttpResponse(f"The number {val} is {result}.")
        except ValueError:
            return func.HttpResponse("Please pass a valid integer.", status_code=400)
    else:
        return func.HttpResponse(
             "Please pass a number on the query string or in the request body",
             status_code=400
        )
