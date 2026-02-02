from openai import AzureOpenAI, AuthenticationError
from fastapi import HTTPException
from .logger import logger

class LLM:

    def __init__(self, endpoint, api_key):

        try:        
            self.client = AzureOpenAI(
                azure_endpoint = endpoint,
                api_key = api_key,
                api_version = "2024-02-15-preview"
            )
            logger.info("LLM client initiated \u2705")

        except AuthenticationError:

            logger.error("Failed to get LLM client due to invalid credentials \u274c")
            raise HTTPException(status_code=401, detail="Failed to get LLM client due to invalid credentials")

        except Exception as e:

            logger.error(f"Failed to get OpenAI client \u274c: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to get OpenAI client\n{str(e)}")


    def get_client(self):
        
        return self.client
    
