
class Validator:

    def is_forbidden(self, query):
        
        forbidden_keywords = ["DELETE", "UPDATE", "ALTER", "INSERT", "DROP", "TRUNCATE"]
       
        return any(word in query.upper() for word in forbidden_keywords)
    