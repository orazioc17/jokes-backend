from fastapi import APIRouter


router = APIRouter(
    prefix='/jokes',
    tags=['Jokes']
)


@router.get('')
def get_jokes():
    return "Hello world"
