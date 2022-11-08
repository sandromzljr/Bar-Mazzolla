from sitebarmazzolla import app

if __name__ == '__main__':
    app.run(debug=True)


@app.before_first_request
def create_tables():
    app.database.create_all()
