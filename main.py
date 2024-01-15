from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
from schema import Query,Mutation
from database import Base, engine
from schema import create_schema


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

graphql_app = GraphQL(schema=create_schema())


app.add_route("/graphql", graphql_app)

