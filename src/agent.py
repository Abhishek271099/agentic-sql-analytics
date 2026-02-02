from fastapi import HTTPException
from openai import AuthenticationError
from .logger import logger

class SQLAgent:

    def agent(self, sql_agent_prompt, sale_schema, dim_store_schema,
                  dim_date_schema, product_dimension_schema,
                      query, llm_client, model="gpt-4o"):
        try:
            response = llm_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": sql_agent_prompt.format(sale_schema=sale_schema, dim_date_schema=dim_date_schema,
                                                                              product_dimension_schema=product_dimension_schema,
                                                                              dim_store_schema = dim_store_schema,
                                                                              query=query)}]
            )

        except AuthenticationError:

            logger.error("Failed to generate SQL query; Invalid Credentials \u274c")
            raise HTTPException(status_code=401, detail=f"Failed to generated SQL query; Invalid Credentials")

        except Exception as e:
            logger.error(f"Failed to generate SQL query \u274c: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to generate SQL query\n{str(e)}")
 
        logger.info("SQL Agent generated a query \u2705")
        return response.choices[0].message.content
    

class ResponseAgent:

    def agent(self, llm_client, llm_agent_prompt, query, data, model="gpt-4o"):

        try:
            response = llm_client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": llm_agent_prompt.format(data=data, query=query)}]
                    )
            
        except AuthenticationError:

            logger.error("Failed to generate LLM Response; Invalid Credentials \u274c")
            raise HTTPException(status_code=401, detail=f"Failed to generated LLM Response; Invalid Credentials")
            
        except Exception as e:
            logger.error(f"Failed to generate final response \u274c: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to generate final response\n{str(e)}")

        logger.info("Response Agent generated a response \u2705")
        return response.choices[0].message.content