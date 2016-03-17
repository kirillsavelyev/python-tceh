# -*- coding: utf-8 -*-

import config
from flask import Flask, request, render_template
from models import Storage, BlogPostModel
from forms import ContactForm

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
Storage.load_from_json_file()


@app.route('/', methods=['GET', 'POST'])
def home():
    storage = Storage()
    all_items = storage.items

    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            all_items.append(model)
            form = ContactForm()
            storage.dump_to_json_file()
    else:
        form = ContactForm()

    return render_template(
        'home.html',
        form=form,
        items=all_items)

if __name__ == '__main__':
    app.run()
