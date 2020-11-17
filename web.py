from views.view import app

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True, port=8088,host='0.0.0.0')
