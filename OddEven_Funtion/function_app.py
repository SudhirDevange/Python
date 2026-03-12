import logging
import azure.functions as func
from logic import check_odd_even

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="OddOrEven")
def OddOrEven(req: func.HttpRequest) -> func.HttpResponse:
    number = req.params.get('number')
    result = check_odd_even(number)
    
    if result:
        return func.HttpResponse(f"The number {number} is {result}.")
    return func.HttpResponse("Please pass a valid integer.", status_code=400)


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
