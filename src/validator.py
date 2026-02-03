from fastapi import HTTPException
from .logger import logger
class Validator:

    def is_forbidden(self, query):
        try:
            forbidden_keywords = ["DELETE", "UPDATE", "ALTER", "INSERT", "DROP", "TRUNCATE"]
        
            return any(word in query.upper() for word in forbidden_keywords)

        except Exception as e:
            logger.error("Failed during SQL query validation \u274c")

    

    