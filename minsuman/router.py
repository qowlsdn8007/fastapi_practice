from sqlalchemy.orm import Session

from config import BASE_DIR
from fastapi import APIRouter, status, Depends
from fastapi.responses import RedirectResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from conn import db
from example import Click

router = APIRouter()
template = Jinja2Templates(directory='./')  # 프로젝트 내부 HTML 파일 참조

@router.get('/')
def get_page(request: Request, click:int = 0):
    return template.TemplateResponse('example.html', {'request': request, 'click': click})

@router.get('/clear')
def database_clear(session: Session = Depends(db.session)):   # fastapi의 DI 방식 지켜야함
    click = Click(click=0)
    session.add(click)
    session.commit()
    return RedirectResponse('/?click' + str(0), status_code=status.HTTP_303_SEE_OTHER)

@router.get('/start')
def add(session: Session = Depends(db.session)):
    click = session.query(Click).all()
    click = click[-1]
    click.click += 1  # BL
    session.add(click)
    session.commit()

    return RedirectResponse('/?click=' + str(click.click), status_code=status.HTTP_303_SEE_OTHER)