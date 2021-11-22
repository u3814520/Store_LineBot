from flask import Flask,request
import webSQL as q

app=Flask(__name__)

@app.route('/store')
def getSeries():
    store = request.args.get('store')
    city = request.args.get('city')
    dist = request.args.get('dist')
    address=request.args.get('address')
    return q.getStore()

@app.route('/',methods=['GET','POST'])
def store_post():
    outStr = """
    <form action="/" method="POST">
        <div>
            <label>請選擇查詢便利商店</label>
            <input name=s value=1 type="checkbox">
            <label for="s_type1">seveneleven</label>
            <input name=s value=2 type="checkbox">
            <label for="s_type2">familymart</label>
        </div>
        <div>
            <label>請輸入查詢縣市:</label>
            <input city="city">
        </div>
        <div>
            <label>請輸入查詢區域:</label>
            <input city="city">
        </div>
        <div>
            <label>是否街道查詢?</label>
            <input name=s value=1 type="checkbox">
            <label for="s_type1">是</label>
            <input name=s value=2 type="checkbox">
            <label for="s_type2">否</label>
        </div>
        <button type="submit">送出</button>
    </form>
    """
    method = request.method
    if method == 'POST':
        store_data = q.getStore()
        column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
        return render_template('show_staff.html', staff_data=staff_data,
                               column=column)

        outStr += """
        <div>Hello {}.</div>
        """.format(store)
    return outStr

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
