import azure.functions as func
from function_app import sync_tickets

# Classic model entrypoint

def main(req: func.HttpRequest) -> func.HttpResponse:
    return sync_tickets(req)
