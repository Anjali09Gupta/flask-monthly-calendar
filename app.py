from flask import Flask, render_template   # import Flask framework and function to load HTML
import calendar                            # import Python's calendar module

app = Flask(__name__)                      # create Flask app instance

@app.route("/")                            # define route for homepage ("/")
def home():                                # function that runs when user visits homepage
    year = 2026                            # set year (fixed for now)
    month = 3                              # set month (fixed for now)

    cal = calendar.HTMLCalendar(calendar.SUNDAY)   # create calendar object starting week from Sunday
    html_cal = cal.formatmonth(year, month)        # generate calendar in HTML format

    return render_template("index.html", calendar=html_cal)  
    # send HTML calendar to index.html

if __name__ == "__main__":                 # ensures app runs only when this file is executed
    app.run(debug=True)                    # run server in debug mode
