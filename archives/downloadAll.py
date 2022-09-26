# @app.route("/downloadAll", methods=["POST"])
# def downloadAll() :
#     dict = session["completingDict"]
#     reports = session["reportType"]
#     periods = session["period"]
    
#     iter = len(dict)

#     patterns = []

#     for ticker in dict.values() :
#         for report in reports :
#             for period in periods :
#                 pattern = (ticker, report, period)
#                 patterns.append(pattern)
    
#     session["iter"] = iter
#     session["patterns"] = patterns

#     for _ in range(iter) :
#         downloadAllExcute()

#     return redirect(url_for("initDict"))


# @app.route("/downloadAllExcute")
# def downloadAllExcute() :
    
#     if session["iter"] > 0 :
#         information = session["patterns"][0]
#         df = getFinancialDataframe2(information[0], information[1], information[2])

#         with io.BytesIO() as output :
#             with pandas.ExcelWriter(output, engine="xlsxwriter") as writer :
#                 df.to_excel(writer)
#             data = output.getvalue()
            
#         XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         filename = information[0] + "-" + information[1] + "-" + information[2] + ".xlsx"
#         response = make_response(data)
#         response.headers['Content-Disposition'] = 'attachment; filename=' + filename
#         response.mimetype = XLSX_MIMETYPE

#         #まずsession["patterns"]の[0]をデリートする。（既に使ったから）
#         del session["patterns"][0]
#         #次にsession[iter]の値をひとつ減らす。（これはカウンターとして機能する。）
#         session["iter"] -= 1

#         return response