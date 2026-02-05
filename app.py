######## HMA FOOD RATING ##########

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------- Data Setup --------------------
menu = {
    "Breakfast": [
        "Scrambled egg", "Chechebsa", "Ful", "Firfir", "Pizza",
        "Kenche", "Tibina", "Oat meal"
    ],
    "Lunch": [
        "Shiro", "Misr (with meat)", "Misr (without meat)",
        "Potato stew", "Meat stew", "Vegi", "Cabbage", "Beetroot"
    ],
    "Dinner": [
        "Rice with vegi sauce", "Rice with fish", "Rice with chicken",
        "Pasta", "Pasta lasagna", "Minestrone soup", "Maccaroni", "Chips"
    ],
    "Snack": [
        "Banana bread", "Fruit",
        "bomolino", "tsom cake", "pancakes"
    ]
}

votes = {}
comments = {}
for category in menu:
    for item in menu[category]:
        votes[item] = []
        comments[item] = []

# -------------------- Helper Functions --------------------
def calculate_average(rating_list):
    if len(rating_list) == 0:
        return None
    return sum(rating_list) / len(rating_list)

def total_votes_in_category(category):
    total = 0
    for item in menu[category]:
        total += len(votes[item])
    return total

# -------------------- Routes --------------------
@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/vote/<category>', methods=['GET','POST'])
def vote(category):
    if request.method == 'POST':
        item = request.form['item']
        rating = int(request.form['rating'])
        comment = request.form.get('comment','').strip()
        votes[item].append(rating)
        if comment != '':
            comments[item].append(comment)
        return redirect(url_for('index'))
    return render_template('vote.html', category=category, items=menu[category])

@app.route('/stats/<item>')
def stats(item):
    item_votes = votes[item]
    avg = calculate_average(item_votes)
    item_comments = comments[item]
    return render_template('stats.html', item=item, votes=item_votes, avg=avg, comments=item_comments)

@app.route('/category/<category>')
def category_summary(category):
    items = menu[category]
    total_votes = total_votes_in_category(category)
    best_item = None
    worst_item = None
    best_avg = -1
    worst_avg = 999
    for item in items:
        avg = calculate_average(votes[item])
        if avg is not None:
            if avg > best_avg:
                best_avg = avg
                best_item = item
            if avg < worst_avg:
                worst_avg = avg
                worst_item = item
    return render_template('category.html', category=category, items=items,
                           votes=votes, averages={i:calculate_average(votes[i]) for i in items},
                           best_item=best_item, best_avg=best_avg,
                           worst_item=worst_item, worst_avg=worst_avg,
                           total_votes=total_votes)

@app.route('/overall')
def overall():
    best_item = None
    worst_item = None
    best_avg = -1
    worst_avg = 999
    total_votes_overall = 0
    for category in menu:
        for item in menu[category]:
            avg = calculate_average(votes[item])
            total_votes_overall += len(votes[item])
            if avg is not None:
                if avg > best_avg:
                    best_avg = avg
                    best_item = item
                if avg < worst_avg:
                    worst_avg = avg
                    worst_item = item
    return render_template('overall.html', total_votes_overall=total_votes_overall,
                           best_item=best_item, best_avg=best_avg,
                           worst_item=worst_item, worst_avg=worst_avg)

@app.route('/all')
def all_items():
    return render_template('all.html', menu=menu, votes=votes)

# -------------------- Run App --------------------
if __name__ == '__main__':
   app.run(debug=True)
