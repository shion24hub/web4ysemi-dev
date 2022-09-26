from datetime import timedelta
from flask import (
    Flask,
    render_template,
    redirect,
    url_for, 
    request,
    session,
    Response,
    make_response,
)

import io
import os
import pandas
import random
import sys

from library.makeTickersDict.getTickers.minkabu import minkabu
from library.operations.getFinancials import getFinancialDataframe2

current_dir = os.getcwd()

sys.path.append(current_dir + "../web4ysemi/lib/makeTickersDict/")
sys.path.append(current_dir + "../web4ysemi/lib/makeTickersDict/getTickers/")
sys.path.append(current_dir + "../web4ysemi/lib/manipulatingDatabase/")


app = Flask(__name__)
app.config.from_pyfile("config.cfg")
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/")
def index():

    """
    later.

    """

    # VARIABLES

    ### PROCESS ###

    fileId = str(random.randrange(10**9, 10**10))

    session.permanent = True
    session["fileId"] = fileId
    session["optionsDict"] = {} #ティッカー検索で複数個の候補が見つかった場合、その辞書を格納する
    session["completingDict"] = {} #ユーザーが最終的に選んだティッカーが格納されていく
    
    return render_template(
        "index.html"
    )


@app.route("/initDict", methods=["POST"])
def initDict():

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    session["fileId"] = 0
    session["optionsDict"] = {}
    session["completingDict"] = {}
    session["reportType"] = []
    session["period"] = []

    return redirect(url_for("index"))


@app.route("/reportType", methods=["POST"])
def reportType():
    
    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    reportType = request.form.getlist("reportType")
    session["reportType"] = reportType
    
    return render_template(
        "period.html",
        reportType = session["reportType"]
    )


@app.route("/period", methods=["POST"])
def period():

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    period = request.form.getlist("period")
    session["period"] = period

    return render_template(
        "companySearch.html",
        reportType = session["reportType"],
        period = session["period"]
    )


@app.route("/companySearch", methods=["POST"])
def companySearch() :

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    return render_template(
        "select.html",
        reportType = session["reportType"],
        period = session["period"],
        companyName = request.form["companyName"]
    )


@app.route("/select", methods=["POST"])
def select():

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    #postされた情報を変数に格納する
    companyName = request.form["companyName"]

    #{companyName : ticker}を作成
    nameTickersDict = minkabu(companyName)

    #minkabu関数が返した辞書の要素数で分岐
    if len(nameTickersDict) == 1 :
        session["completingDict"].update(nameTickersDict)

        print(session["completingDict"])
        return redirect(url_for("searchingIndex"))
    
    elif len(nameTickersDict) == 0 :
        error = "Not a single candidate was found."
        return render_template(
            "nothing.html",
            companyName = companyName,
            reportType = session["reportType"],
            period = session["period"],
            error = error
        )

    else :
        nameOptions = list(nameTickersDict.keys())
        session["optionsDict"].update(nameTickersDict)

        return render_template(
            "select.html",
            reportType = session["reportType"],
            period = session["period"],
            companyName = companyName,
            nameTickersDict = nameTickersDict,
            nameOptions = nameOptions
        )


@app.route("/afterNothingSelected", methods=["POST"])
def afterNothingSelected() :

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    return redirect(url_for("searchingIndex"))
    

@app.route("/afterSelect", methods=["POST"])
def afterSelect():

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    nameSelected = request.form["nameSelected"]
    ticker = session["optionsDict"][nameSelected]
    session["completingDict"].update({nameSelected : ticker})

    return redirect(url_for("searchingIndex"))


@app.route("/searchingIndex")
def searchingIndex():

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    nameList = [name for name in session["completingDict"].keys()]
    return render_template(
        "searchingIndex.html",
        reportType = session["reportType"],
        period = session["period"],
        nameList = nameList,
        sessionDict = session["completingDict"]
    )

@app.route("/deleteCandidates", methods=["POST"])
def deleteCandidates():
    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    companyName = request.form["companyName"]
    
    del session["completingDict"][companyName]

    return redirect(url_for("searchingIndex"))


@app.route("/complete", methods=["POST"])
def complete():

    """
    later.
    """

    # VARIABLES

    ### PROCESS ###

    
    nameList = [name for name in session["completingDict"].keys()]
    return render_template(
        "download.html",
        nameList = nameList,
        Dict = session["completingDict"],
        reportTypes = session["reportType"],
        periods = session["period"]
    )


@app.route("/download", methods=["POST"])
def download() :
    information = request.form.getlist("information")
    df = getFinancialDataframe2(information[0], information[1], information[2])

    with io.BytesIO() as output :
        with pandas.ExcelWriter(output, engine="xlsxwriter") as writer :
            df.to_excel(writer)
        data = output.getvalue()
        
    XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    filename = information[0] + "-" + information[1] + "-" + information[2] + ".xlsx"
    response = make_response(data)
    response.headers['Content-Disposition'] = 'attachment; filename=' + filename
    response.mimetype = XLSX_MIMETYPE

    return response


if __name__ == "__main__":
    # app.run(debug=False)
    app.run()