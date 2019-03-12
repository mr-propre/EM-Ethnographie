from flask import redirect, url_for 
from app import app 

if __name__ == '__main__':
    app.run() 

@app.route('/', methods=['GET', 'POST'])
def redirection():
	return redirect(url_for('base.index'))