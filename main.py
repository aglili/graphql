from fastapi import FastAPI
from fastapi_graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware



from .schema import Query,CreateTodo,DeleteTodo,UpdateTodo
from .database_config import get_db


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_api_route("/graphql", GraphQLApp(schema=Query,mutations=[CreateTodo,DeleteTodo,UpdateTodo]))



