from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from src.agent import SQLAgent, ResponseAgent
from src.llm_service import LLM
from src.sql_service import SQLClient
from src.validator import Validator
from src.logger import logger
from src.utils import regex_extract
from dotenv import load_dotenv
from src.agent_prompt import *
from src.schemas import * 
import json
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


@app.on_event("startup")
def startup():
    app.state.llm = LLM(endpoint=os.getenv("AZURE_ENDPOINT"), api_key=os.getenv("AZURE_API_KEY"))
    app.state.sql = SQLClient(server=os.getenv("SQL_SERVER"),
                    database=os.getenv("SQL_DATABASE"),
                    username=os.getenv("SQL_USERNAME"),
                    password=os.getenv("SQL_PASSWORD"))
    app.state.validator = Validator()
    app.state.sql_agent = SQLAgent()
    app.state.llm_agent = ResponseAgent()
    

@app.post('/generate_response', response_model=Response)
def generate_response(data: InputQuery):
    
    query = data.query

    conn = app.state.sql.get_conn()   
    sql_query = app.state.sql_agent.agent(sql_agent_prompt=sql_agent_prompt, sale_schema=sale_schema,
                                    dim_date_schema=dim_date_schema, dim_store_schema=dim_store_schema,
                                    product_dimension_schema=product_dimension_schema, query=query, llm_client=app.state.llm.get_client()
                                    )   
    clean_sql_query = regex_extract(sql_query)   

    if app.state.validator.is_forbidden(query=clean_sql_query):
        logger.critical("Unforbidden query encounterd, raising the exception")
        raise HTTPException(status_code=403, detail="SQL query failed validation and is forbidden. Cannot execute the operation.")
    
    sql_response = app.state.sql.get_data(conn=conn, sql_query=clean_sql_query)

    llm_response = app.state.llm_agent.agent(llm_client=app.state.llm.get_client(),
                                    llm_agent_prompt=llm_agent_prompt,
                                    query=query, data=sql_response)
    
    final_response = {
        "response": llm_response,
        "sql_query": clean_sql_query,
        "query": query
    }
    
    return HTMLResponse(content=json.dumps(final_response), status_code=200)



    






