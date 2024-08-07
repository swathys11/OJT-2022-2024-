from ast import keyword
#rule based text classification

def classify_request(text):
    text = text.lower()


    if any(keyword in text for keyword in ["billing", "invoice", "charge"]):
        return "Billing Issue"
    elif any(keyword in text for keyword in["passwotd", "access", "login", "account"]):
        return "Technical support"
    elif any(keyword in text for keyword in ["hours", "time", "location", "general"]):
        return "General support"
    else:
        return "other support"


#test sample
requests = [
    "my account is blocked",
    "i need my last details",
    "i need to know the timing of my order",

]

for request in requests:
    category = classify_request(request)
    print("request: ", request , "   category : ", category)
    