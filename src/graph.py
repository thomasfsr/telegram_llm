from langchain_core.tools import tool
from typing import List, Type, Dict
import random
from pydantic import BaseModel, Field
from langchain.tools import BaseTool

## Schemas:

class ConsultInput(BaseModel):
    input_query: str = Field(description='Should be SQL command of SELECT type only')

class RandomInput(BaseModel):
    n_numbers:int = Field(description='Should be the number of random numbers')

class LowerCaseInput(BaseModel):
    text:str = Field(description="A text that will be lower case")

## Tools:

class Consult_Tool(BaseTool):
    name:str = 'consult_tool'
    description: str ="""To make analytical queries using select"""
    args_schema: Type[BaseModel] = ConsultInput

    def _run(self,
             input_query: str
             ) -> Dict:
        
        return input_numbers

class RandomTool(BaseTool):
    name:str='random_tool'
    description:str="""Returns a list of random numbers between 0-100."""
    args_schema: Type[BaseModel] = RandomInput

    def _run(self, n_numbers:int = None, **kwargs) -> List[int]:
        if n_numbers:
            return [random.randint(0, 100) for _ in range(n_numbers)]
        else:
            return 'give me the number of random numbers you need'

class LowerCaseTool(BaseTool):
    name:str = 'lower_case_tool'
    description:str= 'Returns the input as all lower case.'
    args_schema: Type[BaseModel] = LowerCaseInput
    def _run(self,
             text:str
             ) -> str:
        return text.lower()