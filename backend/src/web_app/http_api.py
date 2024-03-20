from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from reports.report_from_local_csv import get_reports

app = FastAPI()


templates = Jinja2Templates(directory="web_app/templates")


@app.get("/", response_class=HTMLResponse)
def render_reports(request: Request):
    legislators, bills, errors = get_reports()
    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "legislators_report": legislators,
            "bills_report": bills,
            "errors": errors,
        },
    )
